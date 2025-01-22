import os
import shutil
from PIL import Image

def create_directory_structure():
    """Membuat struktur direktori dataset"""
    base_dirs = ['dataset/train', 'dataset/test']
    classes = ['paracetamol', 'amoxicillin']  # Sesuaikan dengan kelas obat Anda
    
    for base_dir in base_dirs:
        for class_name in classes:
            os.makedirs(os.path.join(base_dir, class_name), exist_ok=True)

def prepare_image(image_path, output_size=(160, 160)):
    """Mempersiapkan gambar (resize dan normalisasi)"""
    with Image.open(image_path) as img:
        # Resize gambar
        img = img.resize(output_size, Image.LANCZOS)
        # Konversi ke RGB jika perlu
        if img.mode != 'RGB':
            img = img.convert('RGB')
        return img

def process_dataset():
    """Memproses seluruh dataset"""
    base_path = 'dataset'
    for split in ['train', 'test']:
        split_path = os.path.join(base_path, split)
        for class_name in os.listdir(split_path):
            class_path = os.path.join(split_path, class_name)
            if os.path.isdir(class_path):
                for img_name in os.listdir(class_path):
                    if img_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                        img_path = os.path.join(class_path, img_name)
                        try:
                            # Proses gambar
                            img = prepare_image(img_path)
                            # Simpan gambar yang sudah diproses
                            output_path = os.path.join(class_path, f'processed_{img_name}')
                            img.save(output_path, 'JPEG', quality=95)
                        except Exception as e:
                            print(f"Error processing {img_path}: {str(e)}")

if __name__ == "__main__":
    create_directory_structure()
    process_dataset() 