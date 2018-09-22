from keras.preprocessing.image import ImageDataGenerator
from keras.applications.resnet50 import ResNet50
from keras.metrics import top_k_categorical_accuracy

from keras.preprocessing import image
import numpy as np
import time

from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D

def top_5(y_true, y_pred):
    return top_k_categorical_accuracy(y_true, y_pred, k=5)

if __name__ == '__main__':
    batch_size = 8

    train_datagen = ImageDataGenerator(
            rescale=1./255)#,
            # shear_range=0.2,
            # zoom_range=0.2,
            # horizontal_flip=True)

    train_generator = train_datagen.flow_from_directory(
            'data/train',
            target_size=(224, 224),
            batch_size=batch_size,
            class_mode='categorical',
            shuffle=True)

    test_datagen = ImageDataGenerator(
        rescale=1./255)

    validation_generator = test_datagen.flow_from_directory(
            'data/train',
            target_size=(224, 224),
            batch_size=batch_size,
            class_mode='categorical')

    # print(train_generator.filenames)

    model = ResNet50(include_top=True, weights=None, classes=2)
    # base_model = ResNet50(weights='imagenet', include_top=False)
    # x = base_model.output
    # x = GlobalAveragePooling2D()(x)
    # # let's add a fully-connected layer
    # x = Dense(1024, activation='relu')(x)
    # # and a logistic layer -- let's say we have 200 classes
    # predictions = Dense(7, activation='softmax')(x)

    # # this is the model we will train
    # model = Model(inputs=base_model.input, outputs=predictions)
    # for layer in base_model.layers:
    # layer.trainable = False

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    model.fit_generator(
            train_generator,
            steps_per_epoch=15 // batch_size,
            epochs=20,
            validation_data=validation_generator,
            validation_steps=15 // batch_size)
    # model.save('resnet32.h5')

    # print(model.evaluate_generator(test_generator))

    # class_list = ['OK', 'grinning', 'hand_over_mouth', 'rolling_eyes', 'shushing', 'smiling', 'thinking', 'thumbs_up', 'tougue', 'victory']

    # def predict(img):
    #     # y_prob = model.predict(np.expand_dims(img, axis=0))
    #     # y_class = y_prob.argmax(axis=-1)[0]
    #     x = image.img_to_array(img)
    #     x = x/255.0
    #     x = np.expand_dims(x, axis=0)
    #     #x = preprocess_input(x)

    #     preds = model.predict(x)
    #     return class_list[preds.argmax(axis=-1)[0]]

    # # img0 = image.load_img('ACO1.jpg', target_size=(224, 224))
    # img1 = image.load_img('data/grinning/grinning_face_3.jpg', target_size=(224, 224))
    # img2 = image.load_img('data/hand_over_mouth/hand_over_mouth_3.jpg', target_size=(224, 224))
    # img3 = image.load_img('data/OK/OK_hand_3.jpg', target_size=(224, 224))
    # img4 = image.load_img('data/rolling_eyes/face_with_rolling_eyes_3.jpg', target_size=(224, 224))
    # img5 = image.load_img('data/shushing/shushing_face_3.jpg', target_size=(224, 224))
    # img6 = image.load_img('data/smiling/slightly_smiling_3.jpg', target_size=(224, 224))
    # img7 = image.load_img('data/thinking/thinking_face_3.jpg', target_size=(224, 224))
    # img8 = image.load_img('data/thumbs_up/thumbs_up_3.jpg', target_size=(224, 224))
    # img9 = image.load_img('data/tongue/squinting_face_with_tongue_3.jpg', target_size=(224, 224))
    # img10 = image.load_img('data/victory/victory_3.jpg', target_size=(224, 224))

    # start = time.time()
    # # print(predict(img0))
    # print(predict(img1))
    # print(predict(img2))
    # print(predict(img3))
    # print(predict(img4))
    # print(predict(img5))
    # print(predict(img6))
    # print(predict(img7))
    # print(predict(img8))
    # print(predict(img9))
    # print(predict(img10))
    # end = time.time()
    # print(end - start)