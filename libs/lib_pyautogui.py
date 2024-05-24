import pyautogui
import pyperclip
import keyboard
from pyautogui import Point

from time import sleep



class GuiApp:
    """A GUI Form"""
    def __init__(self):
        self.cible = self.find_position()

    def find_position(self):
        print("Cliquer sur la zone à enregistrer")
        sleep(2)
        pos = pyautogui.position()
        print(pos)
        return pyautogui.position()

    def ask_for_positions(self):
        dico = {}
        cont = True
        while cont:
            print("Designer une positions et cliquer ")

            if keyboard.is_pressed('a'):
                print("Lecture")
                pos = pyautogui.position()
                label = input("Nom (END pour finier) ? ")
                if label == "END":
                    cont = False
                else:
                    dico[label] = pos

        print(dico)
        return dico


    def send_to_target(self, msg,):
        pyautogui.click(self.cible[0], self.cible[1])
        sleep(1)
        pyperclip.copy(msg)
        pyautogui.hotkey('ctrl', 'v')

if __name__ == '__main__':

    app = GuiApp()

