import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras

# Global Variables:
run_path = "./Data/Image"

# More Files:
run_full_dir = os.listdir(run_path)
run_dir = []
run_img = []
run_img_rgb = []

# Adds all files from the Images-dir into the run_img array and fileters all folders out
for i in run_full_dir:
    sing_run_img_path = os.path.join(run_path, i)
    if os.path.isfile(sing_run_img_path):
        run_dir.append(i)

# Turning the training-img into 500x500 pixel data
for i in run_dir:
    sing_run_img = cv2.imread(os.path.join(run_path, i))
    if sing_run_img is not None:
        run_img.append(cv2.resize(sing_run_img, (500, 500)))

# Converts all images from BRG to RGB
for img in run_img:
    run_img_rgb.append(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

run_img = np.array(run_img_rgb) / 255
run_img = run_img.reshape(-1, 500*500*3)

model_file = "rbcolor.keras"
model = keras.models.load_model(model_file)

predictions = model.predict(run_img)
for i in range(len(predictions)):
    print("Image:", run_dir[i])
    print(predictions[i])
    if np.argmax(predictions[i]) == 0:
        print("Output 1")
    elif np.argmax(predictions[i]) == 1:
        print("Output 2")
    elif np.argmax(predictions[i]) == 2:
        print("Output 3 (AI doesnt know)")
