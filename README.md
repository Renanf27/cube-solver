# 🧩 Cube Solver

**A computer vision project to solve a physical Rubik's Cube using Python and OpenCV.**

Cube Solver is a personal project focused on exploring computer vision and image processing to build a system capable of recognizing a real Rubik's Cube through a camera and eventually calculating a solution.

The goal is to connect the physical world with software: capture the cube, recognize its colors, reconstruct its state, and visualize the solution digitally.

> 🚧 **Status: In Development** — Currently working on camera input and cube detection.

---

## 🎯 Project Goals

The project is being developed in stages:

- 📷 Capture video frames using a camera.
- 🔍 Detect the Rubik's Cube in the image.
- 🎨 Identify the colors of the cube's stickers.
- 🧩 Reconstruct the cube's state from the detected colors.
- 🧠 Calculate a valid solution for the cube.
- 🖥️ Display a 3D representation of the cube.
- 🔄 Animate the solution and synchronize it with the physical cube.

These are the project's goals, not all implemented features.

---

## 🛠️ Technologies

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)

**Currently exploring:**
- Computer Vision
- Image Processing
- Color Detection
- Object Detection

---

## ⚙️ Current Development

The first stage focuses on accessing the camera and experimenting with image processing to detect the cube in video frames.

The current development process involves:

1. Capturing frames from the camera with OpenCV.
2. Processing images to make detection easier.
3. Experimenting with geometric shapes and identifying the cube's position.
4. Improving detection stability across consecutive frames.

The next challenge is to reliably identify the cube's individual stickers and determine their colors.

---

## 🗺️ Roadmap

- [x] Start the Python project and configure OpenCV.
- [x] Implement initial camera capture.
- [ ] Improve cube detection and tracking.
- [ ] Detect the cube's nine stickers on a visible face.
- [ ] Recognize sticker colors under different lighting conditions.
- [ ] Capture and reconstruct all six faces.
- [ ] Validate the reconstructed cube state.
- [ ] Implement or integrate a Rubik's Cube solving algorithm.
- [ ] Create a 3D cube visualization.
- [ ] Animate the solution step by step.
- [ ] Explore real-time tracking while the cube is being rotated.

---

## 🚀 Getting Started

### Prerequisites

- Python 3
- A working camera
- pip

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd cube-solver
```

### 2. Create a virtual environment

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

On Linux or macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install OpenCV

```bash
pip install opencv-python
```

### 4. Run the project

Run the Python script responsible for camera capture and detection.

For example, if your main file is `main.py`:

```bash
python main.py
```

**Note:** The script name and camera configuration may need to be adjusted to match your local setup.

---

## 💡 Challenges and Learning

This project is also an opportunity to explore practical computer vision challenges, including:

- Lighting changes and color accuracy.
- Camera angle and perspective.
- Reliable detection across multiple frames.
- Distinguishing similar colors.
- Translating image information into a valid cube state.

The long-term objective is to build a complete pipeline, from camera input to a visualized solution.

---

## 👨‍💻 Author

**Renan França**

Computer Science student at IFCE, Brazil.

Interested in software development, artificial intelligence, computer vision, and building practical projects.

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Renanf27)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/renan-de-fran%C3%A7a/)

---

⭐ *Built step by step, exploring computer vision one frame at a time.*
