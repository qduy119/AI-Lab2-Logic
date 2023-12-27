import pygame
from Specification import *

class Gold:
    def __init__(self):
        self.image = pygame.image.load(IMG_GOLD).convert()
        self.image = pygame.transform.scale(self.image, (150,300))
        self.pos = (835, 100)

    def grab_gold(self, screen, font):
        text = font.render('Find a chest!!!', True, BLACK)
        textRect = text.get_rect()
        textRect.center = self.pos
        screen.blit(text, textRect)
        screen.blit(self.image, (750, 200))
        text = font.render('Score + 100', True, BLACK)
        textRect.center = (850, 600)
        screen.blit(text, textRect)
        pygame.display.update()

