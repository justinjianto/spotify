import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyOAuth
import PySimpleGUI as sg


scope = "user-library-read user-read-recently-played user-read-playback-state user-top-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id ="Your own ID", client_secret= "Your own ID",
redirect_uri="http://localhost:8000", scope=scope))

#get name of current user
# print(sp.current_user()["display_name"])

#get users top tracks
top_tracks = sp.current_user_top_tracks(time_range="long_term")

testing_entry = top_tracks['items'][0]
# print(type(testing_entry))
top_entrys = list()
for curr_dict in top_tracks['items']:
    top_entrys.append(curr_dict['name'])

# print("your top songs of all time are:", ', '.join(top_entrys))


#DEALING WITH THE GUI
# 1) Define the window's contents
layout = [
          [sg.Text("Your Top songs are:")],
        #   [sg.Text("Drake-Life is good")],
        #   [sg.Button('Ok'), sg.Button('Quit')]
         ]
# listing out all the songs   
for index,entry in enumerate(top_entrys):
    layout.append([sg.Text(f"#{index + 1}) {entry}")])

layout.append([sg.Button('Ok'), sg.Button('Quit')])

# 2) Create the window
window = sg.Window('Spotify Stats-Justin', layout)
# 3) Display and interact with the Window using an Event Loop
        #values is the return of what we return
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit' or event == 'Ok':
        break
    # Output a message to the window
    # window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI", text_color='blue')

# Finish up by removing from the screen
window.close()








#each dict in curr_dict has:
    # dict_keys(['album', 'artists', 'available_markets', 'disc_number', 'duration_ms', 'explicit', 'external_ids', 
    # 'external_urls', 'href', 'id', 'is_local', 'name', 'popularity', 'preview_url', 'track_number', 'type', 'uri'])



# print(sp.current_user_playing_track())

# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])