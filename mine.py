import multiprocessing
import time
import cv2
import keyboard
import numpy as np
import pyautogui
import win32api
import win32con

def key(k):
    while not keyboard.is_pressed('q'):
        time.sleep(0.6)
        pyautogui.keyDown(k)
        pyautogui.keyDown('shift')
        print("key")
        time.sleep(10)
        pyautogui.keyUp('shift')
        pyautogui.keyUp(k) 

def clickk(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(np.random.uniform(0.1, 0.2))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def skip():
    while not keyboard.is_pressed('q'):
        time.sleep(0.1)
        for pic in pics:
            if pyautogui.locateCenterOnScreen(pic, grayscale=True, confidence=0.9):
                print('True')
                cords = (pyautogui.locateCenterOnScreen(pic, grayscale=True, confidence=0.9))
                    # print(cords)
                    # print(cords.y)
                    # print(cords.x)
                try:
                    if pic == 'menuComerciante2.png':
                        clickk(cords.x, cords.y)
                    else:
                        key('esc')
                except:
                    print('failed')
                    # click(3000, 1400)
                    # key("w")
                    # time.sleep(0.1)

def click(x, y):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(10)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

time.sleep(2)

count = 0
repet = 10000
pics = ['menuComerciante2.png', 'comerciante.png']

if __name__ == '__main__':
    #w = multiprocessing.Process(target=key, args=('w',))
    #space = multiprocessing.Process(target=key, args=(' ',))
    while not keyboard.is_pressed('q'):
        q = multiprocessing.Process(target=key, args=('d',))
        sskip = multiprocessing.Process(target=skip)
        q.start()
        while count < repet and not keyboard.is_pressed('q'):
#            w = multiprocessing.Process(target=key, args=('w',))
#            sete = multiprocessing.Process(target=key, args=('sete',))
#            space = multiprocessing.Process(target=key, args=(' ',))
#            time.sleep(0.1)
#            w.start()
#            time.sleep(0.1)
#            sete.start()
#            space.start()
            time.sleep(0.1)
#            w.join()
#            space.join()
#            sete.join()
#            time.sleep(1)
            try:
                if not keyboard.is_pressed('q'):
                    click(500, 500)
                    print(count/10)
            except:
                print('failed')
            count = count + 1
        q.join()

