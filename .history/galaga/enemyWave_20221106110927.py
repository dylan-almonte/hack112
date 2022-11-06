import random
from enemyWaveGenerator import enemyWaveGenerator


class EnemyWave():
    enemyList = []
    bulletList =[]

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

    def bulletMovement(self, app, playerX, playerY):
        for enemy in EnemyWave.enemyList:
            enemy.bulletMovement(app, playerX, playerY)
    
    def updateBullets(self):
        EnemyWave.bulletList = []
        for enemy in EnemyWave.enemyList:
            EnemyWave.bulletList.extend(enemy.bulletList)

    def deleteEnemy(self, enemy):

        EnemyWave.enemyList.remove(enemy)

    # return drawings of enemies
