import pygame

class Ship:
    #管理飞船
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings #给飞船增加设置属性
        self.screen_rect = ai_game.screen.get_rect() #将整个游戏屏幕的矩形存储在一个变量中
        #加载飞船
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        #确定初始位置
        self.rect.midbottom = self.screen.get_rect().midbottom
        self.x = float(self.rect.x)
        self.moving_right = False #飞船一开始不移动
        self.moving_left = False  # 飞船一开始不移动
        self.moving_up = False  # 飞船一开始不移动
        self.moving_down = False  # 飞船一开始不移动

    def update(self):
        #飞船移动
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top >0:
            self.rect.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.ship_speed
    def blitme(self):
        #指定位置绘制飞船
        self.screen.blit(self.image, self.rect)
