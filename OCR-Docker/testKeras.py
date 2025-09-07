import os
import easyocr

# Thư mục chứa ảnh
image_dir = "MauBiaSach"

# Khởi tạo EasyOCR hỗ trợ tiếng Việt
reader = easyocr.Reader(['vi'])

# Lấy danh sách file ảnh .jpg trong thư mục
image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(".jpg")]

if not image_files:
    print(f"⚠ Không tìm thấy ảnh .jpg trong thư mục: {image_dir}")
    exit()

results = []

# OCR từng ảnh
for img in image_files:
    img_path = os.path.join(image_dir, img)
    print(f"\n👉 Đang OCR ảnh: {img_path}")
    
    try:
        result = reader.readtext(img_path, detail=0)
        sentence = " ".join(result)
    except Exception as e:
        sentence = f"Lỗi OCR: {e}"
    
    results.append((img, sentence))
    print(f"   → {sentence}")

# Đường dẫn tuyệt đối tới file kết quả
output_path = os.path.join(os.getcwd(), "ketqua.txt")

# Xuất ra file ketqua.txt
with open("ketqua.txt", "w", encoding="utf-8") as f:
    for img, sentence in results:
        f.write(f"Ảnh: {img}\n")
        f.write(f"{sentence}\n\n")

print("\n✅ Hoàn tất! Kết quả đã lưu vào ketqua.txt")