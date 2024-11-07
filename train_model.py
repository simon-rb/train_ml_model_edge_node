import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Constants
EPOCHS = 500
NOISE_STD_DEV = 0.05
MODEL_WEIGHTS_PATH = 'model.weights.h5'

def generate_training_data():
    """Generates training data with noise for the function f(x) = x^3."""
    x = np.linspace(-1, 1, 100)
    y_true = x ** 3
    noise = np.random.normal(0, NOISE_STD_DEV, x.shape)
    y = y_true + noise
    return x, y

def create_model():
    """Creates and returns a Keras Sequential model."""
    model = keras.Sequential([
        layers.Input(shape=(1,)),
        layers.Dense(64, activation='relu'),
        layers.Dense(64, activation='relu'),
        layers.Dense(64, activation='relu'),
        layers.Dense(1)
    ])
    return model

def main():
    # Generate training data
    x_train, y_train = generate_training_data()

    # Create and compile the model
    model = create_model()
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Train the model
    history = model.fit(x_train, y_train, epochs=EPOCHS, verbose=1)

    # Save model weights
    model.save_weights(MODEL_WEIGHTS_PATH)
    print(f"Training complete. Weights saved to '{MODEL_WEIGHTS_PATH}'.")

if __name__ == "__main__":
    main()