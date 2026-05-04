# Accessible Audio Adventure

An interactive audio-based experience designed for visually impaired users, enabling navigation through a narrative environment using **hand gestures and real-time audio feedback**.

This project explores an alternative interaction paradigm that replaces traditional graphical interfaces with **gesture-based input and spatial audio output**.

---

## Overview

Accessible Audio Adventure is designed as an experimental system where users interact without relying on visual elements.

Instead of a graphical interface, the system provides:

* gesture-based navigation
* continuous audio feedback
* scene-based progression through an interactive story

The goal is to create an experience that is fully accessible to visually impaired users while remaining intuitive and engaging.

---

## Motivation

Most applications rely heavily on visual interfaces, limiting accessibility for users with visual impairments.

This project explores a different approach:

> replacing visual interaction with a combination of gesture recognition and audio feedback

The system is intentionally designed **without a traditional GUI** to investigate alternative user interaction models.

---

## Interaction Model

The interaction is based on a simple but effective loop:

1. The user performs a hand gesture
2. The system detects the gesture in real-time
3. A corresponding action is triggered
4. Audio feedback communicates the result

Example interactions:

* Open hand → move forward in the story
* Closed hand → interact with an element
* Directional gesture → change path or scene

Audio feedback is used to:

* indicate state changes
* guide navigation
* provide contextual information

---

## User Experience

The system is designed to be fully usable without visual feedback.

Users rely entirely on:

* **audio cues** for orientation and feedback
* **gestures** for interaction

This creates an experience where:

* navigation is intuitive
* feedback is immediate
* interaction does not depend on sight

---

## Features

* 🎧 Audio-driven interaction system
* ✋ Real-time hand gesture recognition
* 🧭 Scene-based navigation
* 🔊 Continuous feedback loop
* ♿ Accessibility-focused design

---

## Tech Stack

* **Python**
* **OpenCV** (camera input)
* **MediaPipe** (gesture detection)
* **NumPy**
* **TensorFlow** (gesture recognition support)
* **playsound** (audio output)

---

## System Architecture

The system is structured around three main components:

* **Input Layer** → gesture detection via webcam
* **Processing Layer** → gesture interpretation and scene logic
* **Output Layer** → audio feedback and narration

---

## Example Interaction

A typical interaction cycle:

* The user raises their hand in front of the camera
* The system detects the gesture using MediaPipe
* The gesture is mapped to an action
* A new scene is triggered
* Audio feedback communicates the transition

This loop allows continuous interaction without requiring visual cues.

---

## Challenges

* Designing interaction without visual feedback
* Mapping gestures to intuitive actions
* Ensuring real-time responsiveness
* Providing meaningful audio feedback
* Handling noisy or inconsistent input from gesture detection

---

## Notes

* This project was originally developed in a university environment
* The focus is on **interaction design and accessibility**, rather than UI/UX in the traditional sense
* The absence of a graphical interface is intentional

---

## Future Improvements

* Improved gesture recognition accuracy
* More complex interaction patterns
* Enhanced audio design (spatial audio, richer feedback)
* Support for additional accessibility features

---

## Key Takeaways

* Designed an interaction system without relying on visual interfaces
* Applied computer vision for real-time gesture recognition
* Explored accessibility-first design principles
* Built a complete input → processing → feedback pipeline
