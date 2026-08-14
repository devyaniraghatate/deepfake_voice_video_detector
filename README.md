# 🧠 Deepfake Voice & Video Detector

> **An integrated AI-powered system for detecting manipulated voice and video content using deep learning, audio analysis, and video-based processing.**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?logo=tensorflow)
![Keras](https://img.shields.io/badge/Keras-Deep%20Learning-red?logo=keras)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?logo=opencv)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-ff4b4b?logo=streamlit)
![Deepfake Detection](https://img.shields.io/badge/AI-Deepfake%20Detection-purple)

---

## 📌 Overview

This project implements an **integrated AI-based deepfake detection system** capable of analyzing both **voice/audio and video content**.

The system provides a unified Streamlit interface where users can upload media and analyze it for signs of manipulation.

### 🔄 Basic Workflow

```text
                 📁 Media Input
                      │
             ┌────────┴────────┐
             │                 │
          🎙️ Audio           🎥 Video
             │                 │
             ▼                 ▼
     Audio Preprocessing   Video Processing
             │                 │
             ▼                 ▼
      Voice Detection      Frame Analysis
             │                 │
             └────────┬────────┘
                      ▼
               🧠 AI Prediction
                      │
                      ▼
              📊 Real / Fake
                      │
                      ▼
             Confidence Score
```

---

## 🎯 Project Objectives

* Build an integrated deepfake detection system for audio and video.
* Detect manipulated or AI-generated voice content.
* Detect manipulated or AI-generated video content.
* Apply deep learning for automated media classification.
* Provide Real/Fake predictions with confidence scores.
* Develop an easy-to-use Streamlit interface.
* Understand the application of AI in digital media authenticity.

---

## 🧠 System Architecture

The project combines separate processing pipelines for voice and video detection within one application.

### 🎥 Video Detection Pipeline

```text
Uploaded Video
      ↓
Video Frame Extraction
      ↓
Frame Preprocessing
      ↓
Deep Learning Model
      ↓
Frame-Level Predictions
      ↓
Prediction Aggregation
      ↓
🎥 Real / Fake Video
```

### 🎙️ Voice Detection Pipeline

```text
Uploaded Audio
      ↓
Audio Preprocessing
      ↓
Audio Feature Extraction
      ↓
Deep Learning Model
      ↓
Prediction
      ↓
🎙️ Real / Fake Voice
```

---

## 📐 Input & Output

### 🎥 Video Input

The system accepts common video formats such as:

```text
MP4
AVI
MOV
```

Video content is processed into frames before being passed to the detection model.

### 🎙️ Audio Input

The system supports audio formats such as:

```text
WAV
MP3
```

Audio is processed and converted into features required by the trained voice detection model.

### 📊 Output

The system provides:

```text
Real / Fake Classification
+
Confidence Score
+
Prediction Visualization
```

---

## ⚙️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 Python | Programming language |
| 🧠 TensorFlow / Keras | Deep learning model development |
| 👁️ OpenCV | Video and image processing |
| 🔢 NumPy | Numerical operations |
| 📊 Matplotlib | Prediction visualization |
| 🌐 Streamlit | Interactive web application |
| 🎙️ Audio Processing | Voice feature extraction |
| 🤖 Machine Learning | Media classification |

---

## 📂 Project Structure

```text
deepfake_voice_video_detector/
│
├── 📄 app.py
├── 📄 train_model.py
├── 📄 video_model.py
├── 📄 audio_model.py
├── 📄 train_voice_model.py
│
├── 📄 my_model.keras
├── 📄 voice_model.h5
├── 📄 requirements.txt
├── 📄 README.md
│
├── 📁 dataset/
│   ├── 📁 real/
│   └── 📁 fake/
│
└── 📁 screenshots/
    ├── 🖼️ video-detection.png
    ├── 🖼️ audio-detection.png
    └── 🖼️ results.png
```

> The exact files may vary depending on the final implementation and training workflow.

---

## 🛠️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/deepfake_voice_video_detector.git
cd deepfake_voice_video_detector
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Required Libraries

Example `requirements.txt`:

```text
tensorflow
numpy
opencv-python
matplotlib
streamlit
librosa
scikit-learn
pandas
```

> Install only the packages required by your final implementation.

---

## 🧹 Data Preprocessing

Deepfake detection requires preprocessing before media can be passed to an AI model.

### 🎥 Video Preprocessing

Typical video preprocessing includes:

1. Reading the uploaded video.
2. Extracting representative frames.
3. Resizing frames to the model's required input dimensions.
4. Normalizing image values.
5. Passing processed frames to the trained model.
6. Aggregating frame-level predictions.

```text
Raw Video
    ↓
Frame Extraction
    ↓
Resize
    ↓
Normalize
    ↓
AI Model
```

### 🎙️ Audio Preprocessing

Typical audio preprocessing includes:

1. Loading the audio file.
2. Converting it into a suitable representation.
3. Extracting relevant audio features.
4. Preparing the feature vector.
5. Passing the features to the trained model.

```text
Raw Audio
    ↓
Audio Loading
    ↓
Feature Extraction
    ↓
Feature Processing
    ↓
AI Model
```

---

## 🧠 Deepfake Detection

Deepfake detection is treated as a **binary classification problem**.

The system aims to classify media into two categories:

```text
0 → Fake
1 → Real
```

The exact class mapping should match the labels used during model training.

### Prediction Concept

```text
Input Media
     ↓
Feature Extraction
     ↓
Trained Neural Network
     ↓
Prediction Probability
     ↓
┌───────────────┐
│ Real / Fake   │
│ Confidence %  │
└───────────────┘
```

---

## 🏋️ Model Training

The project uses TensorFlow/Keras-based models for deepfake classification.

The general training workflow is:

```text
Dataset
   ↓
Preprocessing
   ↓
Feature Extraction
   ↓
Training / Validation Split
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Saved Model
```

The trained models can then be loaded by the Streamlit application for inference.

Example:

```python
model = tf.keras.models.load_model("my_model.keras")
```

and:

```python
voice_model = tf.keras.models.load_model("voice_model.h5")
```

> Model architecture and preprocessing must match the training pipeline used to create the saved models.

---

## 🌐 Streamlit Application

The project provides an interactive web interface using **Streamlit**.

The interface contains two main detection modules:

### 🎥 Video Detection

Users can:

* Upload a video.
* Preview the uploaded video.
* Start AI analysis.
* Process video frames.
* View Real/Fake prediction.
* View confidence percentages.
* View prediction visualization.

### 🎙️ Audio Detection

Users can:

* Upload an audio file.
* Preview the audio.
* Start AI analysis.
* Process audio features.
* View Real/Fake prediction.
* View confidence percentages.

---

## ▶️ Running the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your default web browser.

### Application Workflow

```text
Launch Streamlit
       ↓
Select Detection Type
       ↓
Upload Audio / Video
       ↓
Click Analyze
       ↓
AI Processing
       ↓
Real / Fake Prediction
       ↓
Confidence Score
```

---

## 📊 Results

The system is designed to provide an easy-to-understand detection result.

Example:

```text
🎥 Video Prediction

Result: ⚠️ FAKE VIDEO
Fake Confidence: 92.40%
Real Confidence: 7.60%
```

or:

```text
🎙️ Audio Prediction

Result: ✅ REAL AUDIO
Real Confidence: 86.75%
Fake Confidence: 13.25%
```

> Replace these example values with your actual model results when documenting final performance.

---

## 🎥 Demo

Add your application demonstration here:

```markdown
![Deepfake Detector Demo](screenshots/demo.gif)
```

Or add a video demonstration:

```markdown
[![Deepfake Detection Demo](screenshots/thumbnail.png)](YOUR-YOUTUBE-LINK)
```

---

## 📸 Screenshots

### 🏠 Application Interface

![Application Interface](screenshots/home.png)

### 🎥 Video Detection

![Video Detection](screenshots/video-detection.png)

### 🎙️ Audio Detection

![Audio Detection](screenshots/audio-detection.png)

### 📊 Detection Result

![Detection Result](screenshots/results.png)

> Replace the placeholder paths with your actual screenshots.

---

## 💡 Key Learning Outcomes

Through this project, I gained practical experience in:

* Deepfake detection
* Deep learning
* Binary classification
* Computer vision
* Video frame processing
* Audio processing
* Feature extraction
* TensorFlow/Keras
* OpenCV
* Model training and evaluation
* Streamlit application development
* Real-time inference concepts
* Integrating multiple AI models into a single application

---

## 🚀 Future Improvements

Possible future enhancements include:

* 🔹 Improve model accuracy using larger and more diverse datasets.
* 🔹 Use advanced transfer-learning architectures.
* 🔹 Implement more robust audio feature extraction.
* 🔹 Perform frame-level temporal video analysis.
* 🔹 Build a unified audio-video fusion model.
* 🔹 Add live webcam deepfake detection.
* 🔹 Add real-time microphone voice detection.
* 🔹 Optimize models for faster inference.
* 🔹 Deploy the system as a cloud-based application.
* 🔹 Add explainable AI techniques to highlight suspicious regions or audio segments.

---

## 📚 References

This project builds upon concepts from deep learning, computer vision, audio processing, and synthetic-media detection research.

Relevant areas include:

* Deep learning-based image and video classification
* Audio feature extraction and classification
* CNN-based computer vision
* Synthetic media and deepfake detection
* Multimodal AI

---

## ⭐ Acknowledgements

Special thanks to the open-source Python, TensorFlow, Keras, OpenCV, and Streamlit communities for providing the tools and frameworks used in this project.

---

## 📜 License

This project is intended for **educational, research, and learning purposes**.

---

<div align="center">

### 🧠 Detect the Fake. Verify the Media. 🔍

**Built with Python + TensorFlow + Keras + OpenCV + Streamlit**

⭐ If you found this project interesting, consider giving the repository a star!

</div>
