import random
from enemyWaveGenerator import enemyWaveGenerator


class EnemyWave():
    enemyList = []

    def spawnEnemy(self, app):
        EnemyWave.enemyList.append(
            enemyWaveGenerator.spawnEnemy(self, app))

    def moveEnemy(self):
        for enemy in EnemyWave.enemyList:
            enemy.updateEnemyTime()
            enemy.updateEnemyXpos()
            enemy.updateEnemyYpos()
            #enemy.updateYpos()
            # vel = enemy.getVel(time)
            # enemy.move(vel[0], vel[1])
            # enemy.drawEnemy()

    def drawEnemies(self, canvas):
        for enemy in EnemyWave.enemyList:
            enemy.drawEnemy(canvas)

    def deleteEnemy(self, enemy):

        EnemyWave.enemyList.remove(enemy)

    # return drawings of enemies
