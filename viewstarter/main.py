import checkifprocessrunning
from telegrambot import t

t.start()
while True:
     if checkifprocessrunning.checkifprocessrunning("Lolify.exe") != True:
        checkifprocessrunning.checkifprocessrunning("Lolify.exe")


