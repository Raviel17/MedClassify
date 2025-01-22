import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time
import hashlib

class ImageDownloader:
    def __init__(self):
        self.setup_driver()
        
    def setup_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run in background
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), 
                                     options=options)
    
    def create_directory(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Dibuat direktori: {directory}")
    
    def download_image(self, url, save_path):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                # Generate unique filename using URL hash
                filename = hashlib.md5(url.encode()).hexdigest()[:10] + '.jpg'
                filepath = os.path.join(save_path, filename)
                
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                return True
        except Exception as e:
            print(f"Error downloading {url}: {str(e)}")
        return False
    
    def download_google_images(self, query, save_path, num_images=50):
        self.create_directory(save_path)
        
        # Format query untuk Google Images
        search_url = f"https://www.google.com/search?q={query}&tbm=isch"
        self.driver.get(search_url)
        
        # Scroll untuk memuat lebih banyak gambar
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        
        # Ambil URL gambar
        images = self.driver.find_elements(By.CSS_SELECTOR, 'img.rg_i')
        image_urls = []
        for img in images:
            try:
                img.click()
                time.sleep(1)
                actual_image = self.driver.find_elements(By.CSS_SELECTOR, 'img.n3VNCb')
                for actual in actual_image:
                    url = actual.get_attribute('src')
                    if url.startswith('http') and url not in image_urls:
                        image_urls.append(url)
                        if len(image_urls) >= num_images:
                            break
            except:
                continue
            
            if len(image_urls) >= num_images:
                break
        
        # Download gambar
        print(f"\nMengunduh {len(image_urls)} gambar untuk {query}...")
        success_count = 0
        for url in image_urls:
            if self.download_image(url, save_path):
                success_count += 1
                print(f"Progress: {success_count}/{len(image_urls)}", end='\r')
        
        print(f"\nBerhasil mengunduh {success_count} gambar untuk {query}")
    
    def close(self):
        self.driver.quit()

def main():
    # Daftar obat yang akan diunduh
    medicines = {
        'paracetamol': [
            'paracetamol tablet',
            'paracetamol medicine box',
            'paracetamol package',
        ],
        'amoxicillin': [
            'amoxicillin tablet',
            'amoxicillin medicine box',
            'amoxicillin package',
        ]
    }
    
    downloader = ImageDownloader()
    base_path = 'raw_dataset'
    
    try:
        for medicine, queries in medicines.items():
            medicine_path = os.path.join(base_path, medicine)
            print(f"\nMengunduh gambar untuk {medicine}...")
            
            for query in queries:
                print(f"\nQuery: {query}")
                downloader.download_google_images(query, medicine_path, num_images=20)
    
    finally:
        downloader.close()
    
    print("\nProses pengunduhan selesai!")
    print("Silakan periksa dan bersihkan dataset secara manual sebelum digunakan.")

if __name__ == "__main__":
    main() 