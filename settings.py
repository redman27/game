class Settings():
    """Класс для хранения настроек игры"""
    def __init__(self):
        self.screen_wight = 1350
        self.screen_height = 700
        self.bg_color = (255, 255, 255)
        self.bullet_color = 238, 216, 13
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_allowed = 4
        self.fleet_drop_speed = 15
        self.ship_limit = 3
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed_factor = 8
        self.bullet_speed_factor = 7
        self.alien_speed_factor = 1
    # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
