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
1. **Update System Packages**: Run  
   ```  
   sudo apt update && sudo apt upgrade -y  
   ```
2. **Install Python 3.10 and pip**: Run  
   ```  
   sudo apt install python3.10 python3-pip -y  
   ```  
   and verify with  
   ```  
   python3.10 --version  
   ```
3. **Install `ffmpeg`**: Run  
   ```  
   sudo apt install ffmpeg -y  
   ```
4. **Set Up a Virtual Environment (Optional)**: Run  
   ```  
   python3.10 -m venv whisper_env  
   source whisper_env/bin/activate  
   ```
5. **Install Whisper Library**: Run  
   ```  
   pip install git+https://github.com/openai/whisper.git  
   ```
6. **Verify Installation**: Run  
   ```  
   python -c "import whisper; print('Whisper installed successfully')"  
   ```

**Human:**  
Let's proceed with the step 2.

**AI:**  
To extract audio from an MP4 video using `ffmpeg`, follow this:
1. **Extract Audio**: Use  
   ```  
   ffmpeg -i input_video.mp4 -vn -acodec pcm_s16le -ar 16000 -ac 1 output_audio.wav  
   ```
2. **Verify the Extracted Audio**: Use  
   ```  
   ffplay output_audio.wav  
   ```  
   to ensure the audio is extracted correctly.

**Human:**  
Step 3, please!

**AI:**  
To use Whisper to transcribe the audio:
1. **Create the Python Script**:  
   ```  
   import whisper

   model = whisper.load_model("base")
   audio_path = "output_audio.wav"
   result = model.transcribe(audio_path, language='cs')
   print("Transcription:")
   print(result["text"])
   ```
2. **Run the Script**: Save it as `transcribe.py` and run  
   ```  
   python3 transcribe.py  
   ```
3. **Save Output**: Modify the script to save the output:  
   ```  
   with open("transcription.txt", "w", encoding="utf-8") as f:
       f.write(result["text"])
   ```

**Human:**  
Can you provide me with `ffmpeg` command that would extract only first 60 seconds of the `output_audio.wav`?

**AI:**  
Use the following command:  
```  
ffmpeg -i output_audio.wav -t 60 -c copy output_audio_60s.wav  
```  
This extracts the first 60 seconds from `output_audio.wav` and saves it as `output_audio_60s.wav`.

**Human:**  
We got the following text from the audio:

=====================================  
Tak nahráváme. Dobry. Takže ešte jednou vás vítám teda. No příručce, všichnihni tady uděvili se úlost nahráváním ho diny. Je to tak? Super, super. Nebojde mi to nikdy zvěřejný vat. Jo. A já jsem témulové o tom, že by jsme ten záznamstý přednášky, skusili převí spovocí Open AI whisper do tekstové podoby. To nároveme do GPT, a pokusíme se vytvorit zapyž. V druhu jadí nejsebo ksíme vytvorit zapyž zprbního diny, a to podom dáme na GitHub. Já jsem se moc zvěravé, je zdobry fungovat. Stoučeštíno se troško bojem žene, ale koukou jsem, že tako čištíno dole nejak oficialne podporuje.  
===================================

Could you "polish" the text and convert it to a proper Czech language?

**AI:**  
Certainly! Here is a polished version of the provided text, corrected for proper Czech language:

**Tak nahráváme. Dobře. Takže ještě jednou vás vítám. Všichni jsme tady prošli úlohou nahrávání hodinového záznamu, že? Super, super. Nebojte, nikde to nebudeme zveřejňovat. A já jsem přemýšlel o tom, že bychom ten záznam z přednášky zkusili převést pomocí OpenAI Whisper do textové podoby. Pak to nahrneme do GPT a pokusíme se vytvořit zápis. V další fázi se pokusíme vytvořit zápis z první hodiny a potom ho dáme na GitHub. Jsem velmi zvědavý, jestli to bude dobře fungovat. S češtinou mám trochu obavy, ale koukal jsem, že by ji Whisper měl oficiálně podporovat.**

---

This document serves as a record of our discussion on using Whisper for transcribing Czech audio from an MP4 video. It outlines the steps taken, from dependency installation to transcription and polishing the final text output.
