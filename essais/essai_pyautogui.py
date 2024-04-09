import pyautogui
import pyperclip

from time import sleep

def find_position():
    sleep(2)
    return pyautogui.position()

def send_to_target(msg, pos):
    pyautogui.click(pos[0], pos[1])
    sleep(1)
    pyperclip.copy(msg)
    pyautogui.hotkey('ctrl', 'v')

