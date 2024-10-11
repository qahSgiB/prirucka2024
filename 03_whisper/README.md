# OpenAI Whisper

## Record of Conversation: Audio Transcription with Whisper

**Date:** October 9, 2024  
**Participants:** Petr Zikán (Human), AI Assistant

---

### Conversation Summary

**Human:**  
ROLE: I want you to act as a Python and machine learning expert in this exercise.  
OBJECTIVE: I need a Python script that takes a path to an MP4 video recording, processes sound, and provides me with a textual transcript. The recording is in the Czech language. I want to use the open-source library Whisper from OpenAI. The script should be as short as possible and it should be stand-alone, i.e., not depending on any other local modules. Let's go step by step and start first with generating concise high-level action points with a short (2-3 sentences long) summary. We will explore details later on.

**AI:**  
Here are the high-level action points for creating a Python script that transcribes audio from a Czech MP4 video using OpenAI's Whisper:
1. **Install Dependencies**: Ensure the `whisper` library and any required dependencies like `ffmpeg` are installed. Whisper requires `ffmpeg` for audio extraction from video files.
2. **Extract Audio from MP4**: Use `ffmpeg` to extract the audio from the video file and save it as a temporary audio file (e.g., `.wav`).
3. **Load and Transcribe Audio**: Use Whisper to load the extracted audio file and transcribe it, specifying the Czech language model if possible for better accuracy.
4. **Output Transcription**: Print or save the transcription output to a text file for easy access.

**Human:**  
Ok, so let's explore step number 1 first. Can you provide us with a detailed procedure how to install all dependencies including `whisper`. We are running Ubuntu 22.04, running Python 3.10.

**AI:**  
Here's the detailed procedure for installing all the necessary dependencies, including `whisper`, on an Ubuntu 22.04 system with Python 3.10:
1. **Update System Packages**: Run `sudo apt update && sudo apt upgrade -y`.
2. **Install Python 3.10 and pip**: Run `sudo apt install python3.10 python3-pip -y` and verify with `python3.10 --version`.
3. **Install `ffmpeg`**: Run `sudo apt install ffmpeg -y`.
4. **Set Up a Virtual Environment (Optional)**: Run `python3.10 -m venv whisper_env` and `source whisper_env/bin/activate`.
5. **Install Whisper Library**: Run `pip install git+https://github.com/openai/whisper.git`.
6. **Verify Installation**: Run `python -c "import whisper; print('Whisper installed successfully')"`.

**Human:**  
Let's proceed with the step 2.

**AI:**  
To extract audio from an MP4 video using `ffmpeg`, follow this:
1. **Extract Audio**: Use `ffmpeg -i input_video.mp4 -vn -acodec pcm_s16le -ar 16000 -ac 1 output_audio.wav`.
2. **Verify the Extracted Audio**: Use `ffplay output_audio.wav` to ensure the audio is extracted correctly.

**Human:**  
Step 3, please!

**AI:**  
To use Whisper to transcribe the audio:
1. **Create the Python Script**:
   ```python
   import whisper

   model = whisper.load_model("base")
   audio_path = "output_audio.wav"
   result = model.transcribe(audio_path, language='cs')
   print("Transcription:")
   print(result["text"])
