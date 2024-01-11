import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #管理飞船发射的子弹
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        #创建一个子弹的矩形
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed #  更新子弹的位置
        self.rect.y = self.y #更新表示子弹的rect的位置

    def draw_bullet(self):
        #画子弹
        pygame.draw.rect(self.screen, self.color, self.rect)