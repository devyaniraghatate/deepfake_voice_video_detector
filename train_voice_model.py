# ==============================
# 1. IMPORT LIBRARIES
# ==============================
import os
import numpy as np
import librosa
import soundfile as sf

from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import Input

# ==============================
# 2. CONVERT TO WAV (IMPORTANT)
# ==============================
def convert_to_wav(input_file):
    try:
        audio, sr = librosa.load(input_file, sr=None)
        output_file = input_file + ".wav"
        sf.write(output_file, audio, sr)
        return output_file
    except Exception as e:
        print("Conversion failed:", input_file)
        return None

# ==============================
# 3. FEATURE EXTRACTION
# ==============================
def extract_features(file_path):
    try:
        audio, sample_rate = librosa.load(file_path, sr=None)
        mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
        return np.mean(mfccs.T, axis=0)
    except Exception as e:
        print("Error processing:", file_path)
        return None

# ==============================
# 4. LOAD DATASET
# ==============================
X = []
y = []

dataset_path = "dataset"

for label, category in enumerate(["real", "fake"]):
    folder_path = os.path.join(dataset_path, category)

    if not os.path.isdir(folder_path):
        print(f"❌ Folder not found: {folder_path}")
        continue

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        # Convert if not WAV
        if not file_path.endswith(".wav"):
            new_file = convert_to_wav(file_path)
            if new_file:
                file_path = new_file
            else:
                continue

        features = extract_features(file_path)

        if features is not None:
            X.append(features)
            y.append(label)

X = np.array(X)
y = np.array(y)

print("✅ Data loaded:", X.shape)

# ==============================
# 5. CHECK DATA
# ==============================
if len(X) < 5:
    print("⚠️ Not enough data. Add more audio files.")
    exit()

# ==============================
# 6. TRAIN TEST SPLIT
# ==============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ==============================
# 7. BUILD MODEL
# ==============================
model = Sequential([
    Input(shape=(40,)),
    Dense(256, activation='relu'),
    Dense(128, activation='relu'),
    Dense(1, activation='sigmoid')
])

# ==============================
# 8. COMPILE MODEL
# ==============================
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# ==============================
# 9. TRAIN MODEL
# ==============================
model.fit(
    X_train,
    y_train,
    epochs=20,
    batch_size=16
)

# ==============================
# 10. EVALUATE MODEL
# ==============================
loss, acc = model.evaluate(X_test, y_test)
print(f"🎯 Accuracy: {acc * 100:.2f}%")

# ==============================
# 11. SAVE MODEL
# ==============================
model.save("voice_model.h5")
print("💾 Model saved as voice_model.h5")