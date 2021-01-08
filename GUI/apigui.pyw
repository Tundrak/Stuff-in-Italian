import PySimpleGUI as sg
import requests

risposta = requests.get("https://status.mojang.com/check")
dati = risposta.text
dati = dati.replace("[", "")
dati = dati.replace("]", "")
dati = dati.replace("{", "")
dati = dati.replace("}", "")
dati = dati.replace("\"", "")
dati = dati.replace(":", "  ->  ")
dati = dati.replace("green", "Attivo")
dati = dati.replace("red", "Non attivo")
dati = dati.replace("orange", "Ha problemi")
dati = dati.replace(",", "\n")

sg.theme("DarkBlack")
layout = [[sg.Text("Il server risponde con il codice " + str(risposta.status_code))],
          [sg.Text(dati)]]
window = sg.Window("Strumento controllo server Mojang", layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
window.close()
