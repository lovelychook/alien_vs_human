class Settings:
    '''储存游戏设置'''

    def __init__(self):
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed = 5 #飞船的速度
        self.alien_speed = 5  # 飞船的速度
        #子弹设置
        self.bullet_speed = 6
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 10