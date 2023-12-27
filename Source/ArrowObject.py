import pygame
from Specification import *

class Arrow:
    def __init__(self):
        self.img_list = []
        temp = [IMG_ARROW_RIGHT, IMG_ARROW_LEFT, IMG_ARROW_UP, IMG_ARROW_DOWN]
        for i in range(0, 4):
            img = pygame.image.load(temp[i]).convert()
            self.img_list.append(img)

    def ShootDown(self, screen, x, y):
        i = 10 + x * 70
        j = 10 + (y + 1) * 70
        screen.blit(self.img_list[3], (i, j))
        pygame.display.update()

    def ShootLeft(self, screen, x, y):
        x = 10 + (x - 1) * 70
        y = 10 + y * 70
        screen.blit(self.img_list[1], (x, y))
        pygame.display.update()

    def ShootUp(self, screen, x, y):
        x = 10 + x * 70
        y = 10 + (y - 1) * 70
        screen.blit(self.img_list[2], (x, y))
        pygame.display.update()

    def ShootRight(self, screen, x, y):
        x = 10 + (x + 1) * 70
        y = 10 + y * 70
        screen.blit(self.img_list[0], (x, y))
        pygame.display.update()

    def Shoot(self, direct, screen, y, x):
        if direct == 0:
            self.ShootUp(screen, x, y)
        elif direct == 1:
            self.ShootDown(screen, x, y)
        elif direct == 2:
            self.ShootLeft(screen, x, y)
        elif direct == 3:
            self.ShootRight(screen, x, y)

