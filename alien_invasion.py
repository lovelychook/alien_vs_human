import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from bullet_alien import AlienBullet

class AlienInvasion:
    def __init__(self):
        pygame.init() #初始化游戏
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)
        self.bullet = pygame.sprite.Group()
        self.bullet_alien = pygame.sprite.Group()
        self.alien = Alien(self)

    def _check_keydown_events(self, event): #相应按下
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        if event.key == pygame.K_SPACE:
            self._fire_bullet()
        if event.key == pygame.K_PAGEDOWN:
            self.alien.moving_right = True
        if event.key == pygame.K_DELETE:
            self.alien.moving_left = True
        if event.key == pygame.K_HOME:
            self.alien.moving_up = True
        if event.key == pygame.K_END:
            self.alien.moving_down = True
        if event.key == pygame.K_BACKSPACE:
            self._fire_bullet_alien()

    def _fire_bullet(self): #限制子弹的数量
        if len(self.bullet) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullet.add(new_bullet)

    def _fire_bullet_alien(self):  # 限制子弹的数量
        if len(self.bullet_alien) < self.settings.bullets_allowed:
            new_bullet_alien = AlienBullet(self)
            self.bullet_alien.add(new_bullet_alien)

    def _check_keyup_events(self, event):  # 相应释放
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        if event.key == pygame.K_PAGEDOWN:
            self.alien.moving_right = False
        if event.key == pygame.K_DELETE:
            self.alien.moving_left = False
        if event.key == pygame.K_HOME:
            self.alien.moving_up = False
        if event.key == pygame.K_END:
            self.alien.moving_down = False

    def _check_events(self):
        # 侦听鼠标和键盘
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:  #按下
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)  #释放

    def _update_screen(self):
        # 让最近绘制的屏幕可见
        self.screen.fill(self.settings.bg_color)  # fill()用来填充背景
        for bullet in self.bullet.sprites():
            bullet.draw_bullet()
        for bullet in self.bullet_alien.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.alien.blitme()

    def _update_bullets(self): #更新1子弹1位置并删除已消失的子弹
        self.bullet.update()
        self.bullet_alien.update()
        for bullet in self.bullet.copy():
            if bullet.rect.bottom < 0:
                self.bullet.remove(bullet)
        for bullet_alien in self.bullet_alien.copy():
            if bullet_alien.rect.bottom > self.settings.screen_height:
                self.bullet_alien.remove(bullet_alien)
        if pygame.sprite.spritecollideany(self.ship, self.bullet_alien):
            print("Ship hit!!!")
            sys.exit()
        if pygame.sprite.spritecollideany(self.alien, self.bullet):
            print("Alien hit!!!")
            sys.exit()

    def run_game(self):
            #开始游戏循环
        while True:
            # 侦听鼠标和键盘
            self._check_events()
            self.ship.update()
            self.alien.update()
            self._update_bullets()
            #让最近绘制的屏幕可见
            self._update_screen()
            pygame.display.flip()
            self.clock.tick(60)



if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
