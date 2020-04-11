class GameStats():

    def __init__(self, sy):
        
        self.sy = sy
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):

        self.ships_l = self.sy.ship_l

