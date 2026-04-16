import pyttsx3

engine = pyttsx3.init()

def speak_to_file(text: str, voice_params: dict, filename="output.wav"):
    rate = voice_params.get("rate", 150)
    volume = voice_params.get("volume", 0.8)

    # Apply parameters
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)

    # Save to file
    engine.save_to_file(text, filename)
    engine.runAndWait()

    print(f"Audio saved as {filename}")