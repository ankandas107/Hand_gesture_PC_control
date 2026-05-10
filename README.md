Hand Gesture Control System V1

Control your PC entirely with hand gestures using only a webcam.
Built with Python, OpenCV, and MediaPipe, this project transforms real-time hand movements into smooth mouse actions like cursor movement, clicking, scrolling, and pause control — without any external hardware.

📌 Project Description

Hand Gesture Control System V1 is a computer vision–based virtual mouse application that allows users to interact with their computer through intuitive hand gestures captured by a webcam.

The system uses MediaPipe Hand Landmark Detection to track finger positions in real time and converts them into mouse operations such as cursor movement, left click, right click, scrolling, and pause mode. Advanced safety mechanisms like auto-pause, gesture cooldowns, and a global quit switch help prevent accidental inputs and improve usability.

This project demonstrates practical applications of:

Computer Vision
Human-Computer Interaction (HCI)
Real-Time Gesture Recognition
AI-based Hand Tracking
✨ Features
🎯 Multi-Mode Interaction
MOVE MODE – Control cursor movement using your index finger.
SCROLL MODE – Scroll pages using vertical hand movement.
PAUSED MODE – Temporarily disable all controls for safety.
✋ Supported Gestures
🖱️ Move Cursor
Raise Index Finger Only
Cursor follows fingertip movement.
👆 Left Click
Pinch Thumb + Index Finger
Performs left mouse click.
👉 Right Click
Pinch Thumb + Middle Finger
Opens context menu/right click.
📜 Scroll Mode
Raise Index + Middle Fingers
Move hand:
Up → Scroll Up
Down → Scroll Down
✊ Pause Mode
Make a Closed Fist
Instantly pauses all controls.
❌ Quit Application
Press Q on keyboard
Safely exits the program.
🛡️ Advanced Safety Features
Auto-pause when hand is not detected
FPS monitoring for stable performance
Gesture cooldown system to avoid accidental double-clicks
Global emergency quit key (Q)
Real-time visual dashboard with:
FPS Counter
Current Mode
Active Gesture Detection
🧰 Technologies Used
Python – Core programming language
OpenCV – Webcam capture and image processing
MediaPipe – Hand tracking and landmark detection
PyAutoGUI / Mouse Control Libraries – System mouse automation
⚙️ Prerequisites
Python 3.8+
Webcam
MediaPipe Hand Landmark Model (hand_landmarker.task)
🚀 Installation & Setup
1️⃣ Clone the Repository
git clone <your-repository-link>
cd hand-gesture-control-system
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Download the MediaPipe Model
PowerShell
Invoke-WebRequest -Uri https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task -OutFile hand_landmarker.task
▶️ Run the Application
python main.py
⚙️ Configuration

You can customize settings inside config.py:

Setting	Purpose
SCROLL_SPEED	Controls scrolling sensitivity
GESTURE_COOLDOWN	Delay between clicks
SMOOTHING_FACTOR	Cursor movement smoothness
📈 Future Improvements (Version 3 Roadmap)
🎤 Voice Commands
⌨️ Virtual Keyboard / Air Typing
🧠 Custom Gesture Training
🎮 Gesture-Based Gaming Controls
🌐 Multi-Hand Support
📷 Project Highlights
Real-time gesture recognition
Smooth cursor tracking
Multiple interaction modes
Beginner-friendly computer vision project
Practical AI + HCI implementation
