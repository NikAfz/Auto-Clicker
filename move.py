import pyautogui as pag
import time
import random

def make_random_move(map:list):
    map_x1 = map[0] - 30
    map_x2 = map[0] + 30

    map_y1 = map[1] - 30
    map_y2 = map[1] + 30
    
    rand_x = random.randint(map_x1, map_x2)
    rand_y = random.randint(map_y1, map_y2)
    
    return pag.moveTo(rand_x, rand_y, 0.001)
	
    