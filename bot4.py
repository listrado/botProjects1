import multiprocessing
import time
import cv2
import keyboard
import numpy as np
import pyautogui
import win32api
import win32con

def key(k):
    pyautogui.keyDown(k)
    time.sleep(0.01)
    pyautogui.keyUp(k)


def key2(k):
    while not keyboard.is_pressed('q'):
        pyautogui.keyDown(k)
        time.sleep(2)
        pyautogui.keyUp(k)
        time.sleep(2)


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
    #win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.06)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

time.sleep(2)

count = 0
repet = 100000

if __name__ == '__main__':
    #w = multiprocessing.Process(target=key, args=('w',))
    #space = multiprocessing.Process(target=key, args=(' ',))
    #pics = ['startFort.png', 'readyFort.png', 'claimFort.png']
    while not keyboard.is_pressed('q'):
        #z = multiprocessing.Process(target=key2, args=('z',))
        #z.start()
        while count < repet and not keyboard.is_pressed('q'):
            #e = multiprocessing.Process(target=key, args=('e',))
            #space = multiprocessing.Process(target=key, args=('space',))
            #esc = multiprocessing.Process(target=key, args=('esc',))
            #look = multiprocessing.Process(target=mouse_move, args=(200, 0,))
            #look.start()
            #time.sleep(1)
            #e.start()
            #time.sleep(2)
            #space.start()
            #time.sleep(1)
            #esc.start()
            #e.join()
            #look.join()
            #space.join()
            #esc.join()
            time.sleep(0.03)
            #key('e')
            click(500, 500)
            count = count + 1
        #z.join()

