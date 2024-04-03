import pygame


class Keys:
    def __init__(self, no_player):
        self.number = no_player
        if self.number == 1:
            self.up = pygame.K_w
            self.down = pygame.K_s
            self.left = pygame.K_a
            self.right = pygame.K_d
            self.bomb = pygame.K_q
        if self.number == 2:
            self.up = pygame.K_UP
            self.down = pygame.K_DOWN
            self.left = pygame.K_LEFT
            self.right = pygame.K_RIGHT
            self.bomb = pygame.K_RSHIFT
