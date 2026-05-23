# Realtime Surveillance System

AI-powered realtime surveillance system using YOLOv8 and OpenCV for intelligent object detection and monitoring.

## Project Overview

This project is being developed as part of a Deep Learning Research Internship.

The goal of the system is to detect suspicious activities in realtime using Computer Vision and Deep Learning techniques.

Current implementation includes:

- Real-time object detection
- Webcam video processing
- Bounding box visualization
- Confidence score prediction
- YOLOv8 integration

Future planned features:

- Weapon detection
- Intrusion detection
- Face mask / anonymous person detection
- Alert system
- Dashboard integration
- Night surveillance support

---

# Tech Stack

- Python
- OpenCV
- YOLOv8
- Ultralytics

---

# Current Project Structure

```txt
realtime-surveillance/
│
├── backend/
│   └── detect.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <repo-link>
```

---

## 2. Move Into Project Directory

```bash
cd realtime-surveillance
```

---

## 3. Create Virtual Environment

### Windows

```bash
python -m venv surveillance_env
```

Activate virtual environment:

```bash
surveillance_env\Scripts\activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run The Project

```bash
python backend/detect.py
```

---

# Controls

| Key | Action |
|-----|--------|
| q | Quit application |

---

# Features

- Real-time webcam processing
- YOLOv8 object detection
- Automatic confidence scoring
- Bounding box rendering
- Lightweight and fast inference

---

# Sample Detection Objects

The system can currently detect:

- Person
- Mobile Phone
- Bottle
- Chair
- Laptop
- Car
- Bag
- And many more COCO dataset objects

---

# Future Improvements

- Suspicious activity detection
- Restricted area intrusion alerts
- Weapon detection model
- Telegram/SMS alerts
- Web dashboard
- Cloud deployment
- Multi-camera support

---

# Team

Deep Learning Research Internship Project

Developed for academic and research purposes.

---

# License

This project is intended for educational and research use.