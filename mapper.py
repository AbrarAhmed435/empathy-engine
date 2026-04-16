def map_emotion_to_voice(emotion: str, score: float):
    """
    Maps emotion and intensity score to voice parameters.
    score: -1 (very negative) → +1 (very positive)
    """

    base_rate = 150
    base_volume = 0.8
    base_pitch = 0  # Note: pyttsx3 has limited pitch control

    if emotion == "positive":
        rate = base_rate + int(score * 50)      # faster
        volume = min(1.0, base_volume + 0.2)
        pitch = int(score * 30)

    elif emotion == "negative":
        rate = base_rate + int(score * 50)      # slower (score is negative)
        volume = max(0.5, base_volume - 0.2)
        pitch = int(score * 30)

    else:  # neutral
        rate = base_rate
        volume = base_volume
        pitch = base_pitch

    return {
        "rate": rate,
        "volume": volume,
        "pitch": pitch
    }