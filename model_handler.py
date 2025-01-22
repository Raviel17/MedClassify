import tensorflow as tf
import numpy as np
from PIL import Image
import os

class MedicineClassifier:
    def __init__(self, model_path='model/model.keras'):
        self.model = None
        self.model_path = model_path
        self.class_names = self._load_class_names()
        self.target_size = (160, 160)
        
    def _load_class_names(self):
        try:
            with open('model/class_names.txt', 'r') as f:
                return f.read().splitlines()
        except:
            return []  # Return empty list if file not found
        
    def load_model(self):
        try:
            if self.model_path.endswith('.keras'):
                # Load model format .keras
                self.model = tf.keras.models.load_model(self.model_path)
            else:
                # Load SavedModel format sebagai inference layer
                self.model = tf.keras.layers.TFSMLayer(
                    self.model_path,
                    call_endpoint='serving_default'
                )
            print("Model loaded successfully")
            return True
        except Exception as e:
            print(f"Error loading model: {str(e)}")
            return False
    
    def predict(self, image_path):
        if self.model is None:
            if not self.load_model():
                return None
        
        try:
            # Load dan preprocess gambar
            img = Image.open(image_path)
            img = img.resize(self.target_size)
            img = img.convert('RGB')
            img_array = tf.keras.preprocessing.image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = img_array / 255.0
            
            # Prediksi
            predictions = self.model.predict(img_array)
            
            # Handle different model output formats
            if isinstance(predictions, dict):
                # For SavedModel format
                predictions = list(predictions.values())[0]
            
            predicted_class_index = np.argmax(predictions[0])
            confidence = float(predictions[0][predicted_class_index])
            
            if not self.class_names:
                return None
                
            return {
                'class': self.class_names[predicted_class_index],
                'confidence': confidence
            }
        except Exception as e:
            print(f"Error during prediction: {str(e)}")
            return None 