import pygame
import random
import sys


GRID_SIZE = 50
MOVE_SPEED = 10


class Snake:
    def __init__(self, surface) -> None:
        self.surface = surface
        self.snake_pos = [(0, 0)]
        self.apple_eat = False

        self.snake_grid_size = GRID_SIZE

        self.timer = MOVE_SPEED

        self.movement = {
            "left": (-1, 0),
            "right": (1, 0),
            "up": (0, -1),
            "down": (0, 1),
        }

        self.move_pos = self.movement["right"]
        self.past_head = ()

        self.snake_size = 0

    def move(self, direction):
        self.move_pos = self.movement[direction]

        self.past_head = self.snake_pos[self.snake_size]

        if self.timer:
            self.timer -= 1
        else:
            self.timer = MOVE_SPEED

            if len(self.snake_pos) > 0:
                for x in range(0, self.snake_size):
                    self.snake_pos[x] = self.snake_pos[x + 1]

            self.snake_pos[self.snake_size] = (self.snake_pos[self.snake_size][0] + self.move_pos[0], self.snake_pos[self.snake_size][1] + self.move_pos[1])

    def check(self, apple_pos) -> None:
        self.apple_eat = False

        if self.snake_pos[self.snake_size] == apple_pos:
            self.apple_eat = True
            self.snake_pos.append(apple_pos)
            self.snake_pos[self.snake_size] = ((self.snake_pos[self.snake_size][0] + (-self.move_pos[0]), self.snake_pos[self.snake_size][1] + (-self.move_pos[1])))
            self.snake_size += 1

        for x in range(0, self.snake_size):
            if self.snake_pos[self.snake_size] == self.snake_pos[x]:
                pygame.quit()
                sys.exit()
        
        for x in range(0, self.snake_size + 1):
            if self.snake_pos[x][0] == -1:
                self.snake_pos[x] = (15, self.snake_pos[x][1])
            if self.snake_pos[x][0] == 16:
                self.snake_pos[x] = (0, self.snake_pos[x][1])
            if self.snake_pos[x][1] == -1:
                self.snake_pos[x] = (self.snake_pos[x][0], 11)
            if self.snake_pos[x][1] == 12:
                self.snake_pos[x] = (self.snake_pos[x][0], 0)

    def render(self) -> None:
        for pos in self.snake_pos:
            pygame.draw.rect(self.surface, "white", pygame.Rect(pos[0] * self.snake_grid_size + 1, pos[1] * self.snake_grid_size + 1, self.snake_grid_size - 1, self.snake_grid_size - 1))

    def apple_has_eaten (self) -> bool:
        return self.apple_eat


class Apple:
    def __init__(self, surface):
        self.surface = surface
        self.pos_apple = (random.randint(0, 15), random.randint(0, 11))
        self.grid_size = GRID_SIZE

    def render(self, apple_eaten: bool):
        if apple_eaten:
            self.pos_apple = (random.randint(0, 15), random.randint(0, 11))
        
        pygame.draw.rect(self.surface, "red", pygame.Rect(self.pos_apple[0] * self.grid_size, self.pos_apple[1] * self.grid_size, self.grid_size, self.grid_size))


    def apple_pos(self):
        return self.pos_apple

