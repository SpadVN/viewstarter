from pynput.mouse import Button, Controller
from settings import coordFile, coordRef


def openAccountTXT():
    mouse = Controller()
    mouse.position = coordFile
    mouse.click(Button.left, 2)

def windowRef():
    mouse = Controller()
    mouse.position = coordRef
    mouse.click(Button.left, 1)