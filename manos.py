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
    

class Manos(pygame.sprite.Sprite):
    def __init__(self, inicio1, inicio2, final1, final2, recorrido1, recorrido2):
        super().__init__()
        
        # mano 1
        self.inicio1 = inicio1
        self.final1 = final1
        self.recorrido1 = recorrido1
        self.pos1 = final1
        self.index1 = 0
        self.index_recorrido1 = 0
        self.index_speed1 = 0
        self.index_inicio1 = 0
 
        # mano 2
        self.inicio2 = inicio2
        self.final2 = final2
        self.recorrido2 = recorrido2
        self.pos2 = final2
        self.index2 = 0
        self.index_recorrido2 = 0
        self.index_speed2 = 0
        self.index_inicio2 = 0
