# -*- coding: utf-8 -*-
"""
Written by MaYiming in HeNan XuChang on 2022.4.15
"""

import win32con
import win32api
import time

key_map = {
    "0": 49, "1": 50, "2": 51, "3": 52, "4": 53, "5": 54, "6": 55, "7": 56, "8": 57, "9": 58,
    "A": 65, "B": 66, "C": 67, "D": 68, "E": 69, "F": 70, "G": 71, "H": 72, "I": 73, "J": 74,
    "K": 75, "L": 76, "M": 77, "N": 78, "O": 79, "P": 80, "Q": 81, "R": 82, "S": 83, "T": 84,
    "U": 85, "V": 86, "W": 87, "X": 88, "Y": 89, "Z": 90
}


def key_down(key):
    """
    函数功能：按下按键
    参    数：key:按键值
    """
    key = key.upper()
    vk_code = key_map[key]
    win32api.keybd_event(vk_code, win32api.MapVirtualKey(vk_code, 0), 0, 0)


def key_up(key):
    """
    函数功能：抬起按键
    参    数：key:按键值
    """
    key = key.upper()
    vk_code = key_map[key]
    win32api.keybd_event(vk_code, win32api.MapVirtualKey(vk_code, 0), win32con.KEYEVENTF_KEYUP, 0)


def key_press(key):
    """
    函数功能：点击按键（按下并抬起）
    参    数：key:按键值
    """
    key_down(key)
    time.sleep(0.01)
    key_up(key)


def count_note(Note):
    """
    函数功能：为连接的音符数计数
    参    数：Note：相连的音符（中间无空格） 字符串类型
    """
    i = 0
    count = 0
    while i < len(Note):
        if Note[i] == '(':
            count += 1
            while 1:
                i += 1
                if Note[i] == ')':
                    i += 1
                    break
        else:
            count += 1
            i += 1
    return count


def play_note(Note, time_div, time_div_div, time_interval):
    """
    函数功能：播放连接的音符
    参    数：Note：相连的音符（中间无空格） 字符串类型
             time_div: 音符时值一次分割
             time_div_div：音符时值二次分割
             time_interval：单个小节的时值
    """
    play_time = time_interval / time_div / time_div_div
    i = 0
    while i < len(Note):
        if Note[i] == '(':
            while 1:
                i += 1
                if Note[i] == ')':
                    time.sleep(play_time)
                    i += 1
                    break
                else:
                    key_press(Note[i])
        elif Note[i].isalpha():
            key_press(Note[i])
            time.sleep(play_time)
            i += 1
        elif Note[i] == '1':
            time.sleep(play_time)
            i += 1
        else:
            i += 1


def play_music(music, time_interval):
    """
    函数功能：播放曲谱
    参    数：Music：曲谱 字符串类型
             time_interval：单个小节的时值
    """

    music_section = music.split("/")
    for i in range(len(music_section)):
        if music_section[i][-2:] == "  ":
            music_section[i] = music_section[i] + '1'

    for x in music_section:
        Notes = x.split()
        time_div = len(Notes)
        for y in Notes:
            time_div_div = count_note(y)
            play_note(y, time_div, time_div_div, time_interval)

# 七里香
seven = "A/S/S/S/S/S/D/D/G/D/D/D/S/A/A/D/S/S/S/S/A/N/N/S/S/S/S/D/D/D/G/D/S/A/A/A/A/D/S/S/S/S/S/A/N/N/N/N/S/S/S/S/S/S/D/D/G/D/S/A\
        "

# 延迟3秒播放
time.sleep(3)
# 播放音乐

# 庐州月副歌
play_music(seven, 0.4)

