from keras.models import load_model
from keras.preprocessing import image
# from keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
from resnet import top_5
import time
from keras.preprocessing.image import ImageDataGenerator

model = load_model('xception10.h5', custom_objects={'top_5': top_5})

class_list = ['OK', 'grinning', 'hand_over_mouth', 'rolling_eyes', 'shushing', 'smiling', 'thinking', 'thumbs_up', 'tougue', 'victory']

def predict(img):
    # y_prob = model.predict(np.expand_dims(img, axis=0))
    # y_class = y_prob.argmax(axis=-1)[0]
    x = image.img_to_array(img)
    x = x/255.0
    x = np.expand_dims(x, axis=0)
    #x = preprocess_input(x)

    preds = model.predict(x)
    top5 = sorted(range(len(preds)), key=lambda i: preds[i])[-5:]
    return top5#[class_list[top5[0]],class_list[top5[1]],class_list[top5[2]],class_list[top5[3]],class_list[top5[4]]]

# img0 = image.load_img('ACO1.jpg', target_size=(224, 224))
img1 = image.load_img('data/validation/grinning/grinning_face_3.jpg', target_size=(224, 224))
img2 = image.load_img('data/validation/hand_over_mouth/hand_over_mouth_3.jpg', target_size=(224, 224))
#img3 = image.load_img('data/validation/OK/OK_hand_3.jpg', target_size=(224, 224))
img4 = image.load_img('data/validation/rolling_eyes/face_with_rolling_eyes_3.jpg', target_size=(224, 224))
img5 = image.load_img('data/validation/shushing/shushing_face_3.jpg', target_size=(224, 224))
img6 = image.load_img('data/validation/smiling/slightly_smiling_3.jpg', target_size=(224, 224))
img7 = image.load_img('data/validation/thinking/thinking_face_3.jpg', target_size=(224, 224))
#img8 = image.load_img('data/validation/thumbs_up/thumbs_up_3.jpg', target_size=(224, 224))
img9 = image.load_img('data/validation/tongue/squinting_face_with_tongue_3.jpg', target_size=(224, 224))
#img10 = image.load_img('data/validation/victory/victory_3.jpg', target_size=(224, 224))

start = time.time()
# print(predict(img0))
print(predict(img1))
print(predict(img2))
#print(predict(img3))
print(predict(img4))
print(predict(img5))
print(predict(img6))
print(predict(img7))
#print(predict(img8))
print(predict(img9))
#print(predict(img10))
end = time.time()
print(end - start)

test_datagen = ImageDataGenerator(
        rescale=1./255)

test_generator = test_datagen.flow_from_directory(
        'data',
        target_size=(224, 224))

print(model.evaluate_generator(test_generator))