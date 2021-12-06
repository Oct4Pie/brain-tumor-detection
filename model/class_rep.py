from sklearn import model_selection
from tensorflow.keras import Sequential
from sklearn.metrics import classification_report
from modeler import classify, get_samples
from predictor import get_model
import numpy as np

samples = get_samples()
read_images, properties = classify(samples, 32)

train_len = len(read_images) - 400
valid_data = read_images[train_len::]
valid_prop = properties[train_len::]

valid_data = np.array(valid_data)
valid_data = valid_data.astype("float32") / 255.0

model, _, _ = get_model(6)
predicted = model.predict_classes(valid_data)
report = classification_report(valid_prop, predicted)
print(report)
