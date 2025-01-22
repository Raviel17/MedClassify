import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix, f1_score
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import pandas as pd

def evaluate_model():
    # Konfigurasi
    MODEL_PATH = 'model/model.keras'
    TEST_DIR = 'dataset/test'
    IMG_SIZE = (160, 160)
    BATCH_SIZE = 32

    # Load model
    print("Loading model...")
    model = tf.keras.models.load_model(MODEL_PATH)

    # Data generator untuk test set
    test_datagen = ImageDataGenerator(rescale=1./255)
    test_generator = test_datagen.flow_from_directory(
        TEST_DIR,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        shuffle=False
    )

    # Prediksi
    print("Making predictions...")
    predictions = model.predict(test_generator)
    y_pred = np.argmax(predictions, axis=1)
    y_true = test_generator.classes

    # Hitung metrics
    class_names = list(test_generator.class_indices.keys())
    
    # Classification report
    report = classification_report(y_true, y_pred, 
                                 target_names=class_names, 
                                 output_dict=True)
    
    # Convert report to DataFrame untuk visualisasi
    df_report = pd.DataFrame(report).transpose()
    
    # Plot F1-scores
    plt.figure(figsize=(12, 6))
    plt.bar(class_names, [report[cls]['f1-score'] for cls in class_names])
    plt.title('F1-Score per Class')
    plt.xlabel('Classes')
    plt.ylabel('F1-Score')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('evaluation/f1_scores.png')
    plt.close()

    # Confusion Matrix
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(12, 8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=class_names,
                yticklabels=class_names)
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.tight_layout()
    plt.savefig('evaluation/confusion_matrix.png')
    plt.close()

    # Save metrics to CSV
    df_report.to_csv('evaluation/classification_report.csv')

    # Print summary
    print("\nEvaluation Results:")
    print(f"Macro Avg F1-Score: {report['macro avg']['f1-score']:.4f}")
    print(f"Weighted Avg F1-Score: {report['weighted avg']['f1-score']:.4f}")
    
    # Plot additional metrics
    metrics = ['precision', 'recall', 'f1-score']
    plt.figure(figsize=(15, 6))
    
    x = np.arange(len(class_names))
    width = 0.25
    
    for i, metric in enumerate(metrics):
        values = [report[cls][metric] for cls in class_names]
        plt.bar(x + i*width, values, width, label=metric)
    
    plt.xlabel('Classes')
    plt.ylabel('Score')
    plt.title('Precision, Recall, and F1-Score per Class')
    plt.xticks(x + width, class_names, rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig('evaluation/all_metrics.png')
    plt.close()

if __name__ == "__main__":
    # Buat direktori untuk menyimpan hasil evaluasi
    import os
    os.makedirs('evaluation', exist_ok=True)
    
    print("=== Starting Model Evaluation ===")
    evaluate_model()
    print("\n=== Evaluation Complete ===")
    print("Results saved in 'evaluation' directory") 