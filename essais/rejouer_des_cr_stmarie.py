# Le but est re jouer des CR sur glms

# On a une liste de dossier sur lesquels il faut faire une suite d'actions.


import pyautogui
from pyautogui import Point

import pyperclip
from time import sleep
from pprint import pprint

lst_of_files = ['24041234', '24041227', '24040301']

glm_app = {'icone_liste_patients': Point(x=39, y=82),
           'liste_patients': Point(x=773, y=313),
           'bas_crs': Point(x=997, y=214)
           }


def ouvrir_liste_patients():
    pyautogui.moveTo(glm_app['icone_liste_patients'], duration=0.5)
    pyautogui.click()
    sleep(0.8)
    pyautogui.moveTo(glm_app['liste_patients'], duration=0.5)
    pyautogui.click()


def find_order(order_id: str) -> None:
    """
    Trouve un dossier.
    Préalable : la liste des dossiers doit être ouverte.
    :param order_id: str :
    :return:
    """
    pyautogui.hotkey('ctrl', 'f')  # Find
    pyautogui.write(order_id)
    pyautogui.write(["tab", 'tab', 'Enter'])
    sleep(0.8)


def open_cr():
    pyautogui.write(['alt', 'D'])
    pyautogui.write(["enter", "s", 'c'])
    # A ce point la liste des CR est ouverte.
    sleep(0.5)


def find_crs_locations():
    """Fonction pour contourner un bug de pyautogui"""
    pyautogui.write(['up', 'up'])
    sleep(0.5)

    pyautogui.useImageNotFoundException(False)
    # locations = pyautogui.locateAllOnScreen("../images/cyber_prod_black_on_white.png")
    locations = pyautogui.locateAllOnScreen("../images/cr_stm.png")
    if locations:
        return list(locations)
    else:
        return None


def locate_all_cr():
    sleep(0.5)
    # print("Je cherche...")
    pyautogui.write(['down', 'down'])
    # pyautogui.moveTo(glm_app['bas_crs'])
    # pyautogui.click()
    sleep(0.2)

    cr_location = find_crs_locations()

    if not cr_location:
        print("Je n'ai pas trouvé d'image de CR")
        pyautogui.write(['esc'])
        sleep(0.5)
        return None

    for i, cr in enumerate(cr_location):
        print(i, cr)
        pyautogui.moveTo(cr)
        pyautogui.click()
        rejouer_cr()

    sleep(2)
    pyautogui.write(['esc'])
    sleep(0.2)


def rejouer_cr():
    pyautogui.write(['f6'])
    pyautogui.write(['tab', 'tab', 'tab', 'space'], interval=0.1)
    sleep(0.2)
    ok_button = pyautogui.locateOnScreen("../images/OK_icon.png")
    if ok_button:
        pyautogui.moveTo(ok_button)
        sleep(0.2)
        pyautogui.click()


if __name__ == "__main__":
    lst = """24064454
24063816
24063162
24063166
24061617
24061418
24061804
24061808
24061111
24059347
24061107
24061109
24057480
24059348
"""

    for dossier in lst.split("\n"):
        print(f"Traitement du dossier {dossier}")
        # ouvrir_liste_patients()
        pyautogui.moveTo(glm_app['liste_patients'], duration=0.5)
        pyautogui.click()
        find_order(dossier)
        open_cr()
        locate_all_cr()

        # input("Dossier suivant...")
