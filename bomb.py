import pygame
import time


class Bomb:
    def __init__(self, window, x, y, map1):
        self.image = pygame.transform.scale(pygame.image.load("RES/NeoBigBomb.gif"), (50, 50))
        self.explosion_center_image = pygame.transform.scale(pygame.image.load("RES/explosion_center.png"), (50, 50))
        self.explosion_up_image = pygame.transform.scale(pygame.image.load("RES/explosion_up.png"), (50, 50))
        self.explosion_down_image = pygame.transform.scale(pygame.image.load("RES/explosion_down.png"), (50, 50))
        self.explosion_left_image = pygame.transform.scale(pygame.image.load("RES/explosion_left.png"), (50, 50))
        self.explosion_right_image = pygame.transform.scale(pygame.image.load("RES/explosion_right.png"), (50, 50))

        self.position = pygame.Rect(x - x % 50, y - y % 50, 50, 50)
        self.window = window
        self.window.blit(self.image, (self.position.x, self.position.y))
        self.time = time.time()
        self.map = map1
        self.player_exploded = 0
        self.exploded = False
        self.add_once = False
        self.bonus = None

    def update(self):
        if not self.exploded:
            self.window.blit(self.image, (self.position.x, self.position.y))
            t = time.time()
            if t - self.time > 1:
                if not self.add_once:
                    self.get_points()
                    self.add_once = True
                self.explode()
            if t - self.time > 1.2:
                self.end_explosion()

    def explode(self):
        self.window.blit(self.explosion_center_image, (self.position.x, self.position.y))

        if not self.map.is_collision(pygame.Rect(self.position.x + 50, self.position.y, 50, 50)):
            self.window.blit(self.explosion_right_image, (self.position.x + 50, self.position.y))

        if not self.map.is_collision(pygame.Rect(self.position.x - 50, self.position.y, 50, 50)):
            self.window.blit(self.explosion_left_image, (self.position.x - 50, self.position.y))

        if not self.map.is_collision(pygame.Rect(self.position.x, self.position.y + 50, 50, 50)):
            self.window.blit(self.explosion_down_image, (self.position.x, self.position.y + 50))

        if not self.map.is_collision(pygame.Rect(self.position.x, self.position.y - 50, 50, 50)):
            self.window.blit(self.explosion_up_image, (self.position.x, self.position.y - 50))

    def get_points(self):
        if self.map.player1.bombs:
            if self.position.colliderect(self.map.player2.position) or \
                    pygame.Rect(self.position.x + 50, self.position.y, 50, 50).colliderect(self.map.player2.position) or \
                    pygame.Rect(self.position.x - 50, self.position.y, 50, 50).colliderect(self.map.player2.position) or \
                    pygame.Rect(self.position.x, self.position.y + 50, 50, 50).colliderect(self.map.player2.position) or \
                    pygame.Rect(self.position.x, self.position.y - 50, 50, 50).colliderect(self.map.player2.position):
                self.player_exploded += 1

        if self.map.player2.bombs:
            if self.position.colliderect(self.map.player1.position) or \
                    pygame.Rect(self.position.x + 50, self.position.y, 50, 50).colliderect(self.map.player1.position) or \
                    pygame.Rect(self.position.x - 50, self.position.y, 50, 50).colliderect(self.map.player1.position) or \
                    pygame.Rect(self.position.x, self.position.y + 50, 50, 50).colliderect(self.map.player1.position) or \
                    pygame.Rect(self.position.x, self.position.y - 50, 50, 50).colliderect(self.map.player1.position):
                self.player_exploded += 1

    def get_damage(self):
        if self.position.colliderect(self.map.player2.position) or \
                pygame.Rect(self.position.x + 50, self.position.y, 50, 50).colliderect(self.map.player2.position) or \
                pygame.Rect(self.position.x - 50, self.position.y, 50, 50).colliderect(self.map.player2.position) or \
                pygame.Rect(self.position.x, self.position.y + 50, 50, 50).colliderect(self.map.player2.position) or \
                pygame.Rect(self.position.x, self.position.y - 50, 50, 50).colliderect(self.map.player2.position):
            self.map.player2.current_hp -= 30

        if self.position.colliderect(self.map.player1.position) or \
                pygame.Rect(self.position.x + 50, self.position.y, 50, 50).colliderect(self.map.player1.position) or \
                pygame.Rect(self.position.x - 50, self.position.y, 50, 50).colliderect(self.map.player1.position) or \
                pygame.Rect(self.position.x, self.position.y + 50, 50, 50).colliderect(self.map.player1.position) or \
                pygame.Rect(self.position.x, self.position.y - 50, 50, 50).colliderect(self.map.player1.position):
            self.map.player1.current_hp -= 30

    def end_explosion(self):
        self.exploded = True
