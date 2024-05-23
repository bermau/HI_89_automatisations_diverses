# Le but est re jouer des CR sur glms

# On a une liste de dossier sur lesquels il faut faire une suite d'actions.


import pyautogui
from pyautogui import Point

import pyperclip
from time import sleep
from pprint import pprint


lst_of_files =  [ '24041234',  '24041227', '24040301']


glm_app = {'icone_liste_patients' : Point(x=39, y=82),
           'liste_patients' : Point(x=773, y=313)
             }

def ouvrir_liste_patients():
    pyautogui.moveTo(glm_app['icone_liste_patients'], duration = 0.5)
    pyautogui.click()
    sleep(0.8)
    pyautogui.moveTo(glm_app['liste_patients'], duration=0.5)
    pyautogui.click()

def find_order(order_id : str) -> None:
    """
    Trouve un dossier.
    Préalable : la liste des dossiers doit être ouverte.
    :param order_id: str :
    :return:
    """
    pyautogui.hotkey('ctrl', 'f') # Find
    pyautogui.write(order_id)
    pyautogui.write(["tab", 'tab', 'Enter'])
    sleep(0.8)

def open_cr():
    pyautogui.write(['alt', 'D'])
    pyautogui.write(["enter", "s", 'c'])
    # A ce point la liste des CR est ouverte.
    sleep(0.5)

def locate_all_cr():
    sleep(1)
    # print("Je cherche...")
    try:
        cr_location = pyautogui.locateAllOnScreen("../images/icone_1_white_on_black.png")
    except:
        print("Pas de première image")

    try:
        cr_location = pyautogui.locateAllOnScreen("../images/icone_1_black_on_white.png")
    except :
        print("Pas de seconde image")

    for cr in cr_location:
        print(cr)
        pyautogui.moveTo(cr)
        pyautogui.click()
        rejouer_cr()

    sleep(0.5)
    try:
        fermer_button = pyautogui.locateOnScreen("../images/fermer_icon.png")
        pyautogui.moveTo(fermer_button)
        pyautogui.click()
    except:
        print("Je ne trouve pas le bouton de fermeture. ")

        input("Suite...")

def rejouer_cr():
    pyautogui.write(['f6'])
    pyautogui.write(['tab', 'tab', 'tab', 'space'], interval = 0.1)
    sleep(0.2)
    ok_button= pyautogui.locateOnScreen("../images/OK_icon.png")
    if ok_button:
        pyautogui.moveTo(ok_button)
        sleep(0.2)
        pyautogui.click()


if __name__ == "__main__":
    # ouvrir_liste_patients()
    pyautogui.moveTo(glm_app['liste_patients'], duration=0.5)
    pyautogui.click()
    find_order('24060048')
    open_cr()
    locate_all_cr()

"""
24058295
24060048
24060109
24041269
24059471
"""