# Accessible Audio Adventure

Python audio-first interactive experience designed for visually impaired users, controlled through hand gestures detected via webcam.

---

## 🚀 Overview

Accessible Audio Adventure is an experimental interactive system designed to provide a fully non-visual user experience.

The application allows users to navigate an audio-based adventure using only sound and simple hand gestures detected via webcam.
Instead of relying on a graphical interface, all interactions are guided through audio narration, feedback, and instructions.

This project explores accessibility-oriented interaction design by combining audio interfaces with computer vision.

---

## ✨ Features

* 🎧 Audio-first interaction (no visual UI required)
* ✋ Hand gesture input via webcam
* 🔢 Finger counting using computer vision
* 🎮 Scene-based interactive navigation
* 🔊 Audio narration, feedback, and instructions
* 💡 Contextual help system
* 🔐 Code-based scene transitions
* 🧩 Modular architecture (scenes, session, input mapping)

---

## 🧠 How It Works

The user interacts with the system by showing a number of fingers to the webcam.

The system:

1. Detects the number of fingers using computer vision
2. Waits for a stable input
3. Maps the number to an action depending on the current scene

Possible actions include:

* navigating menus
* replaying instructions
* triggering narration or descriptions
* entering numeric codes
* accessing help
* switching between scenes

---

## 🛠️ Tech Stack

* Python
* OpenCV
* MediaPipe
* NumPy
* TensorFlow
* playsound

---

## 📁 Project Structure

```text
.
├── Audios/                         # Audio files for narration and feedback
├── BasicFingerCountHandler.py      # Input handling via gestures
├── BasicScene.py                   # Scene definitions and behavior
├── BasicSceneInitializer.py        # Scene graph and story logic
├── BasicSceneMapping.py            # Input → action mapping
├── BasicSession.py                 # Session and game state management
├── FingerCount.py                  # Finger detection (MediaPipe + OpenCV)
├── main.py                         # Entry point
├── requirements.txt                # Dependencies
└── progetto_librogame.bat          # Windows launcher
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/SimonePisani/accessible-audio-adventure.git
cd accessible-audio-adventure
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the application:

```bash
python main.py
```

Make sure that:

* a webcam is available
* audio output is enabled
* the `Audios/` folder is present

---

## ♿ Accessibility Focus

This project was designed to explore alternative interaction models for users with visual impairments.

Key principles:

* audio replaces visual interfaces
* gesture input replaces keyboard/mouse
* repeated feedback ensures usability
* minimal reliance on visual elements

---

## 📌 Notes

This is an experimental project developed in an academic context, focused on:

* accessibility
* human-computer interaction
* computer vision

---

## 🚧 Future Improvements

* Add speech recognition as an alternative input
* Improve gesture detection robustness
* External configuration for scenes and audio
* Packaging as executable (.exe)
* UI for hybrid interaction (optional)

---

## 👨‍💻 Author

Simone Pisani
