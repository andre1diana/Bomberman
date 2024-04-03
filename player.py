import pygame
import time
from score import Score
from bomb import Bomb
from utils import Keys

RED = (204, 0, 0)
BLUE = (0, 128, 255)

pygame.mixer.init()
put_bomb_sound = pygame.mixer.Sound('RES/Put_bomb.wav')
explode_bomb_sound = pygame.mixer.Sound('RES/explode_bomb.wav')


class Player:
    def __init__(self, window, map1, image, startX, startY, number):
        self.image = pygame.transform.scale(pygame.image.load(image), (45, 45))
        self.position = pygame.Rect(startX, startY, 50, 50)
        self.velocity = 5
        self.window = window
        self.map = map1
        if number == 1:
            self.score = Score(self.window, 'Player' + str(number), 10, 0, RED)
        else:
            self.score = Score(self.window, 'Player' + str(number), 10, 20, BLUE)
        self.bombs = []
        self.max_bombs = 1
        self.number = number
        self.hp = 90
        self.current_hp = 90
        self.time = time.time()

    def update(self):
        self.window.blit(self.image, (self.position.x, self.position.y))
        self.score.update()
        if self.number == 1:
            self.draw_health_bar(150, 0, 100, 15)
        if self.number == 2:
            self.draw_health_bar(150, 20, 100, 15)
        for b in self.bombs:
            b.update()
            if b.exploded:
                explode_bomb_sound.play()
                self.bombs.remove(b)
                self.score.add_score(b.player_exploded)
                b.get_damage()
        for b in self.map.bonuses:
            if self.position.colliderect(b.bonus):
                t = time.time()
                self.get_bonus(b, t)

    def player_handle_movement(self, keys_pressed):
        old_rect = self.position.copy()  # without copy takes only reference
        new_rect = self.position.copy()
        controls = Keys(self.number)

        if keys_pressed[controls.left]:  # left
            new_rect.x -= self.velocity
            if new_rect.y % 50 <= 20:
                new_rect.y = new_rect.y - new_rect.y % 50
            if new_rect.y % 50 >= 30:
                new_rect.y = new_rect.y - new_rect.y % 50 + 50

        if keys_pressed[controls.right]:  # right
            new_rect.x += self.velocity
            if new_rect.y % 50 <= 20:
                new_rect.y = new_rect.y - new_rect.y % 50
            if new_rect.y % 50 >= 30:
                new_rect.y = new_rect.y - new_rect.y % 50 + 50

        if keys_pressed[controls.up]:  # up
            new_rect.y -= self.velocity
            if new_rect.x % 50 <= 20:
                new_rect.x = new_rect.x - new_rect.x % 50
            if new_rect.x % 50 >= 30:
                new_rect.x = new_rect.x - new_rect.x % 50 + 50

        if keys_pressed[controls.down]:  # down
            new_rect.y += self.velocity
            if new_rect.x % 50 <= 20:
                new_rect.x = new_rect.x - new_rect.x % 50
            if new_rect.x % 50 >= 30:
                new_rect.x = new_rect.x - new_rect.x % 50 + 50

        if keys_pressed[controls.bomb]:  # bomb
            self.put_bomb()
        self.collide(old_rect, new_rect)

    def collide(self, old_rect, new_rect):
        for b in self.map.blocks:
            if new_rect.colliderect(b.position):
                self.position = old_rect
                return
        self.position = new_rect

    def put_bomb(self):
        if len(self.bombs) < self.max_bombs:
            put_bomb_sound.play()
            self.bombs.append(Bomb(self.window, self.position.x, self.position.y, self.map))

    def draw_health_bar(self, x, y, width, height):
        health_length = int((self.current_hp/self.hp) * width)
        if self.number == 1:
            pygame.draw.rect(self.window, (0, 0, 0), (x, y, width, height))
            pygame.draw.rect(self.window, RED, (x, y, health_length, height))
        else:
            pygame.draw.rect(self.window, (0, 0, 0), (x, y, width, height))
            pygame.draw.rect(self.window, BLUE, (x, y, health_length, height))

    def get_bonus(self, b, t):
        if b.type == 2:
            self.map.bonuses.remove(b)
            if self.current_hp < 90:
                self.current_hp += 30
        if b.type == 4:
            self.map.bonuses.remove(b)
            if t - self.time < 10:
                self.velocity = 10
            else:
                self.velocity = 5
