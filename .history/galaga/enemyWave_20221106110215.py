import random
from enemyWaveGenerator import enemyWaveGenerator


class EnemyWave():
    enemyList = []

    def spawnEnemy(self, app):
        EnemyWave.enemyList.append(
            enemyWaveGenerator.spawnEnemy(self, app))

    def moveEnemies(self):
        for enemy in EnemyWave.enemyList:
            enemy.updateEnemyTime()
            enemy.updateEnemyXpos()
            enemy.updateEnemyYpos()
            enemy.drawEnemy()

    def drawEnemies(self, app, canvas):
        for enemy in EnemyWave.enemyList:
            enemy.drawEnemy(app, canvas)
            enemy.drawBullet(app, canvas)

    def bulletMovement(app, playerX, playerY):
        for enemy in EnemyWave.enemyList:
            enemy.bulletMovement(app, playerX, playerY)


    def deleteEnemy(self, enemy):

        EnemyWave.enemyList.remove(enemy)

    # return drawings of enemies
