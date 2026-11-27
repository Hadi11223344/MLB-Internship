# Day 9 — CNN Fashion-MNIST Classifier

## Objective
Classify Fashion-MNIST grayscale clothing images into 10 categories using a CNN.

## Dataset
60,000 training and 10,000 test images; each image is 28×28 grayscale.
Class IDs: 0 T-shirt/top, 1 Trouser, 2 Pullover, 3 Dress, 4 Coat, 5 Sandal, 6 Shirt, 7 Sneaker, 8 Bag, 9 Ankle boot.

## Architecture
Input 28×28×1 → Conv2D(32, 3×3, SAME, ReLU) → MaxPool(2×2) → Conv2D(64, 3×3, SAME, ReLU) → MaxPool(2×2) → Flatten → Dense(128, ReLU) → Dense(10, Softmax).

## Preprocessing
Float32 conversion, pixel normalization to [0,1], channel dimension added. Validation split is 10% of training data; test set remains separate for final evaluation.

## Training
Adam; sparse categorical crossentropy; accuracy; 10 epochs; batch size 32.

## Run
```bash
python -m pip install -r requirements.txt
python cnn_practice.py
python fashion_mnist_cnn.py
```

The main script saves graphs, a confusion matrix, prediction grids, correct/incorrect samples and `model.keras` under `outputs/`.

## Analysis to complete after execution
- Test accuracy and loss:
- Best validation accuracy:
- Classes most frequently confused:
- Evidence of overfitting (if any):
- What could improve performance:
