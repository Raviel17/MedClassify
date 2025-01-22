import cv2
import os
from pathlib import Path
import glob

class VideoProcessor:
    def __init__(self, output_dir='raw_dataset'):
        self.output_dir = Path(output_dir)
        
    def create_directories(self, class_name):
        """Membuat direktori untuk menyimpan frame"""
        class_dir = self.output_dir / class_name
        class_dir.mkdir(parents=True, exist_ok=True)
        return class_dir
        
    def extract_frames(self, video_path, class_name, frame_interval=15):
        """
        Mengekstrak frame dari video
        Args:
            video_path: Path ke file video
            class_name: Nama kelas obat (misal: 'paracetamol')
            frame_interval: Ambil frame setiap n frame
        """
        try:
            output_dir = self.create_directories(class_name)
            
            video = cv2.VideoCapture(video_path)
            if not video.isOpened():
                print(f"Error: Tidak dapat membuka video {video_path}")
                return
            
            frame_count = 0
            saved_count = 0
            
            while True:
                success, frame = video.read()
                if not success:
                    break
                
                if frame_count % frame_interval == 0:
                    frame = cv2.resize(frame, (160, 160))
                    output_path = output_dir / f"{class_name}_{Path(video_path).stem}_{saved_count:04d}.jpg"
                    cv2.imwrite(str(output_path), frame)
                    saved_count += 1
                    
                    print(f"\rMenyimpan frame {saved_count} dari {video_path}", end="")
                
                frame_count += 1
            
            print(f"\nBerhasil menyimpan {saved_count} frame dari {video_path}")
            video.release()
            
        except Exception as e:
            print(f"Error memproses video {video_path}: {str(e)}")

def scan_video_directory(base_dir):
    """Scan direktori untuk menemukan semua video"""
    videos = {}
    
    # Daftar ekstensi video yang didukung
    video_extensions = ['.mp4', '.avi', '.mov', '.mkv']
    
    # Scan setiap subdirektori
    for dir_path in Path(base_dir).iterdir():
        if dir_path.is_dir():
            class_name = dir_path.name
            video_files = []
            
            # Cari semua file video dalam direktori
            for ext in video_extensions:
                video_files.extend(dir_path.glob(f'*{ext}'))
            
            if video_files:
                videos[class_name] = [str(v) for v in video_files]
                print(f"Ditemukan {len(video_files)} video untuk {class_name}")
    
    return videos

def main():
    # Konfigurasi
    video_processor = VideoProcessor()
    
    print("=== Ekstraksi Frame dari Video ===")
    
    # Minta input direktori video
    while True:
        video_dir = input("\nMasukkan path direktori yang berisi folder-folder video obat: ")
        if os.path.isdir(video_dir):
            break
        print("Direktori tidak ditemukan. Silakan coba lagi.")
    
    # Scan direktori untuk menemukan video
    print("\nMencari video...")
    videos = scan_video_directory(video_dir)
    
    if not videos:
        print("Tidak ada video yang ditemukan!")
        return
    
    # Tampilkan ringkasan
    print("\nRingkasan video yang ditemukan:")
    for class_name, video_paths in videos.items():
        print(f"{class_name}: {len(video_paths)} video")
    
    # Konfirmasi untuk melanjutkan
    confirm = input("\nLanjutkan ekstraksi frame? (y/n): ")
    if confirm.lower() != 'y':
        print("Proses dibatalkan")
        return
    
    # Proses setiap video
    total_videos = sum(len(v) for v in videos.values())
    processed_videos = 0
    
    for class_name, video_paths in videos.items():
        print(f"\nMemproses video untuk {class_name}...")
        
        for video_path in video_paths:
            processed_videos += 1
            print(f"\nVideo {processed_videos}/{total_videos}")
            print(f"Mengekstrak frame dari {video_path}")
            
            video_processor.extract_frames(
                video_path=video_path,
                class_name=class_name,
                frame_interval=15
            )
    
    print("\n=== Proses Selesai ===")
    print("\nLangkah selanjutnya:")
    print("1. Periksa hasil ekstraksi di folder 'raw_dataset'")
    print("2. Hapus frame yang blur atau tidak relevan")
    print("3. Jalankan organize_dataset.py untuk membagi data train/test")

if __name__ == "__main__":
    main() 