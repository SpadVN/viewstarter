import os
import time
from keyboardWriter import settingsInput
from mouseControl import openAccountTXT
from settings import *


def restart():
    os.system("TASKKILL /f  /IM  CHROMEDRIVER.EXE")
    os.system("TASKKILL /f  /IM  CHROME.EXE")
    os.startfile(loliPath)
    settingsInput()
    time.sleep(1)
    openAccountTXT()
