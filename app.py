import sounddevice as sd
import soundfile as sf
import numpy as np
import tempfile
from faster_whisper import WhisperModel
import cohere
from gtts import gTTS
import os
from dotenv import load_dotenv
from playsound import playsound
import arabic_reshaper
from bidi.algorithm import get_display

# Load Whisper 
model = WhisperModel("base", device="cpu",compute_type='float32')

# Load .env and get Cohere API key
load_dotenv()
cohere_key = os.getenv("COHERE_API_KEY")
if not cohere_key:
    raise ValueError("COHERE_API_KEY not found. Check your .env file.")
# Create Cohere client
co = cohere.Client(cohere_key)

def record_audio(duration=4, fs=16000):
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype=np.int16)
    sd.wait()
    return audio

while True:
    # Record short chunk
    audio_data = record_audio(4)

    # Save temporarily
    temp_wav = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    sf.write(temp_wav.name, audio_data, 16000)


    # Transcribe
    segments, _ = model.transcribe(temp_wav.name, language="ar")
    user_text = " ".join([seg.text for seg in segments]).strip()
    reshaped_user = arabic_reshaper.reshape(user_text)
    display_user = get_display(reshaped_user)
    print(f"👤: {display_user}")
    

    # AI Response
    response = co.generate(
        model='command-r-plus',
        prompt=user_text,
        max_tokens=100
    )
    bot_text = response.generations[0].text.strip()
    reshaped_bot = arabic_reshaper.reshape(bot_text)
    display_bot = get_display(reshaped_bot)

    print(f"🤖: {display_bot}")

    # Text-to-Speech
    tts = gTTS(bot_text, lang='ar')
    tts.save("reply.mp3")
    playsound("reply.mp3")