from tensorflow import keras
import numpy as np
from PIL import Image
import cv2
import time

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
img_counter = 0
frame_set = []
start_time = time.time()

labels = ['paper', 'scissors', 'stone']

model = keras.models.load_model('Aufgabe_06/model.h5')
model.load_weights("Aufgabe_06/model.weights.h5")

while True:
    ret, frame = capture.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if time.time() - start_time >= 1: #Check if howoften sec passed
        current_frame = cv2.resize(frame, (180, 180))
        current_frame = np.reshape(current_frame, (1, 180, 180, 3))
        pred = model.predict(current_frame)
        print(pred)
        print(labels[np.argmax(pred)])