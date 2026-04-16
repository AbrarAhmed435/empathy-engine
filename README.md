# 🎙️ The Empathy Engine: Giving AI a Human Voice

## 🧠 Overview

The Empathy Engine is a system that bridges the gap between **text-based sentiment and expressive speech generation**. Traditional Text-to-Speech (TTS) systems often produce monotonic and robotic output, lacking emotional depth.

This project introduces an **emotion-aware modulation layer** that dynamically adjusts vocal characteristics such as **rate and volume** based on the detected sentiment of the input text, resulting in more natural and human-like speech.

---

## ⚙️ Features

- ✅ **Emotion Detection** (Positive, Negative, Neutral)
- ✅ **Dynamic Voice Modulation** (Rate, Volume, Pitch logic)
- ✅ **Intensity-Based Scaling** (emotion strength affects speech)
- ✅ **Audio File Generation** (.wav output)
- ✅ **CLI Interface** for quick testing
- ✅ **FastAPI Endpoint** for real-world integration

---

## 🏗️ Architecture

The system follows a **modular, pipeline-based architecture**:

### 🔄 Pipeline Flow
User Input (CLI/API)-> Emotion Detection (VADER)-> Emotion + Intensity Score-> Emotion-to-Voice Mapping-> Voice Parameters (rate, volume, pitch)-> Text-to-Speech Engine (pyttsx3)->Audio Output (.wav file)