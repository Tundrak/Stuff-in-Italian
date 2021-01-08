import PySimpleGUI as sg
import secrets

def inizio():
    sg.theme("DarkBlack")
    layoutInizio = [[sg.Text("Benvenuto in Indovina il Numero!")],
                    [sg.Button("Inizia"), sg.Button("Istruzioni"), sg.Button("Esci")]]
    windowInizio = sg.Window("Indovina il Numero", layoutInizio, size=(270, 70), element_justification="c")
    while True:
        event, values = windowInizio.read()
        if event == "Istruzioni":
            sg.PopupNoButtons(
                "Ho pensato a un numero tra 1 e 100 e tu devi indovinarlo. Prova con un numero qualsiasi e ti darò indicazioni su come avvicinarti di più a quello giusto!", title="Istruzioni")
        if event == "Inizia":
            windowInizio.close()
            gioco()
        if event == sg.WIN_CLOSED or event == "Esci":
            break
    windowInizio.close()

def gioco():
    numero = secrets.randbelow(100)
    sg.theme("DarkBlack")
    layout = [[sg.Text("Inserisci un numero!")],
              [sg.Input(key="tentativo"), sg.Button("Prova", bind_return_key=True)]]
    window = sg.Window("Indovina il Numero", layout)
    while True:
        event, values = window.read()
        if event == "Prova":
            tentativo = values.get("tentativo")
            if tentativo.isdigit() is False:
                window.FindElement("tentativo").Update("")
                sg.PopupNoButtons("Puoi solo inserire numeri come risposta, non lettere o simboli!", title="Errore")
            elif int(tentativo) > numero:
                window.FindElement("tentativo").Update("")
                sg.PopupNoButtons("Il numero che hai scritto è più grande di quello a cui ho pensato!", title="Hai sbagliato")
            elif int(tentativo) < numero:
                window.FindElement("tentativo").Update("")
                sg.PopupNoButtons("Il numero che hai scritto è più piccolo di quello a cui ho pensato!", title="Hai sbagliato")
            elif int(tentativo) == numero:
                window.FindElement("tentativo").Update("")
                window.close()
                fine()
        if event == sg.WIN_CLOSED:
            break
    window.close()
    
def fine():
    sg.theme("DarkBlack")
    layoutFine = [[sg.Text("Bravo, hai indovinato il numero!")],
                  [sg.Text("Vuoi giocare ancora?")],
                  [sg.Button("Sì"), sg.Button("No")]]
    windowFine = sg.Window("Indovina il Numero", layoutFine, size=(270, 100), element_justification="c")
    while True:
        event, values = windowFine.read()
        if event == "Sì":
            windowFine.close()
            gioco()
        if event == sg.WIN_CLOSED or event == "No":
            break
    windowFine.close()

inizio()