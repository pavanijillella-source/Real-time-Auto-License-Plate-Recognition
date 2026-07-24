# 🚗 Real-Time Automatic License Plate Recognition & Computer Vision

A real-time **Automatic License Plate Recognition (ALPR) and Computer Vision system** developed using Python, OpenCV, TensorFlow/Keras, MobileNetV2, EasyOCR, PyTorch, and NumPy.

The project processes video frames in real time, performs deep learning-based image classification, detects and recognizes text from relevant regions of interest (ROIs), and displays the results through OpenCV-based visual overlays.

> **Note:** The current implementation is developed and tested in a local Python environment. Deployment on edge AI platforms such as NVIDIA Jetson Nano is considered a future enhancement.

---

## 📌 Executive Summary

This project implements an end-to-end real-time computer vision pipeline for analyzing video streams and recognizing license plate text.

The system reads video frames using **OpenCV** and processes them through two main branches:

* **Classification Branch:** Uses the pre-trained **MobileNetV2** architecture for image classification and visual analysis.
* **OCR Branch:** Uses **EasyOCR** to detect and recognize alphanumeric characters from relevant regions of interest.

The results are displayed in real time using OpenCV overlays, including classification predictions, text detections, and bounding boxes.

The project demonstrates the integration of **deep learning, computer vision, and OCR technologies** into a single real-time application.

---

## ✨ Features

* 🎥 Real-time video stream processing
* 🚘 Automatic License Plate Recognition (ALPR)
* 🧠 MobileNetV2-based image classification
* 🔤 Optical Character Recognition using EasyOCR
* 📦 Region of Interest (ROI) processing
* 🖼️ Real-time bounding box visualization
* 📝 Alphanumeric text recognition
* ⚡ OpenCV-based live output
* 🔧 Isolated Python virtual environment
* 🚀 Potential for future edge AI deployment

---

## 🛠️ Technologies Used

| Technology             | Purpose                                                    |
| ---------------------- | ---------------------------------------------------------- |
| **Python 3.11**        | Primary programming language                               |
| **TensorFlow / Keras** | Deep learning and model inference                          |
| **MobileNetV2**        | Lightweight image classification                           |
| **EasyOCR**            | Optical Character Recognition                              |
| **PyTorch**            | Deep learning backend used by EasyOCR                      |
| **OpenCV**             | Video processing and real-time visualization               |
| **NumPy**              | Array manipulation and numerical processing                |
| **ONNX**               | Model representation for supported model workflows         |
| **TensorRT**           | Included model artifacts for potential optimized inference |

---

## 🔄 How It Works

The system follows a real-time video processing pipeline:

1. **Video Input**
   OpenCV reads the input video stream frame by frame.

2. **Frame Processing**
   Each frame is processed and prepared for analysis.

3. **Image Classification**
   The MobileNetV2 model analyzes the input frames and generates classification predictions.

4. **Region of Interest Processing**
   Relevant areas of the frame are selected for further analysis.

5. **OCR Processing**
   EasyOCR detects and recognizes alphanumeric characters from the selected regions.

6. **Real-Time Visualization**
   Classification results, detected text, and bounding boxes are displayed directly on the video output using OpenCV.

### Processing Pipeline

```text
Video Input
    ↓
OpenCV Video Capture
    ↓
Frame-by-Frame Processing
    ↓
┌───────────────────────┐
│                       │
▼                       ▼
MobileNetV2          ROI Processing
Classification            ↓
    │                 EasyOCR
    │                    ↓
    │              Text Recognition
    │                    │
    └──────────┬─────────┘
               ↓
      OpenCV Visualization
               ↓
       Real-Time Output
```

---

## 🧠 Core Components

### 1. Video Stream Acquisition

OpenCV's `VideoCapture` functionality is used to read video frames sequentially.

Example:

```python
cap = cv2.VideoCapture("test.mp4")
```

Each frame is processed independently to enable continuous video analysis.

---

### 2. MobileNetV2 Classification

The project uses the pre-trained **MobileNetV2** architecture for lightweight image classification.

MobileNetV2 is well suited for applications that require efficient deep learning inference with relatively low computational requirements.

The classification workflow is:

```text
Input Frame
    ↓
Image Preprocessing
    ↓
MobileNetV2
    ↓
Classification Prediction
```

---

### 3. Optical Character Recognition

The OCR pipeline uses **EasyOCR** to detect and recognize text from relevant regions of the input frames.

The OCR workflow is:

```text
Input Frame
    ↓
Region of Interest
    ↓
EasyOCR
    ↓
Text Detection
    ↓
Recognized Characters
```

---

### 4. Real-Time Visualization

OpenCV is used to display the processed video output and overlay relevant information, including:

* Bounding boxes
* Classification labels
* Detected text
* OCR results

This allows users to visually observe the system's predictions while the video is being processed.

---

## 📂 Project Structure

```text
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
    │   └── Reference documentation for
    │       potential future deployment
    │
    └── images/
        └── Documentation graphics,
            screenshots, and sample results
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/pavanijillella-source/Real-time-Auto-License-Plate-Recognition.git
```

Navigate to the project directory:

```bash
cd Real-time-Auto-License-Plate-Recognition
```

### 2. Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv tf_env
```

Activate the environment on Windows:

```powershell
.\tf_env\Scripts\Activate.ps1
```

On Linux:

```bash
source tf_env/bin/activate
```

### 3. Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

> **Note:** Required dependencies and compatible versions may vary depending on the operating system, Python version, and hardware configuration.

---

## ▶️ Running the Project

Run the main application using:

```bash
python run_video.py
```

Make sure the input video path is correctly configured in the application.

For example:

```python
cap = cv2.VideoCapture("test.mp4")
```

The application will process the video and display the annotated output in real time.

---

## 📊 System Workflow

```text
Input Video
    ↓
OpenCV Frame Capture
    ↓
Frame Preprocessing
    ↓
┌─────────────────────┐
│                     │
▼                     ▼
MobileNetV2        ROI Processing
Classification          ↓
    │                EasyOCR
    │                  ↓
    │            Text Recognition
    │                  │
    └─────────┬────────┘
              ↓
     Real-Time Visualization
              ↓
       Annotated Output
```

---

## 🎯 Applications

The concepts demonstrated in this project can be applied to:

* 🚗 Automatic License Plate Recognition
* 🅿️ Smart parking systems
* 🚦 Traffic monitoring
* 🏢 Vehicle access control
* 🔐 Automated entry systems
* 📹 Video surveillance
* 🏙️ Smart city applications
* 🚘 Intelligent transportation systems

 

---

## 👩‍💻 Author

**Pavani Jillella**

