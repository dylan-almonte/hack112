import random
import enemyWaveGenerator


class EnemyWave ():
    enemyList = []

    def spawnEnemy(self, app):
        EnemyWave.enemyList.append(
            enemyWaveGenerator.spawnEnemy(self, app))

    def moveEnemy(self):
        for enemy in EnemyWave.enemyList:
            vel = enemy.getVel
            enemy.move(vel)
            enemy.drawEnemy()
        

    def deleteEnemy(self, enemy):

        EnemyWave.enemyList.remove(enemy)

    # return drawings of enemies
