"""
train_models.py
รัน 1 ครั้งตอน app เริ่มต้น เพื่อ train และ cache โมเดลทั้ง 2 ไว้ใน session
"""

import pandas as pd
import numpy as np
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# ══════════════════════════════════════════════════════════════════
# ANN MODEL  (StudentsPerformance.csv)
# ══════════════════════════════════════════════════════════════════
def train_ann():
    df = pd.read_csv("ANN/StudentsPerformance.csv")
    df = df.drop_duplicates().reset_index(drop=True)

    df["average_score"]        = (df["math score"] + df["reading score"] + df["writing score"]) / 3
    df["language_score"]       = (df["reading score"] + df["writing score"]) / 2
    df["stem_strength"]        = df["math score"] - df["language_score"]
    df["reading_writing_diff"] = abs(df["reading score"] - df["writing score"])
    df["pass_math"]            = (df["math score"]    >= 50).astype(int)
    df["pass_reading"]         = (df["reading score"] >= 50).astype(int)
    df["pass_writing"]         = (df["writing score"] >= 50).astype(int)
    df["pass_all"]             = ((df["math score"] >= 50) & (df["reading score"] >= 50) & (df["writing score"] >= 50)).astype(int)
    df["final_pass"]           = (df["average_score"] >= 50).astype(int)

    df["gender"]                      = df["gender"].map({"male": 0, "female": 1})
    df["lunch_quality"]               = df["lunch"].map({"standard": 1, "free/reduced": 0})
    df["prepared"]                    = df["test preparation course"].map({"none": 0, "completed": 1})
    df["parental level of education"] = df["parental level of education"].map(
        {"some high school": 0, "high school": 1, "some college": 2,
         "associate's degree": 3, "bachelor's degree": 4, "master's degree": 5})
    df["race/ethnicity"]              = df["race/ethnicity"].map(
        {"group A": 0, "group B": 1, "group C": 2, "group D": 3, "group E": 4})
    df.drop(columns=["lunch", "test preparation course"], inplace=True)

    X = df[["gender", "race/ethnicity", "parental level of education",
            "language_score", "stem_strength", "reading_writing_diff",
            "lunch_quality", "prepared"]]
    y = df["final_pass"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)

    model = Sequential([
        Dense(32, activation="relu", input_shape=(X_train_s.shape[1],)),
        Dense(16, activation="relu"),
        Dense(8,  activation="relu"),
        Dense(1,  activation="sigmoid"),
    ])
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
    model.fit(X_train_s, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=0)

    return model, scaler


# ══════════════════════════════════════════════════════════════════
# ENSEMBLE MODEL  (Titanic train.csv)
# ══════════════════════════════════════════════════════════════════
def train_ensemble():
    train_df = pd.read_csv("Ensemble/train.csv")

    def preprocess(df):
        data = df.copy()
        data['Title'] = data['Name'].str.extract(r' ([A-Za-z]+)\.', expand=False)
        rare = ['Dr','Rev','Col','Major','Mlle','Countess','Capt',
                'Ms','Lady','Jonkheer','Don','Dona','Mme','Sir']
        data['Title'] = data['Title'].replace(rare, 'Rare')

        data['FamilySize'] = data['SibSp'] + data['Parch'] + 1
        data['IsAlone']    = (data['FamilySize'] == 1).astype(int)

        age_median = data.groupby(['Title', 'Pclass'])['Age'].transform('median')
        data['Age'] = data['Age'].fillna(age_median).fillna(data['Age'].median())
        data['Fare'] = data['Fare'].fillna(
            data.groupby('Pclass')['Fare'].transform('median'))
        data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])

        data['AgeBand']  = pd.cut(data['Age'], bins=[0,12,18,35,60,100],
                                   labels=[0,1,2,3,4]).astype(int)
        data['FareBand'] = pd.qcut(data['Fare'], q=4,
                                    labels=[0,1,2,3], duplicates='drop').astype(int)

        data['Sex']      = LabelEncoder().fit_transform(data['Sex'])
        data['Embarked'] = LabelEncoder().fit_transform(data['Embarked'])
        data['Title']    = LabelEncoder().fit_transform(data['Title'])
        data['HasCabin'] = data['Cabin'].notna().astype(int)

        data.drop(columns=[c for c in
            ['PassengerId','Name','Ticket','Cabin','SibSp','Parch']
            if c in data.columns], inplace=True)
        return data

    train_processed = preprocess(train_df)
    FEATURES = [c for c in train_processed.columns if c != 'Survived']
    X = train_processed[FEATURES].values
    y = train_processed['Survived'].values

    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y)

    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)

    svm = SVC(C=1.0, kernel='rbf', gamma='scale', probability=True, random_state=42)
    ann = MLPClassifier(
        hidden_layer_sizes=(128, 64, 32), activation='relu', solver='adam',
        alpha=0.001, learning_rate='adaptive', learning_rate_init=0.001,
        max_iter=500, early_stopping=True, validation_fraction=0.1,
        n_iter_no_change=20, random_state=42)
    rf  = RandomForestClassifier(
        n_estimators=300, max_depth=8, min_samples_split=4, min_samples_leaf=2,
        max_features='sqrt', oob_score=True, class_weight='balanced',
        random_state=42, n_jobs=-1)

    ensemble = VotingClassifier(
        estimators=[('svm', svm), ('ann', ann), ('rf', rf)],
        voting='soft', weights=[1, 1, 1.5])
    ensemble.fit(X_train_s, y_train)

    return ensemble, scaler, FEATURES
