import multiprocessing
import time
from pynput.mouse import Controller, Button
import keyboard
import numpy as np
import pyautogui
import win32api
import win32con

time.sleep(1)
Mouse = Controller()

def key(k):
    pyautogui.keyDown(k)
    time.sleep(np.random.uniform(3, 5))
    pyautogui.keyUp(k)

def click(x, y):
    Mouse.position = (x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(np.random.uniform(0.1, 0.2))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

print(np.version.version)
while not keyboard.is_pressed('q'):
    time.sleep(0.1)
    if pyautogui.locateCenterOnScreen('bot2.png', grayscale=True, confidence=0.4):
        print('True')
        cords = (pyautogui.locateCenterOnScreen('bot2.png', grayscale=True, confidence=0.4))
        #print(cords)
        #print(cords.y)
        #print(cords.x)
        if keyboard.is_pressed('c'):
            try:
                click(cords.x, cords.y)
            except:
                print('failed')
        #click(3000, 1400)
        #key("w")
        #time.sleep(0.1)
    else:
        print('false')