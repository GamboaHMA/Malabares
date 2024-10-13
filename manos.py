import pygame
from pygame.sprite import Group
from settings import *

blanco = (255, 255, 255)

class Mano(pygame.sprite.Sprite):
    def __init__(self, inicio, final, recorrido): # conjunto de puntos por los que recorrera la mano
        super().__init__()
        self.inicio = inicio
        self.final = final
        self.pos = final
        self.index = 0
        self.index_recorrido = 0
        self.index_speed = 0
        self.recorrido = recorrido
        self.index_inicio = 0
        self.iniciado = False

        self.derecha = True
        self.izquierda = False
    
    def update(self, speed=[]):
        #if self.index + speed >= len(self.recorrido):
        #    self.index = 0
        #    self.pos = self.recorrido[self.index]
        #else:
        #    self.index += speed
        #    self.pos = self.recorrido[self.index]

        if not self.iniciado:
            if self.index >= self.index_inicio:
                self.iniciado = True
        
        if self.iniciado:
            if self.index_recorrido >= len(self.recorrido):
                self.index_recorrido = 0
                if self.index_speed >= len(speed):
                    self.index_speed = 0
                self.pos = self.recorrido[self.index_recorrido]
            if self.index_speed >= len(speed):
                self.index_speed = 0
            self.pos = self.recorrido[self.index_recorrido]
            self.index_recorrido += speed[self.index_speed]
            self.index_speed += 1

        self.index += 1
        

    def draw(self, surface):
        # dibujar linea
        pygame.draw.line(surface, blanco, self.inicio, self.pos, 4)
    
        
