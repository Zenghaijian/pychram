import os
import pyautogui



def qidong():
    yeshen = r" E:\tool\Nox\bin\Nox.exe"
    a = os.popen(yeshen)
    print(a)

def weizhi():
    location = pyautogui.locateOnScreen(image='arknight.png')       # 查找图片
    x, y = pyautogui.center(location)                               # 查找图片坐标
    print('center()', x, y)                                         # 算出图片中心坐标
    pyautogui.click(x=x, y=y, clicks=1, button='left')              #

def start():
    location = pyautogui.locateOnScreen(image='start.png')       # 查找图片
    x, y = pyautogui.center(location)                               # 查找图片坐标
    print('center()', x, y)                                         # 算出图片中心坐标
    pyautogui.click(x=x, y=y, clicks=1, button='left')

def huanxing():
    location = pyautogui.locateOnScreen(image='huanxing.png')       # 查找图片
    x, y = pyautogui.center(location)                               # 查找图片坐标
    print('center()', x, y)                                         # 算出图片中心坐标
    pyautogui.click(x=x, y=y, clicks=1, button='left')

# def friends():
#     location = pyautogui.locateOnScreen(image='friends.png')       # 查找图片
#     x, y = pyautogui.center(location)                               # 查找图片坐标
#     print('center()', x, y)                                         # 算出图片中心坐标
#     pyautogui.click(x=x, y=y, clicks=1, button='left')

def fight():
    location = pyautogui.locateOnScreen(image='fight.png')       # 查找图片
    x, y = pyautogui.center(location)                               # 查找图片坐标
    print('center()', x, y)                                         # 算出图片中心坐标
    pyautogui.click(x=x, y=y, clicks=1, button='left')

if __name__ == '__main__':
    print(fight())
