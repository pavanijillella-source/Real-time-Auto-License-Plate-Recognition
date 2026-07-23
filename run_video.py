import cv2
import easyocr
import numpy as np
import tensorflow as np_tf
from tensorflow.keras.applications.mobilenet_v2 import (
    MobileNetV2,
    decode_predictions,
    preprocess_input,
)

# 1. Load Keras Deep Learning Model for Image Recognition
print("Loading Keras Deep Learning Model (MobileNetV2)...")
keras_model = MobileNetV2(weights=None)

# 2. Load EasyOCR Reader
print("Loading EasyOCR Model...")
reader = easyocr.Reader(["en"], gpu=False)

video_path = "test.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error opening video file")
    exit()

frame_count = 0
process_every_n_frames = 5
detected_text = ""
keras_label = "Scanning..."

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

    if frame_count % process_every_n_frames == 0:
        # --- Keras Processing (Deep Learning Image Recognition) ---
        # Resize frame to 224x224 required by MobileNetV2
        resized_frame = cv2.resize(frame, (224, 224))
        img_array = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

        # Run Keras inference
        predictions = keras_model.predict(img_array, verbose=0)
        decoded = decode_predictions(predictions, top=1)[0][0]
        keras_label = f"{decoded[1]} ({decoded[2]*100:.1f}%)"

        # --- OCR Processing (License Plate Text Extraction) ---
        results = reader.readtext(frame)
        for bbox, text, prob in results:
            if prob > 0.3 and len(text) > 3:
                detected_text = text
                (tl, tr, br, bl) = bbox
                top_left = (int(tl[0]), int(tl[1]))
                bottom_right = (int(br[0]), int(br[1]))

                cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)
                cv2.putText(
                    frame,
                    f"{text} ({prob:.2f})",
                    (top_left[0], top_left[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2,
                )

    # Display Keras Deep Learning & OCR output on screen
    cv2.putText(
        frame,
        f"Keras Class: {keras_label}",
        (20, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 0),
        2,
    )
    cv2.putText(
        frame,
        f"Plate Detected: {detected_text}",
        (20, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2,
    )

    cv2.imshow("Task 6 - License Plate Recognition", frame)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()