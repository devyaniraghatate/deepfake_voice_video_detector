import cv2
import sys
from deepface import DeepFace
model = load_model("my_model.keras")

# Check argument
if len(sys.argv) < 2:
    print("0")
    sys.exit()

video_path = sys.argv[1]

cap = cv2.VideoCapture(video_path)

fake_count = 0
total_frames = 0
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

    # 🔥 Skip frames for speed
    if frame_count % 5 != 0:
        continue

    try:
        # 👉 THIS is where DeepFace comes
        result = DeepFace.analyze(
            frame,
            actions=['emotion'],
            enforce_detection=False
        )

        # 👉 Simple fake logic (demo)
        if result:
            fake_count += 1

        total_frames += 1

    except:
        continue

cap.release()

# Avoid crash
if total_frames == 0:
    print("0")
    sys.exit()

fake_percentage = (fake_count / total_frames) * 100

print(f"{fake_percentage:.2f}")