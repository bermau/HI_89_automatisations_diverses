import pyautogui
import pyperclip

from time import sleep



class GuiApp:
    def __init__(self):
        self.cible = self.find_position()

    def find_position(self):
        print("Cliquer sur la zone à enregistrer")
        sleep(2)
        pos = pyautogui.position()
        print(pos)
        return pyautogui.position()


    def send_to_target(self, msg,):
        pyautogui.click(self.cible[0], self.cible[1])
        sleep(1)
        pyperclip.copy(msg)
        pyautogui.hotkey('ctrl', 'v')

if __name__ == '__main__':

    app = GuiApp()

