from gtts import gTTS
import os
tts = gTTS(text='Good morning', lang='en')
tts.save("good.mp3")
os.system("mpg321 good.mp3") # Doesn't Work, must add something to PATH
# os.system("start C:/Code-Stuff/Projects/Py-Jarvis/good.mp3") # Doesn't Work

# https://stackoverflow.com/questions/40811540/gtts-google-text-to-speech-error-audio-gets-saved-but-does-not-play-automatic