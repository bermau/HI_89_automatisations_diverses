# Le but est mieux comprendre le système e recherche d'images

import pyautogui
from pyautogui import Point

# import pyperclip
from time import sleep
import pyscreeze
pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False

from pprint import pprint

EXISTS = "../images/icone_1_white_on_black.png"
NOT_EXISTS = "../images/mate_file.png"

Point = {'start': Point(x=500, y=200)}

pyautogui.moveTo(Point['start'], duration=1)
sleep(1)
pyautogui.click()


def trouver_images():
    try:
        pyautogui.useImageNotFoundException(False)
        # pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False
        ret = pyautogui.locateAllOnScreen(EXISTS)
        return list(ret)

    except pyautogui.ImageNotFoundException:
        print("PAS TROUVé")
        return "BONJOR"
    finally:
        print("Je passe par la fin")
    return ["Rine trouvé du tout"]


locations = trouver_images()
if locations:
    for loc in locations:
        print(loc)
    print("FINI")
else:
    print("RIEN DU TOUT")
