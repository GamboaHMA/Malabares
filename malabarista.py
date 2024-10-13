import pygame
from pygame.sprite import Group
from settings import *

class Malabarista(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/malabarista.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

# inicio brazo izquierdo 476, 348 final 434, 441
# inicio brazo derecho   818, 348 final 864, 441