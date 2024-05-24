"""Demonstration de la possiblité de capturer l'exception ImageNotFoundException"""

import pyautogui

# force use of ImageNotFoundException


NOT_EXISTS = "../images/icone_1_white_on_black_copy.png"
EXISTS = "../images/mate_file.png"

def search_on_screen():
    try:
        pyautogui.useImageNotFoundException()
        location = pyautogui.locateOnScreen(EXISTS)
        print('image found')
        print(location)
        return location
    except pyautogui.ImageNotFoundException:
        print('ImageNotFoundException: image not found')
        return None

if __name__ == '__main__':

    images = search_on_screen()
    if images:
        for image in images:
            print(image)
    else:
        print("PAS d'IMAGE")