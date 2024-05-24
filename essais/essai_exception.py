"""Demonstration de la possiblité de capturer l'exception ImageNotFoundException"""

import pyautogui

# force use of ImageNotFoundException


NOT_EXISTS = "../images/icone_1_white_on_black_copy.png"
EXISTS = "../images/mate_file.png"

try:
    pyautogui.useImageNotFoundException()
    location = pyautogui.locateOnScreen(NOT_EXISTS)
    print('image found')
except pyautogui.ImageNotFoundException:
    print('ImageNotFoundException: image not found')