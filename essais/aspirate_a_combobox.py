# Le but est de récupérer la liste de ATB de l'étude consores.
# Ce script est adaptable pour aspirer toute liste simple contenu dans un combo

import pyautogui
from pyautogui import Point

import pyperclip
from time import sleep
from pprint import pprint
import pandas as pd

glm_app = {'antibiotique': Point(x=151, y=407),
           'materiel': Point(x=163, y=322),
           'uf': Point(x=374, y=557)}

last_atb = ''
lst = []

# position de départ : le second écran est ouvert puis calé en haut à gauche

pyautogui.moveTo(glm_app['antibiotique'])
pyautogui.click()

while True:
    sleep(0.3)
    pyautogui.hotkey('ctrl', 'c')
    nom = pyperclip.paste()

    if nom == last_atb:
        print("Fin?")
        break
    else:
        lst.append(nom)
        last_atb = nom
        pyautogui.write(['down'])
print("\nFIN :")

pprint(lst)

pd.DataFrame(lst, columns=['atb']).to_excel("../data_out/atb.xlsx", index=False)
