class GameStats():

    def __init__(self, sy):
        
        self.sy = sy
        self.reset_stats()
        self.game_active = False
        
        # Pontuação
        self.high_score =  0

    def reset_stats(self):

        self.ships_l = self.sy.ship_l
        self.score = 0

