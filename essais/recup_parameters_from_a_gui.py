# Copy / Past parameters between 2 GUI programs
# Les 2 fenètres étudiées sont Procédure et Analyseur

from lib_pyautogui import  GuiApp
import pyautogui
from pyautogui import Point

import pyperclip
from time import sleep
from pprint import pprint
import sys

# work = GuiApp()

param = []

# formulaire des procédures
procedure = {'onglet_comment': Point(x=166, y=210),
        'comment': Point(x=139, y=245),
        'nom': Point(x=132, y=141)}

init = Point(x=668, y=377)

first_round = True

offset = (0, 0)
# DC sur une ligne de procedure ou F6


def read_form():

    # Clic sur onglet "Comment"
    global first_round

    # if first_round:
    pyautogui.moveTo(procedure['onglet_comment'], duration = 0.5)
    pyautogui.click()
    sleep(0.5)
    first_round = False

    # Copier les champs :
    # se placer sur le champs 1:
    # envoyer Ctrl-A puis Ctrl-C, et récupérer dan champs 1
    pyautogui.moveTo(procedure["nom"])
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    nom = pyperclip.paste()

    # se placer sur le champ 2, envoyer Ctrl-A puis Ctrl-C, et récupérer dans champ comment
    pyautogui.moveTo(procedure["comment"])
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    comment = pyperclip.paste()
    print(f"{nom=}, {comment=}")

    param.append({"nom" : nom, "comment": comment })

# On passe à la ligne suivante par flèche bas.

if __name__ == '__main__':
    last = init

    for _ in range(250):
        pyautogui.moveTo(last)
        pyautogui.click()

        if not first_round:
            pyautogui.press('down')
            last = pyautogui.position()

        pyautogui.press('f6')
        sleep(1)
        read_form()
        # input("suite...")

    pprint(param)
    print("Terminé")
