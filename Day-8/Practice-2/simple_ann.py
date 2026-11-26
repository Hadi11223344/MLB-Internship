
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Dense

# Build the neural network
model = Sequential([
    Input(shape=(3,)),
    Dense(2, activation="relu"),
    Dense(1, activation="sigmoid")
])

# Display the architecture
model.summary()

# Configure the model for training
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

print("\nModel successfully created and compiled!")
