import os
import shutil
from pathlib import Path
import random

def setup_dataset_structure():
    """Membuat struktur folder dataset"""
    # Definisi path
    dataset_root = Path('dataset')
    train_dir = dataset_root / 'train'
    test_dir = dataset_root / 'test'
    
    # Buat direktori
    for dir_path in [train_dir, test_dir]:
        dir_path.mkdir(parents=True, exist_ok=True)
    
    print("✓ Struktur folder dataset telah dibuat")
    return train_dir, test_dir

def split_dataset(source_dir, train_dir, test_dir, split_ratio=0.8):
    """Membagi dataset menjadi training dan testing"""
    source_path = Path(source_dir)
    
    if not source_path.exists():
        print(f"Error: Folder {source_dir} tidak ditemukan!")
        return
    
    # Proses setiap kelas
    for class_folder in source_path.iterdir():
        if not class_folder.is_dir():
            continue
            
        class_name = class_folder.name
        print(f"\nMemproses kelas: {class_name}")
        
        # Buat folder kelas di train dan test
        train_class_dir = train_dir / class_name
        test_class_dir = test_dir / class_name
        train_class_dir.mkdir(exist_ok=True)
        test_class_dir.mkdir(exist_ok=True)
        
        # Daftar semua gambar
        images = []
        for ext in ['.jpg', '.jpeg', '.png']:
            images.extend(list(class_folder.glob(f'*{ext}')))
        
        if not images:
            print(f"Tidak ada gambar ditemukan di {class_folder}")
            continue
            
        # Acak urutan gambar
        random.shuffle(images)
        
        # Hitung pembagian
        n_train = int(len(images) * split_ratio)
        train_images = images[:n_train]
        test_images = images[n_train:]
        
        # Copy gambar ke folder train
        for img in train_images:
            try:
                dest = train_class_dir / img.name
                shutil.copy2(str(img), str(dest))
            except Exception as e:
                print(f"Error copying {img}: {str(e)}")
        print(f"✓ {len(train_images)} gambar disalin ke folder training")
        
        # Copy gambar ke folder test
        for img in test_images:
            try:
                dest = test_class_dir / img.name
                shutil.copy2(str(img), str(dest))
            except Exception as e:
                print(f"Error copying {img}: {str(e)}")
        print(f"✓ {len(test_images)} gambar disalin ke folder testing")

def main():
    print("=== Persiapan Dataset Klasifikasi Obat ===")
    
    # Setup struktur folder
    train_dir, test_dir = setup_dataset_structure()
    
    # Minta input folder sumber dataset
    while True:
        source_dir = input("\nMasukkan path folder yang berisi gambar obat: ")
        if os.path.isdir(source_dir):
            break
        print("Direktori tidak ditemukan. Silakan coba lagi.")
    
    # Split dataset
    split_dataset(source_dir, train_dir, test_dir)
    
    print("\n=== Proses Selesai ===")
    print("\nStruktur dataset yang dihasilkan:")
    print("dataset/")
    print("├── train/")
    print("└── test/")

if __name__ == "__main__":
    main() 