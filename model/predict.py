from predictor import get_model
from mask import crop_img
import numpy as np
import sys
import cv2
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
path = os.path.realpath(sys.argv[1])
if not os.path.exists(path):
    print("path not valid")
    sys.exit()

img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.resize(img, (50, 50))
img = np.array([crop_img(gray, img, path)])
model, acc, loss = get_model()
predictions = model.predict_classes(img)
os.system("clear")
if predictions[0][0]:
    print(path, "has a tumor")
else:
    print(path, "has no tumor")
print("Confidence", model.predict(img))
