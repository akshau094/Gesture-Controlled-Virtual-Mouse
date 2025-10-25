<div align="center">

# 🖐️ Gesture Controlled Virtual Mouse

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=28&pause=1000&color=00D9FF&center=true&vCenter=true&random=false&width=700&lines=Control+Your+PC+With+Hand+Gestures+%F0%9F%96%90%EF%B8%8F;AI+Powered+Virtual+Mouse+%F0%9F%A4%96;No+Physical+Mouse+Needed+%E2%9C%A8;Computer+Vision+%7C+Machine+Learning+%F0%9F%9A%80" alt="Typing SVG" />

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/OpenCV-4.0+-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV"/>
  <img src="https://img.shields.io/badge/MediaPipe-Latest-FF6F00?style=for-the-badge&logo=google&logoColor=white" alt="MediaPipe"/>
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" alt="Status"/>
</p>

<p align="center">
  <strong>Transform your webcam into a touchless mouse controller using AI-powered hand gesture recognition!</strong>
</p>

</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Demo](#-demo)
- [Key Features](#-key-features)
- [Gesture Controls](#-gesture-controls)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Configuration](#-configuration)
- [Troubleshooting](#-troubleshooting)
- [Performance Tips](#-performance-tips)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🎯 Overview

**Gesture Controlled Virtual Mouse** is an innovative AI-powered application that lets you control your computer mouse using simple hand gestures captured through your webcam. No physical mouse needed! Perfect for presentations, touchless computing, accessibility needs, or just having fun with cutting-edge computer vision technology.

Built with Python, OpenCV, and Google's MediaPipe, this project leverages advanced hand tracking algorithms to provide smooth, accurate, and responsive cursor control.

### 🌟 Why This Project?

- **🚫 Touchless Computing**: Perfect for hygiene-conscious environments
- **♿ Accessibility**: Helps users with limited mobility
- **🎤 Presentations**: Control slides from a distance
- **🤖 AI Learning**: Great for learning computer vision and gesture recognition
- **🎮 Fun Factor**: Impress your friends with futuristic tech!

---

## 🎬 Demo

<div align="center">

### See It In Action!

| Cursor Movement | Click & Drag | Scroll Mode |
|:---:|:---:|:---:|
| 👆 Point & Move | 🤏 Pinch Gestures | ✌️ Two Fingers |

</div>

> **Note**: Add your demo GIF or video here to showcase the project!

---

## ✨ Key Features

<table>
<tr>
<td width="50%">

### 🎯 **Precision Control**
- ✅ Smooth cursor movement with adaptive smoothing
- ✅ Dead-zone filtering to eliminate jitter
- ✅ Dynamic sensitivity adjustment
- ✅ Reduced movement area for better control

</td>
<td width="50%">

### 🖱️ **Full Mouse Functionality**
- ✅ Left click (thumb-index pinch)
- ✅ Right click (thumb-middle pinch)
- ✅ Double click (quick double pinch)
- ✅ Click and drag (hold pinch)

</td>
</tr>
<tr>
<td width="50%">

### 📜 **Advanced Features**
- ✅ Vertical scrolling mode
- ✅ Gesture-based mode switching
- ✅ Real-time visual feedback
- ✅ Configurable thresholds

</td>
<td width="50%">

### ⚡ **Performance**
- ✅ Real-time hand tracking (30+ FPS)
- ✅ Low latency response
- ✅ Optimized for smooth operation
- ✅ Multi-hand detection support

</td>
</tr>
</table>

---

## 🖐️ Gesture Controls

<div align="center">

### Master These Simple Gestures!

</div>

| Gesture | Action | Description |
|:---:|:---:|:---|
| 👆 **Index Finger Up** | **Move Cursor** | Point with your index finger to move the cursor around |
| 🤏 **Thumb + Index Pinch** | **Left Click** | Bring thumb and index finger together quickly |
| 🤏🤏 **Double Pinch** | **Double Click** | Two quick thumb-index pinches within 0.35 seconds |
| 🤏⏱️ **Hold Pinch (0.45s)** | **Click & Drag** | Hold the thumb-index pinch for 0.45 seconds to drag |
| 🤌 **Thumb + Middle Pinch** | **Right Click** | Bring thumb and middle finger together |
| ✌️ **Index + Middle Up** | **Scroll Mode** | Raise both index and middle fingers, move up/down to scroll |

### 📊 Visual Guide

```
        Cursor Movement              Left Click              Right Click
              👆                        🤏                       🤌
           ┌──────┐                 ┌──────┐                ┌──────┐
           │Index │                 │Thumb │                │Thumb │
           │  Up  │                 │  +   │                │  +   │
           └──────┘                 │Index │                │Middle│
                                    └──────┘                └──────┘

        Scroll Mode              Double Click             Click & Drag
            ✌️                        🤏🤏                     🤏⏱️
         ┌──────┐                 ┌──────┐                ┌──────┐
         │Index │                 │Quick │                │ Hold │
         │  +   │                 │Double│                │0.45s │
         │Middle│                 │Pinch │                │Pinch │
         └──────┘                 └──────┘                └──────┘
```

---

## 🔥 Tech Stack

<div align="center">

### Built With Cutting-Edge Technologies

<table>
<tr>
<td align="center" width="140">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="65" height="65" alt="Python" />
<br><strong>Python 3.8+</strong>
<br><sub>Core Language</sub>
</td>
<td align="center" width="140">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/opencv/opencv-original.svg" width="65" height="65" alt="OpenCV" />
<br><strong>OpenCV</strong>
<br><sub>Computer Vision</sub>
</td>
<td align="center" width="140">
<img src="https://mediapipe.dev/images/mediapipe_small.png" width="65" height="65" alt="MediaPipe" />
<br><strong>MediaPipe</strong>
<br><sub>Hand Tracking</sub>
</td>
<td align="center" width="140">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" width="65" height="65" alt="NumPy" />
<br><strong>NumPy</strong>
<br><sub>Numerical Computing</sub>
</td>
</tr>
</table>

### 📦 Dependencies

```python
opencv-python    # Computer vision and image processing
mediapipe        # Google's hand tracking solution
numpy           # Mathematical operations and arrays
pyautogui       # Mouse and keyboard control automation
```

</div>

---

## 🚀 Installation

### 📋 Prerequisites

Before you begin, ensure you have:

- **Python 3.8 or higher** installed ([Download Python](https://www.python.org/downloads/))
- **Working webcam** (built-in or external)
- **pip** package manager (comes with Python)

### ⚡ Quick Install

#### **Option 1: Clone from GitHub**

```bash
# 1️⃣ Clone the repository
git clone https://github.com/yourusername/Gesture-Controlled-Virtual-Mouse.git

# 2️⃣ Navigate to project directory
cd Gesture-Controlled-Virtual-Mouse

# 3️⃣ Install required packages
pip install -r requirements.txt

# 4️⃣ Run the application
python virtual_mouse.py
```

#### **Option 2: Manual Installation**

```bash
# Create a new directory
mkdir gesture-mouse
cd gesture-mouse

# Install dependencies one by one
pip install opencv-python
pip install mediapipe
pip install numpy
pip install pyautogui

# Download the script and run
python virtual_mouse.py
```

### 📄 requirements.txt

Create a `requirements.txt` file with:

```txt
opencv-python>=4.5.0
mediapipe>=0.10.0
numpy>=1.19.0
pyautogui>=0.9.50
```

---

## 💻 Usage

### 🎮 Basic Usage

1. **Launch the Application**
   ```bash
   python virtual_mouse.py
   ```

2. **Position Your Hand**
   - Sit 1-2 feet from your webcam
   - Ensure good lighting
   - Keep your hand within the purple boundary box

3. **Start Gesturing**
   - Use index finger to move cursor
   - Perform pinch gestures for clicks
   - Raise two fingers for scroll mode

4. **Exit**
   - Press **`Q`** key to quit

### 🎯 Pro Tips

- **Lighting**: Bright, even lighting works best
- **Background**: Plain backgrounds improve tracking
- **Distance**: 1.5-2 feet from camera is optimal
- **Hand Size**: Palm should fill about 1/4 of the frame
- **Stability**: Rest your elbow on a surface for steadier control

---

## 🧠 How It Works

### Architecture Overview

```
┌─────────────┐      ┌──────────────┐      ┌─────────────┐
│   Webcam    │ ───> │   OpenCV     │ ───> │  MediaPipe  │
│   Capture   │      │  Processing  │      │ Hand Track  │
└─────────────┘      └──────────────┘      └─────────────┘
                                                    │
                                                    ▼
┌─────────────┐      ┌──────────────┐      ┌─────────────┐
│  PyAutoGUI  │ <─── │   Gesture    │ <─── │  Landmark   │
│   Control   │      │  Detection   │      │  Extraction │
└─────────────┘      └──────────────┘      └─────────────┘
```

### 🔍 Technical Deep Dive

#### 1. **Hand Detection & Tracking**
- MediaPipe's ML model detects 21 hand landmarks in real-time
- Tracks fingertips, joints, and palm positions
- Works with various hand sizes and skin tones

#### 2. **Gesture Recognition**
- **Finger State Detection**: Determines which fingers are up/down
- **Distance Calculation**: Measures distances between landmarks
- **Dynamic Thresholds**: Adapts to individual hand sizes

#### 3. **Cursor Control**
- **Coordinate Mapping**: Converts hand position to screen coordinates
- **Smoothing Algorithm**: Reduces jitter with adaptive smoothing
  ```python
  # Dynamic smoothing based on movement speed
  smooth_factor = base_factor + (max_factor - base_factor) * scale
  ```
- **Dead Zone**: Filters out micro-movements (< 2 pixels)

#### 4. **Click Detection**
- **Pinch Detection**: Calculates thumb-finger distances
- **Debouncing**: Prevents multiple rapid clicks
- **Hold Detection**: Distinguishes between click and drag

#### 5. **Scroll Mode**
- **Activation**: Two fingers raised together
- **Sensitivity**: Configurable scroll speed
- **Vertical Tracking**: Uses Y-axis hand movement

### 🎛️ Key Parameters

| Parameter | Value | Purpose |
|-----------|-------|---------|
| `base_smooth_factor` | 4.0 | Base cursor smoothing |
| `max_smooth_factor` | 6.5 | Maximum smoothing for small movements |
| `deadzone_px` | 2 | Minimum movement threshold |
| `frame_reduction` | 100 | Movement boundary margin |
| `drag_hold_seconds` | 0.45 | Hold time to activate drag |
| `double_click_window` | 0.35 | Max time between double-click pinches |
| `scroll_sensitivity` | 1.4 | Scroll speed multiplier |

---

## ⚙️ Configuration

### 🔧 Customization Options

Edit these values in the `VirtualMouseController.__init__()` method:

```python
# Adjust smoothing (higher = smoother but slower)
self.base_smooth_factor = 4.0    # Default: 4.0
self.max_smooth_factor = 6.5     # Default: 6.5

# Movement boundary (in pixels from edge)
self.frame_reduction = 100       # Default: 100

# Click timing
self.drag_hold_seconds = 0.45    # Default: 0.45s
self.double_click_window = 0.35  # Default: 0.35s

# Scroll settings
self.scroll_sensitivity = 1.4    # Default: 1.4

# MediaPipe confidence
min_detection_confidence=0.6     # Default: 0.6
min_tracking_confidence=0.5      # Default: 0.5
```

### 🎨 Visual Customization

Change UI colors and styles:

```python
# Boundary box color (BGR format)
cv2.rectangle(img, ..., (255, 0, 255), 2)  # Purple

# HUD text color
cv2.putText(img, hud, ..., (50, 200, 50), 2)  # Green
```

---

## 🔧 Troubleshooting

<details>
<summary><strong>❌ Webcam Not Detected</strong></summary>

**Solution:**
```bash
# Check if other apps are using the webcam
# Try changing camera index in code:
self.cap = cv2.VideoCapture(1)  # Try 1, 2, etc.
```
</details>

<details>
<summary><strong>❌ Hand Not Detected</strong></summary>

**Possible Causes:**
- Poor lighting conditions
- Hand too far or too close
- Complex background

**Solution:**
- Move to well-lit area
- Adjust distance (1-2 feet optimal)
- Lower detection confidence:
  ```python
  min_detection_confidence=0.4
  ```
</details>

<details>
<summary><strong>❌ Cursor Too Jittery</strong></summary>

**Solution:**
```python
# Increase smoothing
self.base_smooth_factor = 6.0
self.max_smooth_factor = 8.0

# Increase deadzone
self.deadzone_px = 5
```
</details>

<details>
<summary><strong>❌ Clicks Not Registering</strong></summary>

**Solution:**
```python
# Adjust pinch thresholds (increase multiplier)
left_click_thresh = self.dynamic_threshold(..., multiplier=2.0)
```
</details>

<details>
<summary><strong>❌ Performance Issues / Low FPS</strong></summary>

**Solution:**
- Close other applications
- Reduce webcam resolution
- Disable TensorFlow warnings (already in code)
- Use GPU acceleration if available
</details>

<details>
<summary><strong>❌ ImportError: No module named 'cv2'</strong></summary>

**Solution:**
```bash
pip uninstall opencv-python
pip install opencv-python
```
</details>

---

## ⚡ Performance Tips

### 🚀 Optimization Strategies

1. **Hardware**
   - Use a high-quality webcam (720p or higher)
   - Ensure good CPU (multi-core recommended)
   - Close unnecessary background applications

2. **Lighting**
   - Use bright, diffused lighting
   - Avoid backlighting
   - Position light source in front of you

3. **Software**
   - Keep drivers updated
   - Use latest Python version
   - Enable GPU acceleration for MediaPipe (if available)

4. **Settings**
   - Lower `min_tracking_confidence` for faster tracking
   - Reduce `point_history` maxlen for less smoothing
   - Adjust `frame_reduction` for larger control area

### 📊 Expected Performance

| Hardware | FPS | Latency |
|----------|-----|---------|
| **Low-end** (i3, integrated GPU) | 15-20 FPS | ~80ms |
| **Mid-range** (i5, dedicated GPU) | 25-30 FPS | ~50ms |
| **High-end** (i7+, RTX GPU) | 30+ FPS | ~30ms |

---

## 🤝 Contributing

Contributions make the open-source community amazing! Any contributions you make are **greatly appreciated**.

### How to Contribute

1. **Fork** the Project
2. **Create** your Feature Branch
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit** your Changes
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push** to the Branch
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open** a Pull Request

### 💡 Ideas for Contributions

- [ ] Add more gesture controls (zoom, rotate, etc.)
- [ ] Implement gesture customization UI
- [ ] Add multi-hand support for advanced controls
- [ ] Create gesture recording and playback
- [ ] Improve accuracy with ML model fine-tuning
- [ ] Add voice command integration
- [ ] Create mobile app version
- [ ] Develop gesture training mode
- [ ] Add haptic feedback support

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### MIT License Summary

✅ Commercial use  
✅ Modification  
✅ Distribution  
✅ Private use  

---

## 🙏 Acknowledgments

Special thanks to:

- **[Google MediaPipe](https://mediapipe.dev/)** - For the incredible hand tracking solution
- **[OpenCV](https://opencv.org/)** - For computer vision capabilities
- **[PyAutoGUI](https://pyautogui.readthedocs.io/)** - For cross-platform GUI automation
- The open-source community for inspiration and support

---

## 📬 Contact

<div align="center">

### **Akshay Saitwal**

[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=About.me&logoColor=white)](https://your-portfolio.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/akshay-saitwal)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yourusername)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:your.email@example.com)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/yourusername)

**Project Repository**: [Gesture-Controlled-Virtual-Mouse](https://github.com/yourusername/Gesture-Controlled-Virtual-Mouse)

</div>

---

## 📈 Project Stats

<div align="center">

![GitHub stars](https://img.shields.io/github/stars/yourusername/Gesture-Controlled-Virtual-Mouse?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/Gesture-Controlled-Virtual-Mouse?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/yourusername/Gesture-Controlled-Virtual-Mouse?style=social)

![GitHub issues](https://img.shields.io/github/issues/yourusername/Gesture-Controlled-Virtual-Mouse)
![GitHub pull requests](https://img.shields.io/github/issues-pr/yourusername/Gesture-Controlled-Virtual-Mouse)
![GitHub last commit](https://img.shields.io/github/last-commit/yourusername/Gesture-Controlled-Virtual-Mouse)
![GitHub code size](https://img.shields.io/github/languages/code-size/yourusername/Gesture-Controlled-Virtual-Mouse)

</div>

---

## 🎓 Learning Resources

Want to learn more about the technologies used?

### 📚 Recommended Reading

- [MediaPipe Hands Documentation](https://google.github.io/mediapipe/solutions/hands.html)
- [OpenCV Python Tutorial](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
- [Computer Vision Basics](https://www.pyimagesearch.com/start-here/)
- [Gesture Recognition Papers](https://arxiv.org/list/cs.CV/recent)

### 🎥 Video Tutorials

- Hand Tracking with MediaPipe
- OpenCV for Beginners
- Python GUI Automation
- Computer Vision Projects

---

## 🗺️ Roadmap

### Version 2.0 (Planned)

- [ ] **Multi-hand support** - Control with both hands
- [ ] **Gesture customization** - Define your own gestures
- [ ] **Voice commands** - Combine voice with gestures
- [ ] **Config GUI** - Easy settings adjustment
- [ ] **Gesture macros** - Record and replay gesture sequences
- [ ] **Cross-platform testing** - Full Linux/Mac support
- [ ] **Performance dashboard** - Real-time FPS and latency metrics
- [ ] **Tutorial mode** - Interactive gesture learning

### Version 3.0 (Future)

- [ ] **3D hand tracking** - Depth-based controls
- [ ] **AR integration** - Augmented reality overlays
- [ ] **Mobile app** - Control PC from phone gestures
- [ ] **Multi-screen support** - Work across multiple monitors
- [ ] **Accessibility features** - Customizable for different needs

---

<div align="center">

### 💖 Show Your Support

If you find this project helpful, please consider:

⭐ **Starring** the repository  
🐛 **Reporting** bugs and issues  
💡 **Suggesting** new features  
📢 **Sharing** with others  

![Wave](https://raw.githubusercontent.com/mayhemantt/mayhemantt/Update/svg/Bottom.svg)

**Made with ❤️ and 🖐️ by Akshay Saitwal**

<img src="https://komarev.com/ghpvc/?username=gesture-mouse&label=Project%20Views&color=0e75b6&style=flat" alt="Profile views" />

</div>

---

<div align="center">

### 🌟 "The future is touchless, and it starts with a gesture"

**Happy Gesturing! 🖐️✨**

</div>
