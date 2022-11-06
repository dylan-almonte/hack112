from enemy1 import *
from enemy2 import *
from enemy3 import *

import random

class enemyWaveGenerator():
    def __init__(self, app):
        pass
        
    def spawnEnemy(self, app):    
        position = random.randint(0, 10)
        boardCell = app.width//10
        xPos = position * boardCell
        a = enemy1(xPos, 0)
        return a