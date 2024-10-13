import pygame
from manos import *
from parabola import *
from pelota import *

class Malabar():
    def __init__(self, manos, puntos_de_recorrido, pelota:Pelota, totalPelotas=1):
        self.mano1:Mano = manos[0]
        self.mano2:Mano = manos[1]
        self.puntos_de_recorrido = puntos_de_recorrido
        pelota.index_inicio = 0
        self.pelotas = []
        self.pos_actual = 0
        self.totalPelotas = totalPelotas

        rango_entre_pelotas = int(len(pelota.recorrido)/ 4 / totalPelotas)
        resto_de_rango_entre_pelotas = len(pelota.recorrido) % totalPelotas

        for i in range(totalPelotas):
            new_pelota = Pelota(pelota.pos, pelota.radio, pelota.color, pelota.recorrido)
            new_pelota.index_inicio = i * rango_entre_pelotas + resto_de_rango_entre_pelotas
            self.pelotas.append(new_pelota)
    

    def update(self, excedente_pelota=0, excedente_mano=0):
        for i in range(len(self.pelotas)):
            speed_pelota = calcularArrayDeSpeedsPelota(self.pelotas[i])
            self.pelotas[i].update(speed=speed_pelota)   
            speed_mano = calcularArrayDeSpeedsMano(self.pelotas[i], self.mano1, self.totalPelotas) 
            self.mano1.update(speed=speed_mano)
            #self.mano2.update(speed=4, excedente=excedente_mano)     

    def draw(self, surface):
        self.mano1.draw(surface)
        self.mano2.draw(surface)

        for i in range(len(self.pelotas)):
            self.pelotas[i].draw(surface)





def calcularArrayDeSpeedsPelota(pelota:Pelota=None, mano=None):
    total = len(pelota.recorrido)
    resto = total % 4 
    result = []
    rango = int(total/4)
    for i in range(rango):
        if i + 1 >= rango:
            result.append(4 + resto)
        else:
            result.append(4)
    return result
    
def calcularArrayDeSpeedsMano(pelota:Pelota, mano:Mano, totalPelotas):
    total_iteraciones_pelota = int(len(pelota.recorrido)/4) # 185
    puntos_totales_mano = len(mano.recorrido) # 160
    iter_entre_cada_pelota = int(total_iteraciones_pelota) # 185 / 3 = 61
    resto_iter_entre_cada_pelota = total_iteraciones_pelota % totalPelotas # resto 2
    rest_resto_iter_entre_cada_pelota = resto_iter_entre_cada_pelota
    velocidad = int((puntos_totales_mano / iter_entre_cada_pelota))
    resto_velocidad = puntos_totales_mano % iter_entre_cada_pelota # 38
    resto_resto_velocidad = resto_velocidad

    result = []
    
    for i in range(total_iteraciones_pelota):
        if rest_resto_iter_entre_cada_pelota > 0:
            result.append(0)
            rest_resto_iter_entre_cada_pelota -= 1
        else:
            resto = (i - resto_iter_entre_cada_pelota) % iter_entre_cada_pelota
            if resto == 0:
                resto_resto_velocidad = resto_velocidad
            if resto_resto_velocidad > 0:
                result.append(velocidad + 1)
                resto_resto_velocidad -= 1
            else:
                result.append(velocidad)

    return result




