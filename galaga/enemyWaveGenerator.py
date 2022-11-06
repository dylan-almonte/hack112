from enemy1 import enemy1
from enemy2 import enemy2
from enemy3 import enemy3

import random


class enemyWaveGenerator():
    def __init__(self):
        pass

    def spawnEnemy(self, app):
        position = random.randint(0, 10)
        boardCell = app.width//10
        xPos = position * boardCell
        a = enemy1(xPos, 10)
        return a
