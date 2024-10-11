import whisper

# Load the Whisper model (use "base" for a smaller model; "medium" or "large" for better accuracy)
model = whisper.load_model("base")

# Path to the audio file
audio_path = "output_audio_60s.wav"

# Transcribe the audio
result = model.transcribe(audio_path, language="cs")  # 'cs' is the code for Czech

# Print the transcription
with open("transcription.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])
