import cv2
import os

# Görüntülerin bulunduğu klasör
image_folder = 'images'  # Dosya yolunu güncelleyin
image_files = os.listdir(image_folder)  # Klasördeki tüm dosyaları listele

for img_file in image_files:
    img_path = os.path.join(image_folder, img_file)  # Dosya yolunu oluştur
    img = cv2.imread(img_path)  # Görüntüyü oku

    # Görüntünün başarıyla yüklendiğini kontrol et
    if img is None:
        print(f"Görüntü yüklenemedi: {img_path}")
        continue  # Eğer yüklenemezse bir sonraki dosyaya geç

    # Görüntüyü göster
    cv2.imshow('Image', img)
    cv2.waitKey(0)  # Her bir görüntüyü görmek için bir tuşa basmayı bekle

cv2.destroyAllWindows()  # Tüm pencereleri kapat
