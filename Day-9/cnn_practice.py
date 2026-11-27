import tensorflow as tf
model = tf.keras.Sequential([
 tf.keras.layers.Input(shape=(28,28,1)),
 tf.keras.layers.Conv2D(32,3,padding="same",activation="relu"),
 tf.keras.layers.MaxPooling2D(2),
 tf.keras.layers.Conv2D(64,3,padding="same",activation="relu"),
 tf.keras.layers.MaxPooling2D(2),
 tf.keras.layers.Flatten(),
 tf.keras.layers.Dense(128,activation="relu"),
 tf.keras.layers.Dense(10,activation="softmax")
])
model.summary()
x=tf.random.uniform((1,28,28,1))
for layer in model.layers:
 x=layer(x); print(layer.name, x.shape)
