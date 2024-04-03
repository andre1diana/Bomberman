from block import Block
from bricks import Bricks
from bonus import Bonus
import random

GREEN = (51, 255, 153)

'''1 - unbreakable block
   2 - breakable brick
   3 - initial player position
   4 - bonus '''


class Map:
    def __init__(self, window, filename):
        with open(filename, "r") as f:
            self.map = [[int(x) for x in line.split()] for line in f]
        self.window = window
        self.blocks = []
        self.window.fill(GREEN)
        self.player1_x = 0  # player position
        self.player1_y = 0
        self.player2_x = 0
        self.player2_y = 0
        self.player1 = None
        self.player2 = None
        self.bonuses = []

    def player_position(self):
        while True:
            position1_x = random.randint(2, 12)
            position1_y = random.randint(1, 13)
            if self.map[position1_x][position1_y] == 0:
                if self.map[position1_x - 1][position1_y] == 0 and \
                        self.map[position1_x + 1][position1_y] == 0 and \
                        self.map[position1_x][position1_y - 1] == 0 and \
                        self.map[position1_x][position1_y + 1] == 0:
                    self.map[position1_x][position1_y] = 3
                    self.player1_y = position1_x * 50
                    self.player1_x = position1_y * 50
                    break

        while True:
            position2_x = random.randint(2, 12)
            position2_y = random.randint(1, 13)
            if self.map[position2_x][position2_y] == 0 and \
                    self.map[position2_x - 1][position2_y] == 0 and \
                    self.map[position2_x + 1][position2_y] == 0 and \
                    self.map[position2_x][position2_y - 1] == 0 and \
                    self.map[position2_x][position2_y + 1] == 0:
                self.map[position2_x][position2_y] = 3
                self.player2_y = position2_x * 50
                self.player2_x = position2_y * 50
                return

    def generate_bricks(self):
        i = 0
        while i < 90:
            random_position_x = random.randint(2, 12)
            random_position_y = random.randint(1, 13)
            if self.map[random_position_x][random_position_y] == 0 and \
                    self.map[random_position_x - 1][random_position_y] != 3 and \
                    self.map[random_position_x + 1][random_position_y] != 3 and \
                    self.map[random_position_x][random_position_y - 1] != 3 and \
                    self.map[random_position_x][random_position_y + 1] != 3:
                self.map[random_position_x][random_position_y] = 2
                i += 1

    def draw_map(self):
        self.player_position()
        self.generate_bricks()
        for i in range(1, 14):
            for j in range(0, 15):
                if self.map[i][j] == 1:
                    self.blocks.append(Block(self.window, j * 50, i * 50))
                if self.map[i][j] == 2:
                    self.blocks.append(Bricks(self.window, j * 50, i * 50))

    def update(self):
        self.window.fill(GREEN)
        for b in self.blocks:
            b.update()
        for b in self.bonuses:
            b.update()

    def is_collision(self, rect):
        for b in self.blocks:
            if b.position.colliderect(rect):
                if type(b) is Bricks:
                    self.blocks.remove(b)
                    self.add_bonus(b.position)
                    return False

                return True
        return False

    def add_players(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def add_bonus(self, position):
        rand = random.randint(1, 10)
        self.bonuses.append(Bonus(self.window, position.x, position.y, rand))
        if self.bonuses:
            self.map[int(position.x / 50)][int(position.y / 50)] = 4
