import pyautogui
import time

time.sleep(5)

f = open("wordlist", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")

# Now open a chat dialog and start this script :)