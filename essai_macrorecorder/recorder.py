import pyautogui
import pynput
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener, Key
import time
import json

actions = []
recording = True

def on_move(x, y):
    if recording:
        actions.append(('move', x, y, time.time()))

def on_click(x, y, button, pressed):
    if recording:
        actions.append(('click', x, y, button.name, pressed, time.time()))

def on_scroll(x, y, dx, dy):
    if recording:
        actions.append(('scroll', x, y, dx, dy, time.time()))

def on_press(key):
    if recording:
        try:
            actions.append(('press', key.char, time.time()))
        except AttributeError:
            actions.append(('press', key.name, time.time()))

def on_release(key):
    actions.append(('release', key.name, time.time()))
    if key == Key.esc:
        # Stop listener
        print("Stop !")
        print(actions)
        recording = False
        mouse_listener.stop()
        return False

time.sleep(4)


# Start listeners
with MouseListener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as mouse_listener, \
     KeyboardListener(on_press=on_press, on_release=on_release) as keyboard_listener:
    mouse_listener.join()
    keyboard_listener.join()

# Save actions to a file
with open('actions.json', 'w') as f:
    print("Writing data...")
    json.dump(actions, f)
