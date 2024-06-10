# Directment de chatGPT

import pyautogui
import json
import time

# Load actions from file
with open('actions.json', 'r') as f:
    actions = json.load(f)

start_time = actions[0][2]

for action in actions:
    action_type = action[0]
    if action_type == 'move':
        _, x, y, timestamp = action
        time.sleep(timestamp - start_time)
        pyautogui.moveTo(x, y)
    elif action_type == 'click':
        _, x, y, button, pressed, timestamp = action
        time.sleep(timestamp - start_time)
        if pressed:
            pyautogui.mouseDown(x, y, button=button)
        else:
            pyautogui.mouseUp(x, y, button=button)
    elif action_type == 'scroll':
        _, x, y, dx, dy, timestamp = action
        time.sleep(timestamp - start_time)
        pyautogui.scroll(dy, x, y)
    elif action_type == 'press':
        _, key, timestamp = action
        time.sleep(timestamp - start_time)
        pyautogui.press(key)
    elif action_type == 'release':
        _, key, timestamp = action
        time.sleep(timestamp - start_time)
        # pyautogui does not have a release function

    start_time = timestamp
