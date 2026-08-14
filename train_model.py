from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

model = Sequential([
    Dense(10, input_shape=(5,), activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy')

# fake training data
X = np.random.rand(100, 5)
y = np.random.randint(0, 2, 100)

model.fit(X, y, epochs=5)

model.save("my_model.keras")

print("Model created successfully!")