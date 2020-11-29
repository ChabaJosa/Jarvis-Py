
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
    
    # Clear Variables
    wolfram_res = None
    wiki_res    = None
    popup       = None

    try:
        try:
            res = client.query(values[0]);
            wolfram_res = next(res.results).text;
        except:
            pass   
        try:
            wiki_res = wikipedia.summary(values[0], sentences=2);
        except:
            pass  

        if wolfram_res != None or wiki_res != None:
            if wolfram_res and wiki_res != None:
                popup = ('Wolfram Result: ' + wolfram_res, 'Wikipedia Result: '+ wiki_res) 
            elif wiki_res != None:
                popup = ('Wikipedia Result: '+ wiki_res);
            elif wolfram_res != None:
                popup = ('Wolfram Result: '+ wiki_res);
            else:
                engine.say("Sorry.")
                engine.runAndWait()    
            print('This is the current popup', popup)
            engine.say(popup)
            sg.PopupNonBlocking(popup)
            engine.runAndWait()
        else:
            engine.say("Sorry Sir, Could not find anything.")
            engine.runAndWait()   
          
    except:
        engine.say("Could not find anything, sir.")
        engine.runAndWait()
    
# Finish up by removing from the screen
window.close() 

# Simple GUI Docs:        https://pysimplegui.readthedocs.io/en/latest/
# wolframalpha Pypi:      https://pypi.org/project/wolframalpha/
# wolframalpha Website:   https://developer.wolframalpha.com/portal/myapps/index.html
# Wikipedia Pypi:         https://pypi.org/project/wikipedia/ 

# To Add Speech Recognition: https://medium.com/towards-artificial-intelligence/creating-a-voice-recognition-application-with-python-57d8c3e55256
