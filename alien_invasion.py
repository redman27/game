import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from pygame.sprite import Group
from button import Button
from scoreboard import Scoreboard
from bg import BackGround

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_wight, ai_settings.screen_height))
    pygame.display.set_caption('Атака Злобного Писюна')
    b = BackGround('images/space.bmp', [0, 0])
    ship = Ship(ai_settings, screen)
    stats = GameStats(ai_settings)
    play_button = Button(ai_settings, screen, 'Играть')
    sb = Scoreboard(ai_settings, screen, stats)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
bullets)
        bullets.update()
        gf.update_screen(ai_settings,b, screen, stats, sb, ship, aliens, bullets, play_button)
run_game()
