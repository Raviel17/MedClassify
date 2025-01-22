import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
import os

def create_model(num_classes):
    # Gunakan MobileNetV2 dengan ukuran input yang lebih kecil
    base_model = MobileNetV2(weights='imagenet', 
                            include_top=False, 
                            input_shape=(160, 160, 3))
    
    # Freeze base model layers
    for layer in base_model.layers:
        layer.trainable = False
    
    # Tambahkan custom layers yang lebih sederhana
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(64, activation='relu')(x)
    predictions = Dense(num_classes, activation='softmax')(x)
    
    model = Model(inputs=base_model.input, outputs=predictions)
    return model

def train_model():
    # Konfigurasi
    BATCH_SIZE = 16
    EPOCHS = 10
    IMG_SIZE = (160, 160)
    TRAIN_DIR = 'dataset/train'
    TEST_DIR = 'dataset/test'
    
    # Data augmentation yang lebih sederhana
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=10,
        width_shift_range=0.1,
        height_shift_range=0.1,
        horizontal_flip=True
    )

    test_datagen = ImageDataGenerator(rescale=1./255)

    print("Loading training data...")
    train_generator = train_datagen.flow_from_directory(
        TRAIN_DIR,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        shuffle=True
    )

    print("Loading validation data...")
    test_generator = test_datagen.flow_from_directory(
        TEST_DIR,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        shuffle=False
    )

    # Buat model
    print("Creating model...")
    num_classes = len(train_generator.class_indices)
    model = create_model(num_classes)

    # Compile dengan optimizer yang lebih conservative
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    # Pastikan direktori model ada
    os.makedirs('model', exist_ok=True)

    # Callbacks
    checkpoint = tf.keras.callbacks.ModelCheckpoint(
        'model/best_model.keras',
        monitor='val_accuracy',
        save_best_only=True,
        mode='max',
        verbose=1
    )

    early_stopping = tf.keras.callbacks.EarlyStopping(
        monitor='val_loss',
        patience=3,
        restore_best_weights=True
    )

    # Training dengan error handling
    try:
        # Clear any existing models from memory
        tf.keras.backend.clear_session()
        
        print("Starting training...")
        history = model.fit(
            train_generator,
            epochs=EPOCHS,
            validation_data=test_generator,
            callbacks=[checkpoint, early_stopping]
        )
        
        print("Evaluating model...")
        test_loss, test_accuracy = model.evaluate(test_generator)
        print(f"\nTest accuracy: {test_accuracy:.4f}")
        
        # Save model and class names
        print("Saving model and class names...")
        model.save('model/model.keras')
        
        class_names = list(train_generator.class_indices.keys())
        with open('model/class_names.txt', 'w') as f:
            f.write('\n'.join(class_names))
        
        return history
        
    except Exception as e:
        print(f"Error during training: {str(e)}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    print("=== Starting Model Training ===")
    
    # Set memory growth
    gpus = tf.config.experimental.list_physical_devices('GPU')
    if gpus:
        try:
            for gpu in gpus:
                tf.config.experimental.set_memory_growth(gpu, True)
        except RuntimeError as e:
            print(e)
    
    # Train model
    history = train_model()
    
    if history:
        print("\n=== Training completed successfully! ===")
    else:
        print("\n=== Training failed! ===") 