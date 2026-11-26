### Results

The Artificial Neural Network was trained for 10 epochs using the Fashion MNIST dataset.

| Metric | Result |
|---|---:|
| Final Training Accuracy | 91.50% |
| Final Validation Accuracy | 88.45% |
| Final Test Accuracy | 87.81% |
| Final Test Loss | 0.3613 |
| Trainable Parameters | 109,386 |

The model achieved 87.81% accuracy on the 10,000-image test dataset.

Training accuracy continued to improve throughout training, while validation accuracy began to plateau during the later epochs. Validation loss reached its lowest value at epoch 6 and fluctuated afterward, indicating mild overfitting during the later training stages.

All 10 displayed sample predictions were correctly classified, although this small sample is not representative of the overall test performance.

### Key Learnings

- Understood the fundamentals of Deep Learning and Artificial Neural Networks.
- Learned how perceptrons calculate weighted sums and apply activation functions.
- Explored ReLU, Sigmoid, Tanh and Softmax.
- Built and inspected neural network architectures using TensorFlow/Keras.
- Loaded, explored and normalized the Fashion MNIST dataset.
- Trained a multi-layer ANN for multiclass classification.
- Evaluated performance using training, validation and testing data.
- Visualized training and validation accuracy and loss.
- Generated predictions and compared them against actual labels.
- Saved the trained model in the Keras format.
