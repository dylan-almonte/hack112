
class Enemy:

    Size: int = 10

    def __init__(self, x, y, health):
        self.health: int = health

        """
        positition of Enemy
        """
        self.x: int = x
        self.y: int = y

    def isHit(self, player_missles) -> bool:
        '''
        iterates through the player missles and checks if the missiles are in the 
        enemy hitbox and returns a bool 
        '''
        self.health -= 1
        for missle_xy in player_missles:
            if (self.x, self.y) in missle_xy:
                return True
        return False

    def move(self,)
