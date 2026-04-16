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
User Input (CLI/API)-> Emotion Detection (VADER) -> Emotion + Intensity Score -> Emotion-to-Voice Mapping -> Voice Parameters (rate, volume, pitch) -> Text-to-Speech Engine (pyttsx3) -> Audio Output (.wav file)


---

### 🧩 Component Breakdown

- **emotion.py**
  - Performs sentiment analysis using VADER
  - Outputs emotion label and intensity score

- **mapper.py**
  - Maps emotion + intensity to voice parameters
  - Implements dynamic scaling logic

- **tts.py**
  - Applies parameters and generates audio using pyttsx3

- **main.py**
  - CLI interface for user input

- **api.py**
  - FastAPI interface for real-world usage

---

### 🧠 Design Principle

The system follows **separation of concerns**:
- NLP (emotion detection)
- Decision logic (mapping)
- Output generation (TTS)

This makes the system **modular, scalable, and extensible**.

---

## 🧪 How It Works

1. Input text is analyzed using **VADER sentiment analysis**
2. A **compound score (-1 to +1)** is generated
3. Emotion is classified into:
   - Positive
   - Negative
   - Neutral
4. Voice parameters are dynamically adjusted:
   - **Rate (speed)**
   - **Volume (loudness)**
   - **Pitch (logical mapping)**
5. Audio is generated using modified parameters

---

## 🎯 Emotion-to-Voice Mapping Logic

Instead of static mapping, the system uses **intensity-aware scaling**:

- Strong positive → faster, louder speech  
- Strong negative → slower, softer speech  
- Neutral → balanced delivery  

This creates a more **natural and expressive output**.

---

## ⚠️ Note on Pitch

While pitch is included in the mapping logic, **pyttsx3 has limited pitch control support**. Therefore, **rate and volume are the primary modulation parameters**.

---

## 🚀 Setup Instructions

### 1. Clone Repository

```bash
git clone <your-repo-link>
cd empathy-engine