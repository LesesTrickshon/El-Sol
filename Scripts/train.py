# Imports:
import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow import keras

# Global Variables:
# This part of the code loads the image-files into an array
# File Paths:
train_path = "./Data/Train Images"
rating_path = "./Data/rating.txt"

# More Files:
train_full_dir = os.listdir(train_path)
train_dir = []
train_img = []
train_img_rgb = []
train_txt = []

#Setting Up Image training:
# Adds all files from the trainings-dir into the train_img array and fileters all folders out
for i in train_full_dir:
    sing_train_img_path = os.path.join(train_path, i)
    if os.path.isfile(sing_train_img_path):
        train_dir.append(i)

# Turning the training-img into 500x500 pixel data
for i in train_dir:
    sing_train_img = cv2.imread(os.path.join(train_path, i))
    if sing_train_img is not None:
        train_img.append(cv2.resize(sing_train_img, (500, 500)))

# Turns converts all images from BRG to RGB
for img in train_img:
    train_img_rgb.append(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

# Normalizing the pic from 0-255 to 0.0 to 1.0 and put it into the correct format
train_img = np.array(train_img_rgb) / 255
train_img = train_img.reshape(-1,500*500*3)

# Setting up the text training
with open(rating_path, 'r') as file:
    # Read each line in the file
    for line in file:
        clean_line = line.strip()
        rating = float(clean_line)
        train_txt.append(rating)
train_txt = np.array(train_txt)

# Setting up the model
model = keras.Sequential([
    keras.layers.Dense(256, input_shape=[500*500*3], activation='relu'),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(3, activation='softmax')
])

# Compliling and training model
model.compile(optimizer="adam", loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(train_img, train_txt, epochs=50, batch_size=32)

# Tests the model and outputs accuracy score
model_loss, model_acc = model.evaluate(train_img, train_txt, verbose=1)
print(f"The Model is {int(model_acc*100)}% accurat")

# Save the model as a file with a specific name
model_save_file_name = input("What should the model be named?: ") + ".keras"
model.save(model_save_file_name)
