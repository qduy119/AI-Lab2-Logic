import pygame
from Specification import *

class Arrow:
    def __init__(self):
        self.img_list = []
        temp = [IMG_ARROW_RIGHT, IMG_ARROW_LEFT, IMG_ARROW_UP, IMG_ARROW_DOWN]
        for i in range(0, 4):
            img = pygame.image.load(temp[i]).convert()
            self.img_list.append(img)

    def shoot(self, direct, screen, y, x):
        if direct == 0:
            self.shoot_up(screen, x, y)
        elif direct == 1:
            self.shoot_down(screen, x, y)
        elif direct == 2:
            self.shoot_left(screen, x, y)
        elif direct == 3:
            self.shoot_right(screen, x, y)

    def shoot_right(self, screen, x, y):
        x = 10 + (x + 1) * 70
        y = 10 + y * 70
        screen.blit(self.img_list[0], (x, y))
        pygame.display.update()

    def shoot_left(self, screen, x, y):
        x = 10 + (x - 1) * 70
        y = 10 + y * 70
        screen.blit(self.img_list[1], (x, y))
        pygame.display.update()

    def shoot_up(self, screen, x, y):
        x = 10 + x * 70
        y = 10 + (y - 1) * 70
        screen.blit(self.img_list[2], (x, y))
        pygame.display.update()

    def shoot_down(self, screen, x, y):
        i = 10 + x * 70
        j = 10 + (y + 1) * 70
        screen.blit(self.img_list[3], (i, j))
        pygame.display.update()

