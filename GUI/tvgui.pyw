import PySimpleGUI as sg
import os
import subprocess

sg.theme("DarkGrey2")
layout = [[sg.Radio("Regno Unito", "nazione", default = True, key = "uk")] + [sg.Radio("Tutto il mondo", "nazione", default = False)],
          [sg.Text("Inserisci il nome del canale")],
          [sg.Input(key = "canale"), sg.Button("Cerca")],
          [sg.Text("Inserisci l'indirizzo del canale")],
          [sg.Input(key = "indirizzo"), sg.Button("Guarda")]]
window = sg.Window("Tv dal Mondo", layout)
while True:
    event, values = window.read()
    if event == "Cerca":
        canale = values.get("canale").replace(" ", "_")
        os.chdir("C:\Program Files\BraveSoftware\Brave-Browser\Application")
        if values.get("uk") == True:
            subprocess.Popen("brave -app=https://hlscat.com/united_kingdom_/s/" + canale)
        if values.get("uk") == False:
            subprocess.Popen("brave -app=https://hlscat.com/s/" + canale)
    if event == "Guarda":
        indirizzo = values.get("indirizzo")
        window.FindElement("indirizzo").Update("")
        os.chdir("C:\Program Files\PotPlayer")
        subprocess.Popen("potplayermini64 " + indirizzo)
    if event == sg.WIN_CLOSED:
        break
window.close()
