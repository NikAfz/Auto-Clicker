import pyautogui as pag
import time
import keyboard

from pos import pos
from move import make_random_move
from click import click
from tip import tip

first_pos = pos()
print(tip())
while True :
  
  make_random_move(first_pos)
  
  if keyboard.is_pressed("s"):
    break
  
  click()
  
  if keyboard.is_pressed("s"):
    break
