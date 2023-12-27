import pygame
from Specification import *

class Wumpus:
    def __init__(self, x, y):
        self.image = pygame.image.load(IMG_WUMPUS).convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 200))
        self.size = 10
        self.pos = (835, 100)
        self.is_discovered = None
        self.noti = [[False for i in range(self.size)] for j in range(self.size)]
        self.wumpus_pos = [[False for i in range(self.size)] for j in range(self.size)]
        for i in range(len(x)):
            self.wumpus_pos[x[i]][y[i]] = True

    def wumpus_kill(self, screen, font):
        text = font.render('Killed a wumpus!!!', True, WHITE)
        textRect = text.get_rect()
        textRect.center = self.pos
        screen.blit(text, textRect)
        screen.blit(self.image, (755, 200))
        pygame.display.update()

    def wumpus_notification(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.wumpus_pos[i][j]:
                    if i > 0:
                        self.noti[i - 1][j] = True
                    if i < self.size - 1:
                        self.noti[i + 1][j] = True
                    if j > 0:
                        self.noti[i][j - 1] = True
                    if j < self.size - 1:
                        self.noti[i][j + 1] = True

    def wumpus_killed(self, i, j):
        self.wumpus_pos[i][j] = False
        if i > 0:
            self.noti[i-1][j] = False
        if i < self.size - 1:
            self.noti[i+1][j] = False
        if j > 0:
            self.noti[i][j - 1] = False
        if j < self.size - 1:
            self.noti[i][j + 1] = False

    def update(self, screen, font, is_discovered):
        for i in range(self.size):
            for j in range (self.size):
                if self.noti[i][j] and is_discovered[i][j]:
                    text = font.render('Stench', True, BLACK)
                    textRect = text.get_rect()
                    textRect.center = (45 + j * 70, 30 + i * 70)
                    screen.blit(text, textRect)
                    pygame.display.update()

    def stench_i_j(self, i, j):
        return self.noti[i][j]

