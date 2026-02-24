import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import pygame
import os
import time

# Initialize recognizer
recognizer = sr.Recognizer()

def speak_kannada(text):
    filename = "kannada_output.mp3"
    
    # Convert text to speech
    tts = gTTS(text=text, lang='kn')
    tts.save(filename)

    # Initialize pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    # Wait until audio finishes playing
    while pygame.mixer.music.get_busy():
        time.sleep(0.5)

    pygame.mixer.quit()
    os.remove(filename)

def translate_to_kannada(text):
    return GoogleTranslator(source='en', target='kn').translate(text)

def listen_and_translate():
    with sr.Microphone() as source:
        print("🎤 Speak something in English...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        english_text = recognizer.recognize_google(audio)
        print("You said:", english_text)

        kannada_text = translate_to_kannada(english_text)
        print("Kannada Translation:", kannada_text)

        speak_kannada(kannada_text)

    except Exception as e:
        print("Error:", e)

# Run
listen_and_translate()