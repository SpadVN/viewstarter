import checkifprocessrunning
from Telegram import t


t.start()
while True:
     if checkifprocessrunning.checkifprocessrunning("Lolify.exe") != True:
        checkifprocessrunning.checkifprocessrunning("Lolify.exe")


