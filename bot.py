import pywhatkit
import keyboard
import time
from datetime import datetime

contatos=('+5581999065969')

while len(contatos) >= 1:

    pywhatkit.sendwhatmsg(contatos[0], 'Testando meu bot de python',datetime.now().hour,datetime.now().minute + 1) 
    del contatos [0]
    time.sleep(60)
    keyboard.press_and_release('ctrl + w')