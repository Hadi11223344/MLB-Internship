
import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Flatten, Dense

# --------------------------------------------------
# 1. Configuration
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

GRAPH_DIR = os.path.join(BASE_DIR, "Graphs")
PREDICTION_DIR = os.path.join(BASE_DIR, "Predictions")

os.makedirs(GRAPH_DIR, exist_ok=True)
os.makedirs(PREDICTION_DIR, exist_ok=True)

np.random.seed(42)
tf.random.set_seed(42)

class_names = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot"
]

# --------------------------------------------------
# 2. Load the dataset
# --------------------------------------------------

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

print("Dataset loaded successfully!")
print("Training images:", x_train.shape)
print("Training labels:", y_train.shape)
print("Testing images:", x_test.shape)
print("Testing labels:", y_test.shape)

# --------------------------------------------------
# 3. Explore the dataset
# --------------------------------------------------

print("\nPixel range before normalization:")
print("Minimum:", x_train.min())
print("Maximum:", x_train.max())

print("\nUnique labels:", np.unique(y_train))

# Display sample images
plt.figure(figsize=(10, 5))

for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(x_train[i], cmap="gray")
    plt.title(class_names[y_train[i]])
    plt.axis("off")

plt.tight_layout()

sample_path = os.path.join(
    PREDICTION_DIR,
    "dataset_samples.png"
)

plt.savefig(sample_path, dpi=150)
plt.show()

# --------------------------------------------------
# 4. Normalize the pixel values
# --------------------------------------------------

x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

print("\nPixel range after normalization:")
print("Minimum:", x_train.min())
print("Maximum:", x_train.max())

# --------------------------------------------------
# 5. Build the ANN
# --------------------------------------------------

model = Sequential([
    Input(shape=(28, 28)),
    Flatten(),

    Dense(128, activation="relu"),
    Dense(64, activation="relu"),

    Dense(10, activation="softmax")
])

print("\nModel architecture:")
model.summary()

# --------------------------------------------------
# 6. Compile the model
# --------------------------------------------------

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# --------------------------------------------------
# 7. Train the model
# --------------------------------------------------

history = model.fit(
    x_train,
    y_train,
    epochs=10,
    batch_size=32,
    validation_split=0.1
)

# --------------------------------------------------
# 8. Evaluate the model
# --------------------------------------------------

test_loss, test_accuracy = model.evaluate(
    x_test,
    y_test,
    verbose=1
)

print("\nFinal test results:")
print("Test loss:", test_loss)
print("Test accuracy:", test_accuracy)

# --------------------------------------------------
# 9. Plot training and validation accuracy
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    history.history["accuracy"],
    label="Training Accuracy"
)

plt.plot(
    history.history["val_accuracy"],
    label="Validation Accuracy"
)

plt.title("Training and Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(True)

accuracy_graph_path = os.path.join(
    GRAPH_DIR,
    "accuracy_curve.png"
)

plt.savefig(accuracy_graph_path, dpi=150)
plt.show()

# --------------------------------------------------
# 10. Plot training and validation loss
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    history.history["loss"],
    label="Training Loss"
)

plt.plot(
    history.history["val_loss"],
    label="Validation Loss"
)

plt.title("Training and Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)

loss_graph_path = os.path.join(
    GRAPH_DIR,
    "loss_curve.png"
)

plt.savefig(loss_graph_path, dpi=150)
plt.show()

# --------------------------------------------------
# 11. Make predictions
# --------------------------------------------------

predictions = model.predict(x_test[:10])

predicted_labels = np.argmax(
    predictions,
    axis=1
)

# --------------------------------------------------
# 12. Display actual vs predicted
# --------------------------------------------------

plt.figure(figsize=(12, 6))

for i in range(10):
    plt.subplot(2, 5, i + 1)

    plt.imshow(x_test[i], cmap="gray")

    actual = class_names[y_test[i]]
    predicted = class_names[predicted_labels[i]]

    color = "green" if actual == predicted else "red"

    plt.title(
        f"Actual: {actual}\nPred: {predicted}",
        color=color
    )

    plt.axis("off")

plt.tight_layout()

prediction_path = os.path.join(
    PREDICTION_DIR,
    "sample_predictions.png"
)

plt.savefig(prediction_path, dpi=150)
plt.show()

# --------------------------------------------------
# 13. Print prediction results
# --------------------------------------------------

print("\nSample predictions:")

for i in range(10):
    actual = class_names[y_test[i]]
    predicted = class_names[predicted_labels[i]]

    print(
        f"Image {i + 1}: "
        f"Actual = {actual}, "
        f"Predicted = {predicted}"
    )

# --------------------------------------------------
# 14. Save the trained model
# --------------------------------------------------

model_path = os.path.join(
    BASE_DIR,
    "fashion_mnist_model.keras"
)

model.save(model_path)

print("\nModel saved successfully!")
print("Model path:", model_path)

print("\nDay-8 Fashion MNIST project completed!")
