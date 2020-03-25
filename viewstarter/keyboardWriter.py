import pyautogui
import time
from pynput.keyboard import Controller
from settings import *

starting = True


def settingsInput ():
    keyboard = Controller()
    time.sleep(wait_time)
    keyboard.type(threads)
    pyautogui.hotkey("enter")
    time.sleep(wait_time)
    keyboard.type("PROXYLESS")
    pyautogui.hotkey("enter")
    time.sleep(wait_time)
    keyboard.type(minPlay)
    pyautogui.hotkey("enter")
    time.sleep(wait_time)
    keyboard.type(maxPlay)
    pyautogui.hotkey("enter")
    time.sleep(wait_time)
    keyboard.type("y")
    pyautogui.hotkey("enter")
    time.sleep(wait_time)
    keyboard.type("y")
    pyautogui.hotkey("enter")
    time.sleep(wait_time)
    keyboard.type(songURL)
    pyautogui.hotkey("enter")
    time.sleep(wait_time)
