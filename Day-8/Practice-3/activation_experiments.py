
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Dense

activations = ["relu", "sigmoid", "tanh"]

for activation in activations:

    print("\n" + "=" * 50)
    print(f"Experiment: {activation.upper()}")
    print("=" * 50)

    model = Sequential([
        Input(shape=(3,)),
        Dense(4, activation=activation),
        Dense(1, activation="sigmoid")
    ])

    model.summary()
