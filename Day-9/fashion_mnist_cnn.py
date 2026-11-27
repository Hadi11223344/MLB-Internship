from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report

tf.keras.utils.set_random_seed(42)
OUT=Path("outputs"); OUT.mkdir(exist_ok=True)
NAMES=["T-shirt/top","Trouser","Pullover","Dress","Coat","Sandal","Shirt","Sneaker","Bag","Ankle boot"]

(x_train,y_train),(x_test,y_test)=tf.keras.datasets.fashion_mnist.load_data()
x_train=x_train.astype("float32")/255.; x_test=x_test.astype("float32")/255.
x_train=x_train[...,np.newaxis]; x_test=x_test[...,np.newaxis]

fig,axes=plt.subplots(2,5,figsize=(10,5))
for ax,img,label in zip(axes.flat,x_train[:10],y_train[:10]):
 ax.imshow(img.squeeze(),cmap="gray"); ax.set_title(NAMES[label]); ax.axis("off")
fig.tight_layout(); fig.savefig(OUT/"dataset_samples.png",dpi=150); plt.close(fig)

model=tf.keras.Sequential([
 tf.keras.layers.Input(shape=(28,28,1)),
 tf.keras.layers.Conv2D(32,3,padding="same",activation="relu"),
 tf.keras.layers.MaxPooling2D(2),
 tf.keras.layers.Conv2D(64,3,padding="same",activation="relu"),
 tf.keras.layers.MaxPooling2D(2),
 tf.keras.layers.Flatten(),
 tf.keras.layers.Dense(128,activation="relu"),
 tf.keras.layers.Dense(10,activation="softmax")
],name="fashion_mnist_cnn")
model.summary()
model.compile(optimizer="adam",loss="sparse_categorical_crossentropy",metrics=["accuracy"])
history=model.fit(x_train,y_train,epochs=10,batch_size=32,validation_split=.1,shuffle=True)

for metric,ylabel,filename in [("accuracy","Accuracy","training_accuracy.png"),("loss","Loss","training_loss.png")]:
 plt.figure(figsize=(8,5)); plt.plot(history.history[metric],label="Training")
 plt.plot(history.history["val_"+metric],label="Validation"); plt.xlabel("Epoch"); plt.ylabel(ylabel)
 plt.title(ylabel+" across epochs"); plt.legend(); plt.grid(alpha=.3); plt.tight_layout()
 plt.savefig(OUT/filename,dpi=150); plt.close()

loss,acc=model.evaluate(x_test,y_test,verbose=0)
print(f"Test loss: {loss:.4f} | Test accuracy: {acc:.4f} ({acc*100:.2f}%)")
probs=model.predict(x_test,verbose=0); pred=probs.argmax(axis=1)
cm=confusion_matrix(y_test,pred)
disp=ConfusionMatrixDisplay(cm,display_labels=NAMES)
fig,ax=plt.subplots(figsize=(12,10)); disp.plot(ax=ax,xticks_rotation=45,colorbar=False)
ax.set_title("Fashion-MNIST CNN Confusion Matrix"); fig.tight_layout()
fig.savefig(OUT/"confusion_matrix.png",dpi=150); plt.close(fig)
print(classification_report(y_test,pred,target_names=NAMES))

fig,axes=plt.subplots(2,5,figsize=(12,6))
for ax,i in zip(axes.flat,range(10)):
 ax.imshow(x_test[i].squeeze(),cmap="gray"); ax.set_title(f"Pred: {NAMES[pred[i]]}\nTrue: {NAMES[y_test[i]]}"); ax.axis("off")
fig.tight_layout(); fig.savefig(OUT/"sample_predictions.png",dpi=150); plt.close(fig)

correct=np.where(pred==y_test)[0][:10]; wrong=np.where(pred!=y_test)[0][:10]
def show_indices(indices,file,title):
 if len(indices)==0: return
 fig,axes=plt.subplots(2,5,figsize=(12,6)); axes=np.array(axes).reshape(-1)
 for ax,i in zip(axes,indices):
  ax.imshow(x_test[i].squeeze(),cmap="gray")
  ax.set_title(f"Pred: {NAMES[pred[i]]}\nTrue: {NAMES[y_test[i]]}"); ax.axis("off")
 for ax in axes[len(indices):]: ax.axis("off")
 fig.suptitle(title); fig.tight_layout(); fig.savefig(OUT/file,dpi=150); plt.close(fig)
show_indices(correct,"correctly_classified.png","Correct predictions")
show_indices(wrong,"incorrectly_classified.png","Incorrect predictions")
model.save(OUT/"model.keras")
print("Saved artifacts to",OUT.resolve())
