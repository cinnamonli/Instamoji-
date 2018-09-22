from keras.preprocessing.image import ImageDataGenerator
from keras.applications.xception import Xception
from keras.metrics import top_k_categorical_accuracy

def top_5(y_true, y_pred):
    return top_k_categorical_accuracy(y_true, y_pred, k=5)

if __name__ == '__main__':
    batch_size = 16

    train_datagen = ImageDataGenerator(
            rescale=1./255,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True)

    train_generator = train_datagen.flow_from_directory(
            'data',
            target_size=(224, 224),
            batch_size=batch_size,
            class_mode='categorical',
            shuffle=True)

    model = Xception(include_top=True, weights=None, classes=10)

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy', top_5])

    model.fit_generator(
            train_generator,
            steps_per_epoch=125 // batch_size,
            epochs=10)
    model.save('xception10.h5')