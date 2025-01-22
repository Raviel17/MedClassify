from flask import Flask, render_template, request, jsonify, flash
from werkzeug.utils import secure_filename
import os
import numpy as np
from PIL import Image
from medicine_info import MEDICINE_INFO, get_medicine_info
from model_handler import MedicineClassifier

app = Flask(__name__)
app.secret_key = 'rahasia123'

# Konfigurasi upload
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Pastikan folder uploads ada
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Inisialisasi classifier
classifier = MedicineClassifier(model_path='model/model.keras')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print("POST request received")
        
        if 'image' not in request.files:
            print("No image in request.files")
            return render_template('index.html', error="Tidak ada file yang dipilih")
        
        file = request.files['image']
        print("File received:", file.filename)
        
        if file.filename == '':
            return render_template('index.html', error="Tidak ada file yang dipilih")
        
        if file and allowed_file(file.filename):
            try:
                # Simpan file
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                print("File saved to:", filepath)
                
                # Prediksi menggunakan model
                result = classifier.predict(filepath)
                print("Prediction result:", result)
                
                if result is None:
                    return render_template('index.html', 
                                        error="Gagal melakukan prediksi gambar")
                
                predicted_class = result['class']
                confidence = result['confidence']
                
                # Dapatkan informasi obat dengan rekomendasi
                medicine_info = get_medicine_info(predicted_class, confidence)
                
                print("Medicine info:", medicine_info)
                
                return render_template('index.html',
                                     prediction=predicted_class,
                                     confidence=f"{confidence:.2%}",
                                     medicine_info=medicine_info,
                                     filename=filename)
                
            except Exception as e:
                print("Error during prediction:", str(e))
                import traceback
                traceback.print_exc()
                return render_template('index.html', 
                                     error=f"Terjadi kesalahan: {str(e)}")
        else:
            return render_template('index.html', 
                                 error="Format file tidak didukung. Gunakan PNG, JPG, atau JPEG")
    
    return render_template('index.html')

if __name__ == '__main__':
    # Load model saat startup
    if classifier.load_model():
        print("Model loaded successfully")
    else:
        print("Failed to load model")
    
    app.run(debug=True) 