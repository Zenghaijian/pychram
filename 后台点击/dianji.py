import win32gui
from PyQt6.QtWidgets import QApplication
import sys

hwnd_title = dict()


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


# 获取所有的句柄和应用名
def all_hwnd():
    win32gui.EnumWindows(get_all_hwnd, 0)
    # print(hwnd_title.items())
    for h, t in hwnd_title.items():
        if t != "":
            print(h, t)


# 程序会打印窗口的hwnd和title，有了title就可以进行截图了。
def jietu(x, y):
    hwnd = win32gui.FindWindow(x, y)
    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(hwnd).toImage()
    img.save("screenshot.jpg")


if __name__ == '__main__':
    jietu('UnityWndClass', '原神')
