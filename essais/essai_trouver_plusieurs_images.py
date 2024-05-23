# Le but est mieux comprendre le système e recherche d'images

import pyautogui
from pyautogui import Point

import pyperclip
from time import sleep
from pprint import pprint

Point = {'start': Point(x=500, y=200)}

pyautogui.moveTo(Point['start'], duration=1)
sleep(1)
pyautogui.click()
print("après premier clic")

locations = pyautogui.locateAllOnScreen("../images/mate_file.png")

for loc in locations:
    print(loc)
