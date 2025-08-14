# Realtime-Voice-Chat

This project is a Realtime Voice Chat system using Python.  
It allows a user to:  
1. Speak into a microphone.  
2. Convert speech to text using **Faster-whisper**.  
3. Generate AI responses using **Cohere**.  
4. Convert AI responses back to speech using **gTTS**.  
5. Listen to the responses in real-time through the system speakers.


## Requirements
- Python 3.9 - 3.12  
- Packages:
You can download and install all required packages with the following command:  
- **Record audio from microphone**
```bash
pip install sounddevice
```
- **Handle numerical operations on audio data**
```bash
pip install numpy
```
- **Speech-to-text using Whisper model**
```bash
pip install faster-whisper
```
- **AI text generation using cohere**
```bash
pip install cohere
```
- **Text-to-speech (Google TTS)**
```bash
pip install gtts
```
- **Load environment variables from .env**
```bash
pip install python-dotenv
```
- **Read/write audio files**
```bash
pip install soundfile
```
- **Cross-platform audio playback**
```bash
pip install playsound
```
- **Arabic text shaping and bidirectional display**
```bash
pip install arabic_reshaper python-bidi
```
## Environment Setup

1. Create a `.env` file in the project folder.  
2. Add your Cohere API key like this:`COHERE_API_KEY=your_api_key_here`
COHERE_API_KEY=your_api_key_here
3. The program will automatically load the API key using `python-dotenv`.

## Demo Video

You can watch a demonstration of the Realtime Voice Chat project here:
[Watch Demo](demo_video.mp4)

