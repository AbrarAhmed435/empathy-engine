from emotion import detect_emotion
from mapper import map_emotion_to_voice
from tts import speak_to_file

def main():
    text = input("Enter your text: ")

    emotion, score = detect_emotion(text)
    print(f"Detected Emotion: {emotion} (score: {score})")

    voice_params = map_emotion_to_voice(emotion, score)
    print("Voice Params:", voice_params)

    filename = f"{emotion}_output.wav"
    speak_to_file(text, voice_params, filename)

if __name__ == "__main__":
    main()