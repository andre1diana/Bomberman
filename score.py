import pygame


class Score:
    def __init__(self, window, name, x, y, color):
        self.name_player = name
        self.window = window
        self.score = 0
        self.font = pygame.font.SysFont('Comic Sans MS', 18)
        self.x = x
        self.y = y
        self.color = color

    def add_score(self, x):
        self.score += x

    def update(self):
        surface = self.font.render(str(self.name_player) + ': ' + str(self.score), False, self.color)
        self.window.blit(surface, (self.x, self.y))
