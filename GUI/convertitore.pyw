from numpy import base_repr
import PySimpleGUI as sg

sg.theme("DarkBlack")
layout = [[sg.T("Decimale:     "), sg.I(key="dec"), sg.B("Calcola", key="10dec")],
          [sg.T("Binario:         "), sg.I(key="bin"), sg.B("Calcola", key="02bin")],
          [sg.T("Ottale:          "), sg.I(key="oct"), sg.B("Calcola", key="08oct")],
          [sg.T("Esadecimale:"), sg.I(key="hex"), sg.B("Calcola", key="16hex")]]
window = sg.Window("Strumento di conversione numeri", layout)
while True:
    event, values = window.read()
    if event and values.get(event[2:]) != "":
        numero = int(values.get(event[2:]), int(event[:-3]))
        window["dec"].update("")
        window["bin"].update("")
        window["oct"].update("")
        window["hex"].update("")
        window["dec"].update(numero)
        window["bin"].update(base_repr(int(numero), 2))
        window["oct"].update(base_repr(int(numero), 8))
        window["hex"].update(base_repr(int(numero), 16))
    if event == sg.WIN_CLOSED:
        break
window.close()
