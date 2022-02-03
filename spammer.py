import pyautogui
import time

time.sleep(10)

with open("wordlist", 'r') as f:
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")

# Now open a chat dialog and start this script :)