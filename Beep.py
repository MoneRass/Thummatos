#Made by Thummatos Sribunna
#For Portfolio
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Tile 1 Position:X:  721 Y:  400 RGB: (156, 162, 231)
#Tile 2 Position:X:  875 Y:  400 RGB: (156, 161, 230)
#Tile 3 Position:X:  1016 Y:  400 RGB: (155, 161, 230)
#Tile 4 Position:X:  1194 Y:  400 RGB: (155, 161, 231)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    

    if pyautogui.pixel(721, 400)[0] == 0:
        click(721, 400)
    if pyautogui.pixel(875, 400)[0] == 0:
        click(875, 400)
    if pyautogui.pixel(1016, 400)[0] == 0:
        click(1016, 400)
    if pyautogui.pixel(1194, 400)[0] == 0:
        click(1194, 400)
#Made by Thummatos Sribunna
#For Portfolio

