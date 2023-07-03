import time

import win32gui
import win32api
import win32con

def dianji(x, y):
    p1 = (x, y)
    handle = win32gui.FindWindow(None, '原神')
    rect = win32gui.GetWindowRect(handle)
    win32api.SetCursorPos((rect[0] + p1[0], rect[1] + p1[1]))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def xunhuan(x, y):
    a = 1
    while a < 10000000000:
        dianji(x, y)
        a = a+1
        time.sleep(5)

if __name__ == '__main__':
    xunhuan(900, 650)
