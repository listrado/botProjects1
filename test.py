import time
import keyboard
import pyautogui
from pynput.mouse import Controller, Button
import numpy as np
import win32api
import win32con
import win32gui
import win32ui

#Mouse = Controller()

def mouse_move(x, y):
    x2 = 0
    y2 = 0
    while x2 < x or y2 < y and not keyboard.is_pressed('q'):
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 1, 1, 1, 1)
        x2 = x2 + 1
        y2 = y2 + 1
        if x2 % 50 == 0:
            time.sleep(0.1)
        #win32api.SetCursorPos((100, 100))
        #pyautogui.moveTo(x, y, np.random.uniform(3, 4))
        #Mouse.position = (x, y)

time.sleep(1)
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
print(screenWidth)
print(screenHeight)
print(currentMouseX)
print(currentMouseY)
time.sleep(1)
#mouse_move(200, 100)
#mouse_move(200, 100)
pyautogui.displayMousePosition()
RGB: (234, 234, 234)
