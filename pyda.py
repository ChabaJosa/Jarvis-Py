
import wolframalpha    
import PySimpleGUI as sg 
client = wolframalpha.Client('44Q652-4RYAJKUGJU')

sg.theme('Dark Red 2')

layout = [  [sg.Text('Hello Mr. Stark')],
            [sg.Text('Enter a command:'), sg.InputText()],
            [sg.OK(), sg.Cancel()]]

window = sg.Window('Jarvis', layout)        # Create the window

while True:
    event, values = window.read()               # Display and interact with the Window                
    if event in (None, 'Cancel'):
        break
    res = client.query(values[0])
    sg.Popup(next(res.results).text)

# Finish up by removing from the screen
window.close()                                  
