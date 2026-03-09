# เพิ่ม code นี้ต่อจาก model.fit() ใน notebook ของคุณ

import pickle

# บันทึก model
model.save("ann_model.keras")

# บันทึก scaler
with open("ann_scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("✅ บันทึก ann_model.keras และ ann_scaler.pkl เรียบร้อย")
