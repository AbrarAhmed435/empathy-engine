from fastapi import FastAPI
from pydantic import BaseModel
from emotion import detect_emotion
from mapper import map_emotion_to_voice
from tts import speak_to_file

app = FastAPI()

class Request(BaseModel):
    text: str

@app.post("/speak")
def speak_api(request: Request):
    text = request.text

    # Step 1: Emotion detection
    emotion, score = detect_emotion(text)

    # Step 2: Map to voice params
    voice_params = map_emotion_to_voice(emotion, score)

    # Step 3: Generate audio file
    filename = f"{emotion}_output.wav"
    speak_to_file(text, voice_params, filename)

    return {
        "emotion": emotion,
        "score": score,
        "voice_params": voice_params,
        "audio_file": filename
    }