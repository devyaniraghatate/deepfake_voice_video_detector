🧠 Deepfake Voice & Video Detector

An AI-powered real-time deepfake detection system that integrates voice and video analysis using deep learning and multimodal processing to identify manipulated media and deliver Real/Fake predictions with confidence scores.

🚀 Overview

Deepfakes are AI-generated or manipulated media that can make fake audio and videos appear authentic. This project aims to provide an integrated solution for detecting both:

🎙️ Deepfake Voice / Audio

🎥 Deepfake Video

The system provides a simple Streamlit-based interface where users can upload media and analyze it using trained AI models.

✨ Features

🎥 Video deepfake detection

🎙️ Voice/audio deepfake detection

🧠 Deep learning-based analysis

⚡ Real-time prediction interface

📊 Real/Fake confidence scores

📈 Prediction visualization

🖥️ Interactive Streamlit web interface

🔗 Integrated voice and video detection in one system

🛠️ Technologies Used

Python

TensorFlow / Keras

OpenCV

NumPy

Matplotlib

Streamlit

Audio processing / feature extraction

Deep Learning

📂 Project Structure

deepfake_voice_video_detector/
│
├── app.py
├── train_model.py
├── video_model.py
├── audio_model.py
├── train_voice_model.py
├── my_model.keras
├── voice_model.h5
├── dataset/
│   ├── real/
│   └── fake/
│
├── requirements.txt
└── README.md

File names may vary depending on the final version of the project.

⚙️ Installation

1. Clone the repository

git clone https://github.com/your-username/deepfake_voice_video_detector.git
cd deepfake_voice_video_detector

2. Create a virtual environment

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

▶️ Run the Application

Start the Streamlit application:

streamlit run app.py

The application will open in your browser.

🔄 System Workflow

        ┌─────────────────────┐
        │    User Uploads     │
        │   Audio / Video     │
        └──────────┬──────────┘
                   │
          ┌────────┴────────┐
          │                 │
     🎙️ Audio          🎥 Video
          │                 │
          ▼                 ▼
   Audio Processing    Frame Processing
          │                 │
          ▼                 ▼
    AI Voice Model     AI Video Model
          │                 │
          └────────┬────────┘
                   ▼
          Real / Fake Prediction
                   │
                   ▼
          Confidence Score

📊 Output

The system provides:

Real / Fake classification

Confidence percentage

Prediction visualization

Analysis results for uploaded media

🎯 Project Objective

The main objective of this project is to develop an integrated AI-based system capable of detecting manipulated voice and video content efficiently. The project demonstrates how deep learning and multimodal analysis can be applied to address the growing challenge of synthetic and manipulated digital media.

🔮 Future Enhancements

Real-time webcam deepfake detection

Live microphone voice analysis

Improved CNN/transfer-learning architectures

Larger and more diverse datasets

Frame-level video analysis

Advanced audio feature extraction

Combined audio-video fusion model

Deployment as a cloud-based application

⚠️ Disclaimer

This project is developed for educational, research, and demonstration purposes. Detection results should not be treated as absolute proof of authenticity.

👩‍💻 Author

Devyani Raghatate

⭐ If you find this project useful, consider giving the repository a star!
