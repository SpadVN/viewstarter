import pyautogui
import time
from pynput.keyboard import Key, Controller
from settings import *


def settingsInput():
    time.sleep(wait_time)
    keyboard = Controller()
    keyboard.type("CRACKED-89712-XNO00-80YPP-3X6MD-TO")
    time.sleep(wait_time)
    pyautogui.hotkey("enter")
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
