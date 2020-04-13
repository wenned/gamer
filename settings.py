class Settings():
    
    def __init__(self):

        self.screen_w = 900
        self.screen_h = 600
        self.bg = (230,230,230)
        self.ship_speed = 1.5
        self.ship_l = 1

        #   configuração dos projeteis
         
        self.bullet_speed_factor = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 90, 60, 70
        self.bullets_allowed = 3      

        # configuração dos alieniginas
        
        self.alien_speed = 1.1
        self.speed_scale = 1.1
        self.fleet_drop = 10
        self.fleet_direction = 1.1
       
        self.speedup_scale = 1.5
        self.score_scale = 1.5       

        # pontuação

        self.alien_points = 50

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        
        self.alien_speed = 1
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 1
        self.fleet_direction = 1

    def increase_speed(self):

        self.ship_speed *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
