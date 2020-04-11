class Settings():
    
    def __init__(self):
        self.screen_w = 900
        self.screen_h = 700
        self.bg = (230,230,230)
        self.ship_speed = 1.5

        #   configuração dos projeteis
         
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 90, 60, 70
        self.bullets_allowed = 3      

        # configuração dos alieniginas

        self.alien_speed = 1
        self.fleet_drop = 10
        self.fleet_direction = 1
