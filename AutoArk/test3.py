import os
import pyautogui

from AutoArk import test2


def fun(a):
    pass


def restart(a):
    try:
        fun(a)
    except EOFError as e:
        print(e)
    finally:
        restart()


if __name__ == '__main__':
	restart(test2.py)