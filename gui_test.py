import PySimpleGUI as sg

# 1) Define the window's contents
layout = [[sg.Text("Your Top songs are:")],
          [sg.Text("Drake-Life is good")],
          [sg.Button('Ok'), sg.Button('Quit')]]

# 2) Create the window
window = sg.Window('Spotify Stats-Justin', layout)

# 3) Display and interact with the Window using an Event Loop
        #values is the return of what we return
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    # window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI", text_color='blue')

# Finish up by removing from the screen
window.close()