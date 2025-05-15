import pygame
import sys
import random
from Scripts.GameManager import Snake, Apple


class Game:
    def __init__(self) -> None:
        pygame.init()

        self.screen = (800, 600)

        self.surface = pygame.display.set_mode(self.screen)
        self.clock = pygame.time.Clock()

        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)

        self.movement = "right"

    def run(self) -> None:
        while True:
            self.surface.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()  
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        if self.movement != "right":
                            self.movement = "left"
                    if event.key == pygame.K_s:
                        if self.movement != "up":
                            self.movement = "down"
                    if event.key == pygame.K_d:
                        if self.movement != "left":
                            self.movement = "right"
                    if event.key == pygame.K_w:
                        if self.movement != "down":
                            self.movement = "up"

            
            self.snake.move(self.movement)
            self.snake.check(self.apple.apple_pos())
            self.snake.render()

            self.apple.render(self.snake.apple_has_eaten())

            pygame.display.update()
            self.clock.tick(60)
            

Game().run()

