from enemy1 import enemy1
from enemy2 import enemy2
from enemy3 import enemy3

import random


class enemyWaveGenerator():
    def __init__(self, app):
        pass

    def spawnEnemy(self, app):
        position = random.randint(250, 750)

        a = enemy1(position, 10, app)
        return a
