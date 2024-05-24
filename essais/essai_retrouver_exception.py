"""Demonstration de la possiblité de capturer l'exception ImageNotFoundException.
Ici je veux retrouver l'erreur initiale."""

import pyautogui

# force or not force use of ImageNotFoundException


NOT_EXISTS = "../images/icone_1_white_on_black_copy.png"
EXISTS = "../images/mate_file.png"

try:
    # pyautogui.useImageNotFoundException()
    location = pyautogui.locateOnScreen(EXISTS)
    print('image found')
except IndexError:
    print('ImageNotFoundException: image not found')