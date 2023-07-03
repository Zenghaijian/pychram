import time

import win32gui
import win32api
import win32con
import pyautogui
import cv2


def get_xy(img_model_path):
    """
    用来判断游戏画面的点击坐标
    :param img_model_path:用来检测模板图片的路径
    :return:以元组形式返回区域的中心坐标
    """
    # 将屏幕截图保存
    pyautogui.screenshot().save("./pic/screenshot.png")
    # 载入图片
    img = cv2.imread("./pic/screenshot.png")
    # 图像模板
    img_terminal = cv2.imread(img_model_path)
    # 读取模板的宽度和高度
    height, width, channel = img_terminal.shape
    # 进行模板匹配
    result = cv2.matchTemplate(img, img_terminal, cv2.TM_SQDIFF_NORMED)
    # 解析出匹配区域的左上角坐标
    upper_left = cv2.minMaxLoc(result)[2]
    # 计算匹配区域右下角的坐标
    lower_right = (upper_left[0] + width, upper_left[1] + height)
    # 计算中心区域的坐标并且返回
    avg = (int((upper_left[0] + lower_right[0]) / 2), int((upper_left[1] + lower_right[1]) / 2))
    return avg


def auto_click(var_avg):
    """
    接受一个元组参数，自动点击
    :param var_avg: 坐标元组
    :return: None
    """
    pyautogui.click(var_avg[0], var_avg[1], button='left')
    time.sleep(1)


def routine(img_model_path, name):
    avg = get_xy(img_model_path)
    print(f'正在点击{name}')
    auto_click(avg)
    print(avg)


routine("pic/Rstar.png", "终端")
