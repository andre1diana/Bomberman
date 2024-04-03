import pygame


class Block:
    def __init__(self, window, x, y):
        self.image = pygame.transform.scale(pygame.image.load("RES/bloc1.png"), (50, 50))
        self.position = pygame.Rect(x, y, 50, 50)
        self.window = window
        self.window.blit(self.image, (self.position.x, self.position.y))

    def update(self):
        self.window.blit(self.image, (self.position.x, self.position.y))
