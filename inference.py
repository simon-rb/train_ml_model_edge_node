import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers

MODEL_WEIGHTS_PATH = 'model.weights.h5'

def create_model():
    """Creates and returns a Keras Sequential model with identical structure to the training model."""
    model = keras.Sequential([
        layers.Input(shape=(1,)),
        layers.Dense(64, activation='relu'),
        layers.Dense(64, activation='relu'),
        layers.Dense(64, activation='relu'),
        layers.Dense(1)
    ])
    return model

def main():
    # Create and load the model
    model = create_model()
    model.load_weights(MODEL_WEIGHTS_PATH)
    print("Model weights loaded.")

    # Generate test data for inference
    x_test = np.linspace(-1, 1, 100)
    y_pred = model.predict(x_test)

    # Plot the predictions
    plt.figure(figsize=(12, 8))
    plt.plot(x_test, y_pred, color='red', label='Model Prediction', linewidth=2)
    plt.plot(x_test, x_test ** 3, color='green', label='True Function', linewidth=2, linestyle='--')
    plt.title('Neural Network Approximation of $f(x) = x^3$', fontsize=16)
    plt.xlabel('x', fontsize=14)
    plt.ylabel('f(x)', fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()