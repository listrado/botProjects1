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
repet = 10000

if __name__ == '__main__':
    #w = multiprocessing.Process(target=key, args=('w',))
    #space = multiprocessing.Process(target=key, args=(' ',))
    pics = ['startFort.png', 'readyFort.png', 'claimFort.png']
    while not keyboard.is_pressed('q'):
        while count < repet and not keyboard.is_pressed('q'):
            w = multiprocessing.Process(target=key, args=('w',))
            sete = multiprocessing.Process(target=key, args=('sete',))
            space = multiprocessing.Process(target=key, args=(' ',))
            look = multiprocessing.Process(target=mouse_move, args=(200, 0,))
            look.start()
            time.sleep(0.1)
            w.start()
            time.sleep(0.1)
            sete.start()
            time.sleep(1)
            space.start()
            w.join()
            look.join()
            space.join()
            sete.join()
            time.sleep(1)
            for pic in pics:
                if pyautogui.locateCenterOnScreen(pic, grayscale=True, confidence=0.7):
                    print('True')
                    cords = (pyautogui.locateCenterOnScreen(pic, grayscale=True, confidence=0.7))
                    # print(cords)
                    # print(cords.y)
                    # print(cords.x)
                    try:
                        click(cords.x, cords.y)
                    except:
                        print('failed')
                    # click(3000, 1400)
                    # key("w")
                    # time.sleep(0.1)
                else:
                    print('false')
            click(500, 500)
            count = count + 1


