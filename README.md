🚗 Real-Time Automatic License Plate Recognition & Computer Vision
📌 Executive Summary

This project implements a Real-Time Automatic License Plate Recognition (ALPR) and Computer Vision system using Python, OpenCV, TensorFlow/Keras, MobileNetV2, EasyOCR, PyTorch, and NumPy.

The system processes a video stream frame by frame using OpenCV. It combines a deep learning-based image classification pipeline with an Optical Character Recognition (OCR) pipeline to analyze video frames and detect and recognize alphanumeric text from relevant regions of interest (ROIs).

The results are visualized in real time by overlaying classification predictions, bounding boxes, and recognized text directly onto the video frames.

The project is currently developed and tested in a local Python environment. Future work can include optimizing the system for deployment on edge AI platforms such as the NVIDIA Jetson Nano.

✨ Key Features
🎥 Real-time video processing
🚘 Automatic License Plate Recognition (ALPR)
🔤 Optical Character Recognition using EasyOCR
🧠 Image classification using MobileNetV2
📦 Region of Interest (ROI) processing
🖼️ Real-time bounding box visualization
📝 Alphanumeric text recognition
⚡ OpenCV-based live output
🔧 Isolated Python virtual environment
🚀 Potential for future edge-device deployment
🛠️ Technologies Used
Technology	Purpose
Python 3.11	Primary programming language
TensorFlow / Keras	Deep learning and MobileNetV2 inference
MobileNetV2	Lightweight image classification
EasyOCR	Optical Character Recognition
PyTorch	Deep learning backend for EasyOCR
OpenCV	Video processing and visualization
NumPy	Array manipulation and numerical operations
ONNX	Model representation for supported model workflows
TensorRT Engine Files	Included model artifacts for potential optimized inference
🔄 Core Development Workflow

The system processes the input video through a multi-stage pipeline.

                 Video Input
                     │
                     ▼
             OpenCV VideoCapture
                     │
                     ▼
              Frame-by-Frame
                Processing
                     │
            ┌────────┴────────┐
            │                 │
            ▼                 ▼
      Classification       ROI / Text
          Branch            Processing
            │                 │
            ▼                 ▼
       MobileNetV2          EasyOCR
            │                 │
            ▼                 ▼
      Classification      Text Detection
        Prediction              │
            │                   ▼
            │             Recognized Text
            │                   │
            └────────┬──────────┘
                     │
                     ▼
            OpenCV Visualization
                     │
                     ▼
            Real-Time Annotated
                 Video Output
1. Isolated Virtual Environment

A dedicated Python virtual environment named tf_env was created to manage project dependencies independently from the system Python installation.

This environment helps avoid dependency conflicts between libraries such as:

TensorFlow
Keras
PyTorch
EasyOCR
OpenCV
NumPy

The tf_env/ directory is excluded from Git version control using .gitignore.

2. Video Stream Acquisition

OpenCV's VideoCapture functionality is used to read the input video frame by frame.

The system processes each frame sequentially, allowing the computer vision and OCR pipeline to operate continuously.

Example:

cap = cv2.VideoCapture("test.mp4")
3. Classification Pipeline

The video frames are preprocessed and passed through the MobileNetV2 architecture.

MobileNetV2 is a lightweight convolutional neural network designed to provide efficient image classification while maintaining relatively low computational requirements.

The classification workflow is:

Input Frame
     │
     ▼
Image Preprocessing
     │
     ▼
MobileNetV2
     │
     ▼
Classification Prediction
4. OCR Pipeline

Relevant regions of the video frames are processed using EasyOCR.

The OCR engine detects text regions and extracts alphanumeric characters from the selected regions.

The workflow is:

Input Frame
     │
     ▼
Region of Interest
     │
     ▼
EasyOCR
     │
     ▼
Text Detection
     │
     ▼
Recognized Characters
5. Real-Time Visualization

The processed results are displayed using OpenCV.

The application can overlay information such as:

Bounding boxes
Classification labels
Detected text
OCR results

This provides a real-time visual representation of the computer vision pipeline.

📂 Project Structure
Real-time-Auto-License-Plate-Recognition/
│
├── run_video.py
│   └── Main execution script integrating
│       OpenCV, TensorFlow/Keras,
│       MobileNetV2, and EasyOCR
│
├── .gitignore
│   └── Excludes virtual environments,
│       large video files, and generated files
│
├── README.md
│   └── Project documentation
│
├── networks/
│   │
│   ├── az_ocr/
│   │   └── OCR-related model files,
│   │       ONNX models, and TensorRT engines
│   │
│   └── az_plate/
│       └── License plate detection
│           model files and labels
│
└── doc/
    │
    ├── dataset.md
    │   └── Dataset information
    │
    ├── plate-detect.md
    │   └── License plate detection documentation
    │
    ├── jetson-setup.md
    │   └── Future/reference deployment documentation
    │
    └── images/
        └── Documentation graphics,
            screenshots, and sample results
⚙️ Installation
1. Clone the Repository
git clone https://github.com/pavanijillella-source/Real-time-Auto-License-Plate-Recognition.git

Navigate to the project:

cd Real-time-Auto-License-Plate-Recognition
2. Create a Virtual Environment

Create a virtual environment:

python -m venv tf_env

Activate it on Windows:

.\tf_env\Scripts\Activate.ps1

On Linux:

source tf_env/bin/activate
3. Install Dependencies
pip install -r requirements.txt
▶️ Running the Project

Run the main application:

python run_video.py

Make sure the input video path is correctly configured in the application.

For example:

cap = cv2.VideoCapture("test.mp4")

The application will process the video and display the real-time annotated output.

📊 System Workflow
Video Input
     │
     ▼
OpenCV Frame Capture
     │
     ▼
Frame Preprocessing
     │
     ├───────────────┐
     │               │
     ▼               ▼
MobileNetV2       ROI Processing
     │               │
     ▼               ▼
Classification     EasyOCR
Prediction           │
                     ▼
               Text Recognition
     │               │
     └───────┬───────┘
             │
             ▼
    Real-Time Visualization
             │
             ▼
       Annotated Output
🎯 Applications

The concepts demonstrated in this project can be applied to:

🚗 Automatic License Plate Recognition
🅿️ Smart parking systems
🚦 Traffic monitoring
🏢 Vehicle access control
🔐 Automated entry systems
📹 Video surveillance
🏙️ Smart city applications
🚘 Intelligent transportation systems

This would enable the system to operate as a standalone AI-powered edge vision solution.

👩‍💻 Author

Pavani Jillella
