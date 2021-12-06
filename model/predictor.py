import tensorflow as tf
import os
import numpy as np
import cv2
import imghdr
from modeler import get_samples, classify


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


def get_model(num=0):
    os.system(f"find . -name '.DS_Store' -type f -delete")
    samples = get_samples()
    read_images, properties = classify(samples, 32)
    train_len = len(read_images) - 400
    train_img = read_images[:train_len]
    train_lbl = properties[:train_len]

    val_img = read_images[train_len::]
    val_lbl = properties[train_len::]
    model = tf.keras.models.load_model(f"model/models/test_model_{num}")
    loss, acc = model.evaluate(train_img, train_lbl, verbose=2)

    return model, acc, loss


if __name__ == "__main__":
    model, acc, loss = get_model()
    print(model.summary())
    print("\033[92m" + "Model restored; accuracy: {:%}".format(acc) + "\033[0m")

    while 1:
        sample = get_test_sample(input())
        predictions = model.predict(sample)
        pred_class = model.predict_classes(sample)
        print("predictions shape:", predictions)
        print("prediction class:", pred_class)
