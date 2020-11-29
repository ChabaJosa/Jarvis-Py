# To Add Speech Recognition: 
# https://medium.com/towards-artificial-intelligence/creating-a-voice-recognition-application-with-python-57d8c3e55256
import speech_recognition as sr

r = sr.Recognizer()
file = sr.AudioFile('good-wav.wav')

with file as source:
 r.adjust_for_ambient_noise(source)
 audio = r.record(source)
 result = r.recognize_google(audio,language='en-IN')
print(result)

# To Convert MP3 to WAV: https://www.zamzar.com/convert/mp3-to-wav/