# Le but est mieux comprendre le système e recherche d'images

import pyautogui
from pyautogui import Point

# import pyperclip
from time import sleep
import pyscreeze
pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False

from pprint import pprint

NOT_EXISTS = "../images/icone_1_white_on_black_copy.png"
EXISTS = "../images/mate_file.png"

Point = {'start': Point(x=500, y=200)}

pyautogui.moveTo(Point['start'], duration=1)
sleep(1)
pyautogui.click()


def trouver_images():
    try:
        # pyautogui.useImageNotFoundException()
        # pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False
        ret = pyautogui.locateAllOnScreen(NOT_EXISTS)
        return ret

    except pyautogui.ImageNotFoundException:
        print("PAS TROUVé")
        return "BONJOR"
    except pyscreeze.ImageNotFoundException:
        print('RIEN')
        return("TUTUTUTU")
    finally:
        print("JE passe par la fin")
    return ["Rine trouvé du tout"]


locations = trouver_images()

for loc in locations:
    print(loc)
print("FINI")
