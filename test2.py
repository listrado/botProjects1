import multiprocessing
import time

import keyboard
import numpy as np
import pyautogui
import win32api
import win32con


def key(k):
    pyautogui.keyDown(k)
    time.sleep(np.random.uniform(3, 5))
    pyautogui.keyUp(k)


def mouse_move(x, y):
    x2 = 0
    y2 = 0
    while x2 < x or y2 < y and not keyboard.is_pressed('q'):
        if y > y2:
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 1, 0, 0)
            y2 = y2 + 1
        if x > x2:
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 1, 0, 0, 0)
            x2 = x2 + 1
        if x2 % 50 == 0:
            time.sleep(0.1)


#    pyautogui.moveTo(x, y, np.random.uniform(3, 4))
#    time.sleep(0.5)
#    pyautogui.moveTo(x + 1000, y + 1000, np.random.uniform(0.3, 0.5))

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(np.random.uniform(0.1, 0.2))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


time.sleep(2)
count = 0
count2 = 0

if __name__ == '__main__':
    # w = multiprocessing.Process(target=key, args=('w',))
    # space = multiprocessing.Process(target=key, args=(' ',))
    while not keyboard.is_pressed('q'):
        time.sleep(0.1)
        if pyautogui.locateCenterOnScreen('testLua.png', grayscale=False, confidence=0.6):
            print('True')
            cords = (pyautogui.locateCenterOnScreen('testLua.png', grayscale=False, confidence=0.6))
            # print(cords)
            # print(cords.y)
            # print(cords.x)
            try:
                # click(cords.x, cords.y)
                print(cords)
            except:
                print('failed')
            # click(3000, 1400)
            # key("w")
            # time.sleep(0.1)
        sc = pyautogui.screenshot()
        width, height = sc.size
        count = 0
        count2 = 0
        for x in range(0, width, 1):
            for y in range(0, height, 1):
                r, g, b = sc.getpixel((x, y))
                if r == 151 and g == 126 and b == 136:
                    print(r, g, b)
                    count2 = 9
                if r == 255 and 190 <= g >= 180 and 65 <= b >= 55:
                    print(r, g, b)  
                    count = 1
        chest = count + count2
        if chest == 10:
            print(chest == 10)

        if pyautogui.locateCenterOnScreen('testLua.png', grayscale=False, confidence=0.6):
            print('True')
            cords = (pyautogui.locateCenterOnScreen('testLua.png', grayscale=False, confidence=0.6))
            # print(cords)
            # print(cords.y)
            # print(cords.x)
            try:
                # click(cords.x, cords.y)
                print(cords)
            except:
                print('failed')
            # click(3000, 1400)
            # key("w")
            # time.sleep(0.1)
        else:
            print('false')
