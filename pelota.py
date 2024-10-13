import pygame
from pygame.sprite import Group
from settings import *
from parabola import *

blanco = (255, 255, 255)
azul = (0, 255, 255)
verde = (100, 255, 200)

class Pelota(pygame.sprite.Sprite):
    def __init__(self, pos, radio, color, recorrido):  # recorrido es un array de curvas, las cuales concatenadas formaran el recorrido de la pelota
        self.pos = pos
        self.index = 0
        self.index_speed = 0
        self.index_recorrido = 0
        self.index_inicio = 0
        self.radio = radio
        self.color = color
        self.recorrido = recorrido
        self.iniciado = False
    
    def update(self, speed):
        if not self.iniciado:
            if self.index >= self.index_inicio:
                self.iniciado = True
                
        if self.iniciado:
            if self.index_recorrido >= len(self.recorrido):
                self.index_speed = 0
                self.index_recorrido = 0
                self.pos = self.recorrido[speed[self.index_speed]]
            self.pos = self.recorrido[self.index_recorrido]
            self.index_recorrido += speed[self.index_speed]
            self.index_speed += 1
        
        self.index += 1

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.radio)

    


#curva1 = Arco()

        

# inicio arco_izquierda_derecha (570, 500)
# final  arco_izquierda_derecha (840, 500)