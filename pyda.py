
import wolframalpha 
client = wolframalpha.Client('44Q652-4RYAJKUGJU')

import wikipedia   

import pyttsx3
import PySimpleGUI as sg 


sg.theme('Dark Red 2')

layout = [  [sg.Text('Hello Mr. Stark')],
            [sg.Text('Enter a command:'), sg.InputText()],
            [sg.OK(), sg.Cancel()]]

window = sg.Window('Jarvis', layout)        # Create the window

while True:
    event, values = window.read()               # Display and interact with the Window                
    if event in (None, 'Cancel'):
        break
    engine = pyttsx3.init()
    
    try:
        res = client.query(values[0]);
        wolfram_res = next(res.results).text;
        wiki_res = wikipedia.summary(values[0], sentences=2);
        sg.Popup('Wolfram Result: ' + wolfram_res, 'Wikipedia Result: '+ wiki_res);
        engine.say(wolfram_res)
        engine.runAndWait()
        print(values[0])
    except:
        engine.say("Couldn't find anything.")
        engine.runAndWait()
    
# Finish up by removing from the screen
window.close() 

# Simple GUI Docs:        https://pysimplegui.readthedocs.io/en/latest/
# wolframalpha Pypi:      https://pypi.org/project/wolframalpha/
# wolframalpha Website:   https://developer.wolframalpha.com/portal/myapps/index.html
# Wikipedia Pypi:         https://pypi.org/project/wikipedia/ 


# https://youtu.be/NZMTWBpLUa4?t=1470
