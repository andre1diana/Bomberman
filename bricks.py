import pygame


class Bricks:
    def __init__(self, window, x, y):
        self.image = pygame.transform.scale(pygame.image.load("RES/destructibleBlocks.png"), (50, 50))
        self.position = pygame.Rect(x, y, 50, 50)
        self.window = window
        self.is_destroyed = False
        self.window.blit(self.image, (self.position.x, self.position.y))

    # def destroy(self):
    #     self.is_destroyed = True
    #     self.window.blit(self.image, (self.position.x, self.position.y))
    #     self.image.fill((0, 0, 0, 0))

    def update(self):
        self.window.blit(self.image, (self.position.x, self.position.y))
