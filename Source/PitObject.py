

import pygame
from Specification import *
class Pit:
    def __init__(self, x, y):
        self.is_discovered = None
        self.size = 10
        self.noti = [[False for i in range(self.size)] for j in range(self.size)]
        self.pit_pos = [[False for i in range(self.size)] for j in range(self.size)]
        for i in range(len(x)):
            self.pit_pos[x[i]][y[i]] = True

    def pit_discovered(self):
        self.is_discovered = True

    def pit_notification(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.pit_pos[i][j]:
                    if i > 0:
                        self.noti[i - 1][j] = True
                    if i < self.size - 1:
                        self.noti[i + 1][j] = True
                    if j > 0:
                        self.noti[i][j - 1] = True
                    if j < self.size - 1:
                        self.noti[i][j + 1] = True

    def update(self, screen, font, is_discovered):
        for i in range(self.size):
            for j in range (self.size):
                if self.noti[i][j] and is_discovered[i][j]:
                    text = font.render('Breeze', True, BLACK)
                    textRect = text.get_rect()
                    textRect.center = (42 + j * 70, 40 + i * 70)
                    screen.blit(text, textRect)
                    pygame.display.update()