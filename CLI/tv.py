import os
import subprocess

print("Guarda TV utilizzando HLS!")
print("")
canale = input("Inserisci il nome del canale.\n").replace(" ", "_")
os.chdir("C:\Program Files\BraveSoftware\Brave-Browser\Application")
subprocess.Popen("brave -app=https://hlscat.com/united_kingdom_/s/" + canale)
print("")
indirizzo = input("Inserisci l'indirizzo ottenuto.\n")
os.chdir("C:\Program Files\PotPlayer")
subprocess.Popen("potplayermini64 " + indirizzo)
