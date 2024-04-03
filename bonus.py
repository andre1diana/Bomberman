import pygame
import time


class Bonus:
    def __init__(self, window, x, y, bonus_type):
        self.window = window
        self.position_x = x
        self.position_y = y
        self.life = pygame.transform.scale(pygame.image.load("RES/Bonus_life.png"), (50, 50))
        self.speed = pygame.transform.scale(pygame.image.load("RES/Bonus_speed.png"), (50, 50))
        self.bonus = pygame.Rect(self.position_x, self.position_y, 50, 50)
        self.type = bonus_type
        self.time = time.time()

    def update(self):
        t = time.time()
        if t - self.time < 3:
            if self.type == 2:
                self.window.blit(self.life, (self.position_x, self.position_y))
            if self.type == 4:
                self.window.blit(self.speed, (self.position_x, self.position_y))
