import pygame
from malabarista import Malabarista
from settings import *
from manos import *

class Level():
    def __init__(self):
        
        # get display surface
        self.display_surface = pygame.display.get_surface()
        
        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

    def create_map(self):

        Malabarista((544, 250), [self.visible_sprites])
        #brazo1 = Mano((550, 382), (528, 452), [(528, 452)])
        #brazo2 = Mano((765, 382), (790, 452), [(790, 452)])
        mano1 = Mano((528, 452),(550, 529), [(550, 529)])
        mano2 = Mano((790, 452),(765, 529), [(765, 529)])

        #self.visible_sprites.add(brazo1)
        #self.visible_sprites.add(brazo2)


    def run(self):
        # update ando draw the game
        self.visible_sprites.update()

        for sprite in self.visible_sprites:
            if isinstance(sprite, Mano):
                sprite.draw(self.display_surface)
            else:
                self.display_surface.blit(sprite.image, sprite.rect)
