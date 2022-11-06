import random
from enemyWaveGenerator import enemyWaveGenerator


class EnemyWave():
    enemyList = []

    def spawnEnemy(self):
        EnemyWave.enemyList.append(
            enemyWaveGenerator.spawnEnemy(self))

    def moveEnemies(self):
        for enemy in EnemyWave.enemyList:
            enemy.updateEnemyTime()
            enemy.updateEnemyXpos()
            enemy.updateEnemyYpos()
            enemy.drawEnemy()

    def drawEnemies(self, canvas):
        for enemy in EnemyWave.enemyList:
            enemy.drawEnemy(canvas)

    def deleteEnemy(self, enemy):

        EnemyWave.enemyList.remove(enemy)

    # return drawings of enemies
