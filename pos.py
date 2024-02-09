import pyautogui as pag
import time

def pos():
    print("you have 5 seconds")
    time.sleep(1)

    print("you have 4 seconds")
    time.sleep(1)

    print("you have 3 seconds")
    time.sleep(1)

    print("you have 2 seconds")
    time.sleep(1)

    print("you have 1 seconds")
    time.sleep(1)


    return [pag.position().x, pag.position().y]


