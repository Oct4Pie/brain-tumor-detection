import numpy as np
import pandas as pd
import tensorflow as tf
import os
import cv2
import imghdr
import random
import json
from tensorflow import keras
from tensorflow.keras import layers



def get_samples():
    # data_dir = os.path.join(os.getcwd(), "brain_tumor_dataset")
    data_dir = os.path.join(os.getcwd(), 'model', "cropped")
    paths = []
    img_formats = ["jpeg", "png", "jpg"]

    for directory in os.listdir(data_dir):
        for file in os.listdir(os.path.join(data_dir, directory)):
            file_path = os.path.join(data_dir, directory, file)
            print(file_path)
            if imghdr.what(file_path):
                if imghdr.what(file_path).lower() in img_formats:
                    paths.append(file_path)
            else:
                print(file_path, "not recognized")

    random.shuffle(paths)

    return paths


def get_test_samples(size):
    data_dir = os.path.join(os.getcwd(), "tests")
    paths = []
    sample_imgs = []
    img_formats = ["jpeg", "png", "jpg"]

    for directory in os.listdir(data_dir):
        for file in os.listdir(os.path.join(data_dir, directory)):
            file_path = os.path.join(data_dir, directory, file)
            print(file_path)
            if imghdr.what(file_path):
                if imghdr.what(file_path).lower() in img_formats:
                    paths.append(file_path)
            else:
                print(file_path, "not recognized")

    random.shuffle(paths)

    for image_path in paths:
        image = cv2.imread(image_path)
        image = cv2.resize(image, (size, size))
        sample_imgs.append(image)

    return np.array(sample_imgs)


def get_test_sample(img_name):
    img_formats = ["jpeg", "png", "jpg"]
    img = []

    for file in os.listdir("tests"):
        if img_name == file:
            file_path = os.path.join("tests", file)
            print(file_path)
            if imghdr.what(file_path):
                if imghdr.what(file_path).lower() in img_formats:
                    img.append(cv2.resize(cv2.imread(file_path), (size, size)))

    return np.array(img)


def classify(img_paths, size):
    read_images = []
    properties = []
    for image_path in img_paths:
        image = cv2.imread(image_path)
        image = cv2.resize(image, (size, size))
        read_images.append(image)
        properties.append(1) if "yes" in os.path.normpath(image_path).split(
            os.path.sep
        ) else properties.append(0)

    # read_images = np.array(tuple(random.sample(read_images, len(read_images))))
    # properties = np.array(tuple(random.sample(properties, len(properties))))
    # random.shuffle(read_images)
    # random.shuffle(properties)

    mn_list = list(zip(read_images, properties))
    mn_list = sorted(mn_list, key=lambda x: random.random())
    read_images, properties = zip(*mn_list)
    read_images = np.array(read_images)
    properties = np.array(properties)

    # print(len(read_images), len(properties))

    return read_images, properties


def train(read_images, properties):
    classes = 1
    train_len = len(read_images) - 400
    valid_data = read_images[train_len::]
    valid_prop = properties[train_len::]
    train_data = read_images[:train_len]
    train_prop = properties[:train_len]

    

    print(
        "\033[92m"
        + f"Training with {len(train_data)} images and validating with {len(valid_data)} images"
        + "\033[0m"
    )
    print("Shape:", train_data.shape, train_prop.shape)
    input("Press enter to continue...\n")

    train_data = np.array(train_data)
    valid_data = np.array(valid_data)
    train_data = train_data.astype("float32") / 255.0
    valid_data = valid_data.astype("float32") / 255.0

    model = keras.Sequential()
    model.add(
        layers.Conv2D(
            32,
            (3, 3),
            padding="SAME",
            activation="relu",
            input_shape=(size, size, 3),
        ),
    )
    model.add(layers.MaxPooling2D((2, 2), strides=2))
    model.add(layers.Conv2D(64, (3, 3), padding="SAME", activation="relu"))
    model.add(layers.MaxPooling2D((2, 2), strides=2))
    # model.add(layers.Dropout(0.25))
    model.add(layers.Dropout(0.7))
    model.add(layers.Flatten())
    model.add(layers.Dense(128, activation="relu"))
    model.add(layers.Dense(classes, activation="sigmoid"))

    model.compile(
        optimizer="adam", loss=tf.keras.losses.BinaryCrossentropy(), metrics=["accuracy"]
    )

    history = model.fit(
        train_data, train_prop, epochs=300, validation_data=(valid_data, valid_prop)
    )
    history_dic = history.history
    os.makedirs(os.path.join("model", "history"), exist_ok=True)
    json.dump(
        history_dic,
        open(
            os.path.join("model", "history", f'history_{len(os.listdir(os.path.join("model", "history")))}.json'), "w"
        ),
    )

    if input("Save model(y/N)? ").lower() == "y":
        model.save(os.path.join("model", "models", f"test_model_{len(os.listdir(os.path.join('model', 'models')))}"))


def rm_r_ds_store(path):
    os.system(f"find . -name '.DS_Store' -type f -delete")


if __name__ == "__main__":
    rm_r_ds_store(0)
    size = 50
    samples = get_samples()
    read_images, properties = classify(samples, size)
    # print( read_images, properties)
    train(read_images, properties)
