from pynput.mouse import Button, Controller
from settings import coordFile


def openAccountTXT():
    mouse = Controller()
    mouse.position = coordFile
    mouse.click(Button.left, 2)
