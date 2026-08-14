import streamlit as st
import time
import random
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Deepfake Detector AI", page_icon="🧠", layout="wide")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #141E30, #243B55);
    color: white;
}
.big-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
}
.stButton>button {
    width: 80%;
    border-radius: 10px;
    height: 2em;
    font-size: 16px;
    background-color: #ff4b4b;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="big-title">🧠 Deepfake Detection System</div>', unsafe_allow_html=True)
st.markdown("### 🔍 Detect Fake Audio & Video using AI")

# ---------------- TABS ----------------
tab1, tab2 = st.tabs(["🎥 Video Detection", "🎙️ Audio Detection"])

# ---------------- PROGRESS FUNCTION ----------------
def fake_progress():
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)

# ================= VIDEO TAB =================
with tab1:
    st.markdown("## 🎥 Upload Video")

    video_file = st.file_uploader("Upload Video", type=["mp4", "avi", "mov"], key="video")

    if video_file:
        st.video(video_file)

        if st.button("🔍 Analyze Video"):
            st.info("Analyzing video...")

            fake_progress()

            # 🔥 Replace with your real model
            final_score = random.uniform(0, 1)

            fake_percent = final_score * 100
            real_percent = 100 - fake_percent

            st.markdown("### 📊 Result")

            if fake_percent > 50:
                st.error(f"⚠️ FAKE VIDEO ({fake_percent:.2f}%)")
            else:
                st.success(f"✅ REAL VIDEO ({real_percent:.2f}%)")

            st.progress(int(fake_percent))

            # -------- GRAPH --------
            st.markdown("### 📈 Confidence Graph")

            labels = ["Real", "Fake"]
            values = [real_percent, fake_percent]

            fig, ax = plt.subplots()
            ax.bar(labels, values)

            ax.set_ylabel("Confidence (%)")
            ax.set_title("Video Prediction Confidence")

            st.pyplot(fig)

            st.write(f"✅ Real: {real_percent:.2f}%")
            st.write(f"⚠️ Fake: {fake_percent:.2f}%")

# ================= AUDIO TAB =================
with tab2:
    st.markdown("## 🎙️ Upload Audio")

    audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3"], key="audio")

    if audio_file:
        st.audio(audio_file)

        if st.button("🔍 Analyze Audio"):
            st.info("Analyzing audio...")

            fake_progress()

            # 🔥 Replace with your real model
            final_score = random.uniform(0, 1)

            fake_percent = final_score * 100
            real_percent = 100 - fake_percent

            st.markdown("### 📊 Result")

            if fake_percent > 50:
                st.error(f"⚠️ FAKE AUDIO ({fake_percent:.2f}%)")
            else:
                st.success(f"✅ REAL AUDIO ({real_percent:.2f}%)")

            st.progress(int(fake_percent))

            # -------- GRAPH --------
            st.markdown("### 📈 Confidence Graph")

            labels = ["Real", "Fake"]
            values = [real_percent, fake_percent]

            fig, ax = plt.subplots()
            ax.bar(labels, values)

            ax.set_ylabel("Confidence (%)")
            ax.set_title("Audio Prediction Confidence")

            st.pyplot(fig)

            st.write(f"✅ Real: {real_percent:.2f}%")
            st.write(f"⚠️ Fake: {fake_percent:.2f}%")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("💡 Built with AI | Deepfake Detection Project")