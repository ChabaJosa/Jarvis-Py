from gtts import gTTS
import os
tts = gTTS(text='Good morning', lang='en')
tts.save("good.mp3")
os.system("mpg321 good.mp3")

# https://stackoverflow.com/questions/40811540/gtts-google-text-to-speech-error-audio-gets-saved-but-does-not-play-automatic