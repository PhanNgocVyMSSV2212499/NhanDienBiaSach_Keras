import os
import keras_ocr

image_dir = "MauBiaSach"
pipeline = keras_ocr.pipeline.Pipeline()

image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(".jpg")]
results = []

for img in image_files:
    img_path = os.path.join(image_dir, img)
    print(f"\n👉 Đang OCR ảnh: {img_path}")
    images = [keras_ocr.tools.read(img_path)]
    prediction_groups = pipeline.recognize(images)

    # Lấy toàn bộ text trong ảnh
    text_in_image = [text for text, box in prediction_groups[0]]

    # Ghép thành một câu
    sentence = " ".join(text_in_image)

    results.append((img, sentence))

    print(f"   → {sentence}")

# Xuất ra file ketqua.txt
with open("ketqua.txt", "w", encoding="utf-8") as f:
    for img, sentence in results:
        f.write(f"Ảnh: {img}\n")
        f.write(f"{sentence}\n\n")

print("\n✅ Hoàn tất! Kết quả đã lưu vào ketqua.txt")