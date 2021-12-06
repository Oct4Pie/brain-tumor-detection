import matplotlib.pyplot as plt
import os
import json
import mplcursors
from predictor import get_model

mplcursors.cursor(hover=True)

model, _, _ = get_model(6)
choices = os.listdir("history")
choice = input(f"Choose\n{choices}: ")
if choice not in choices:
    exit()
model_hist = json.loads(open(os.path.join("history", choice)).read())
accuracy = model_hist["accuracy"]
val_accuracy = model_hist["val_accuracy"]
loss = model_hist["loss"]
val_loss = model_hist["val_loss"]

print("\n", model.summary(), "\n")
print(f"Best Accuracy: {max(accuracy):.4f}")
print(f"Best Validation Accuracy: {max(val_accuracy):.4f}")
print(f"Best Loss: {min(loss):.4f}")
print(f"Best Validation Loss: {min(val_loss):.4f}")
print()
print(f"Accuracy: {accuracy[-1]:.4f}")
print(f"Validation Accuracy: {val_accuracy[-1]:.4f}")
print(f"Loss: {loss[-1]:.4f}")
print(f"Validation Loss: {val_loss[-1]:.4f}")

input("Press enter to continue ...")

epochs = range(1, len(val_loss) + 1)
plt.plot(epochs, accuracy, "go--", label="acc")
plt.plot(epochs, val_accuracy, "g", label="val_acc")
plt.title("acc and val_acc")
plt.xlabel("epochs")

plt.legend()

plt.figure()

plt.plot(epochs, loss, "ro--", label="loss")
plt.plot(epochs, val_loss, "r", label="val_loss")
plt.title("loss and val_loss")
plt.xlabel("epochs")
plt.legend()
mplcursors.cursor()
plt.show()
