# Le but est re jouer des CR sur glms

# On a une liste de dossier sur lesquels il faut faire une suite d'actions.


import pyautogui
from pyautogui import Point

import pyperclip
from time import sleep
from pprint import pprint


lst_of_files =  [ '24041234',  '24041227', '24040301']


glm_app = {'icone_liste_patients' : Point(x=39, y=82),
           'liste_patients' : Point(x=773, y=313),
            'bas_crs' : Point(x=997, y=214)
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
    sleep(0.5)
    # print("Je cherche...")
    pyautogui.write(['down', 'down'])
    # pyautogui.moveTo(glm_app['bas_crs'])
    # pyautogui.click()
    sleep(0.2)
    cr_location = pyautogui.locateAllOnScreen("../images/icone_1_black_on_white.png")

    # try:
    #     cr_location = pyautogui.locateAllOnScreen("../images/icone_1_black_on_white.png")
    # except :
    #     print("Pas de seconde image")

    for i, cr in enumerate(cr_location):
        print(i, cr)
        pyautogui.moveTo(cr)
        pyautogui.click()
        rejouer_cr()

    sleep(0.5)
    try:
        fermer_button = pyautogui.locateOnScreen("../images/fermer_icon.png")
        pyautogui.moveTo(fermer_button)
        pyautogui.click()
    except:
        print("Je ne trouve pas le bouton de fermeture. .. je vais utiliser Esc")
        pyautogui.write(['esc'])
        sleep(5)

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
    lst = """24057761
24058660"""

    for dossier in lst.split("\n"):

        print(f"Traitement du dossier {dossier}")

        # ouvrir_liste_patients()
        pyautogui.moveTo(glm_app['liste_patients'], duration=0.5)
        pyautogui.click()
        find_order(dossier)
        open_cr()
        locate_all_cr()
