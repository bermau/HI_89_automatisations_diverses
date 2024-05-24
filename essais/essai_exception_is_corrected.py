"""Demonstration de la possibilité de contourner l'exception ImageNotFoundException"""

import pyautogui

NOT_EXISTS = "../images/icone_1_white_on_black_copy.png"
EXISTS = "../images/mate_file.png"

def search_on_screen():
    try:
        # force use of ImageNotFoundException
        pyautogui.useImageNotFoundException(False)
        location = pyautogui.locateAllOnScreen(EXISTS)
        return location

    except:
        print("Autre erreur lors de la recherche d'images")
        return None


if __name__ == '__main__':

    images = list(search_on_screen())
    if images:
        print("Il y a images")
        for image in images:
            print(image)
    else:
        print("PAS d'IMAGE")