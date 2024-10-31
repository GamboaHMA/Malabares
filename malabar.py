import pygame
from manos import *
from manos import Mano
from parabola import *
from pelota import *
from pelota import Pelota
from abc import ABC, abstractmethod

class Malabar(ABC):
    def __init__(self):
        self.is_activate = False
        self.pelotas_totalPelotas_manos()
        self.indice_inicial_pelota_mano(self.pelota, self.totalPelotas)        


    @abstractmethod
    def pelotas_totalPelotas_manos(self):
        pass    
    
    @abstractmethod
    def indice_inicial_pelota_mano(self, pelota, totalPelotas):
        pass
    

    def update(self):
        if self.is_activate:
            for i in range(len(self.pelotas)):
                speed_pelota = self.calcularArrayDeSpeedsPelota(self.pelotas[i])
                self.pelotas[i].update(speed=speed_pelota)   
                speed_mano = self.calcularArrayDeSpeedsMano(self.pelotas[i], self.mano1, self.totalPelotas) 
                self.mano1.update(speed=speed_mano)
                self.mano2.update(speed=speed_mano)  
        else:
            self.pelotas_totalPelotas_manos()
            self.indice_inicial_pelota_mano(self.pelota, self.totalPelotas)   

    def draw(self, surface):
        if self.is_activate:
            self.mano1.draw(surface)
            self.mano2.draw(surface)

            for i in range(len(self.pelotas)):
                self.pelotas[i].draw(surface)


    @abstractmethod
    def calcularArrayDeSpeedsPelota(pelota:Pelota=None, mano=None):
        pass

    @abstractmethod
    def calcularArrayDeSpeedsMano(pelota:Pelota, mano:Mano, totalPelotas):
        pass



class Cascade3(Malabar):
    def __init__(self):
        super().__init__()

    def pelotas_totalPelotas_manos(self):
        parabola_izq_der1 = Parabola((620, 140), 0.01, 0, (-145, 145))
        inicio_de_par_izq_der2 = parabola_izq_der1.points[len(parabola_izq_der1.points)-1]
        centro_par_izq_der2 = (inicio_de_par_izq_der2[0] + 40, inicio_de_par_izq_der2[1] + 30)
        parabola_izq_der2 = Parabola(centro_par_izq_der2, 0.01, 0, (-40, 40), inversa=True)
        parabola_izq_der3 = Parabola((700, 140), 0.01, 0, (-145, 145))
        inicio_de_par_izq_der4 = parabola_izq_der1.points[0]
        centro_par_izq_der4 = (inicio_de_par_izq_der4[0] + 40, inicio_de_par_izq_der4[1] + 30)
        parabola_izq_der4 = Parabola(centro_par_izq_der4, 0.01, 0, (-40, 40), inversa=True)

        mano1_parabola = Parabola((centro_par_izq_der4[0], centro_par_izq_der4[1] - 50), 0.01, 0, (-40, 40))
        mano2_parabola = Parabola((centro_par_izq_der2[0], centro_par_izq_der2[1] - 50), 0.01, 0, (-40, 40))

        recorrido = [
             (parabola_izq_der1, False),
             (parabola_izq_der4, True),
             (parabola_izq_der3, True),
             (parabola_izq_der2, False),
             ]
        
        mano1_recorrido = parabola_izq_der1.puntosDeRecorrido([(parabola_izq_der4, True), (mano1_parabola, False)], malabar='cascada3')
        mano2_recorrido = parabola_izq_der1.puntosDeRecorrido([(parabola_izq_der2, False), (mano2_parabola, True)], malabar='cascada3')

        puntos_de_recorrido = parabola_izq_der1.puntosDeRecorrido(recorrido=recorrido, malabar='cascada3')

        self.mano1 = Mano((528, 452),(550, 529), mano1_recorrido)
        self.mano2 = Mano((790, 452),(765, 529), mano2_recorrido)
        self.pelota = Pelota((-25, -25), 25, azul, puntos_de_recorrido)
        self.pelotas = []
        self.pos_actual = 0
        self.pelota.index_inicio = 0
        self.totalPelotas = 3


    def indice_inicial_pelota_mano(self, pelota, totalPelotas):
        rango_entre_pelotas = int(len(pelota.recorrido)/ 4 / totalPelotas)
        resto_de_rango_entre_pelotas = len(pelota.recorrido) % totalPelotas

        for i in range(totalPelotas):
            new_pelota = Pelota(pelota.pos, pelota.radio, pelota.color, pelota.recorrido)
            new_pelota.index_inicio = i * rango_entre_pelotas + resto_de_rango_entre_pelotas + (rango_entre_pelotas) // 2
            self.pelotas.append(new_pelota)

        self.mano2.index_inicio = 0
        self.mano1.index_inicio = 5*rango_entre_pelotas


    def calcularArrayDeSpeedsPelota(self, pelota: Pelota = None, mano=None):
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

    
    def calcularArrayDeSpeedsMano(self, pelota: Pelota, mano: Mano, totalPelotas):
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
        #for i in range(total_iteraciones_pelota):
        #    if i >= puntos_totales_mano:
        #        result.append(velocidad)
        #    else:
        #        result.append(velocidad + 1)

        return result


class Cascade4(Malabar):
    def __init__(self):
        super().__init__()

    def pelotas_totalPelotas_manos(self):
        parab_izq_der1 = Parabola((centro_par_izq_der2[0], centro_par_izq_der2[1] - 400), 0.01, 0, (-48, 48), mod1=16)
        parab_izq_der2 = Parabola(centro_par_izq_der2, 0.01, 0, (-40, 40), inversa=True)
        mano2_parabola = Parabola((centro_par_izq_der2[0], centro_par_izq_der2[1] - 50), 0.01, 0, (-40, 40))

        pelota1_recorrido = parab_izq_der1.puntosDeRecorrido([(parab_izq_der1, True),(parab_izq_der2, False)])

        mano2_recorrido = parab_izq_der1.puntosDeRecorrido([(mano2_parabola, True), (parab_izq_der2, False)])

        parab_der_izq1 = Parabola((centro_par_izq_der2[0] - 285, centro_par_izq_der2[1] - 400), 0.01, 0, (-48, 48), mod1=16)
        parab_der_izq2 = Parabola(centro_par_izq_der4, 0.01, 0, (-40, 40), inversa=True)
        mano1_parabola = Parabola((centro_par_izq_der2[0] - 285, centro_par_izq_der2[1] - 50), 0.01, 0, (-40, 40))

        pelota2_recorrido = parab_izq_der1.puntosDeRecorrido([(parab_der_izq1, False), (parab_der_izq2, True)])

        mano1_recorrido = parab_izq_der1.puntosDeRecorrido([(mano1_parabola, False),(parab_der_izq2, True)])

        self.mano1 = Mano((528, 452),(550, 529), mano1_recorrido)
        self.mano2 = Mano((790, 452),(765, 529), mano2_recorrido)
        self.pelota = Pelota((-25,-25), 25, azul, pelota1_recorrido)   # solo para cumplir con el prototipo
        self.pelota1 = Pelota((-25,-25), 25, azul, pelota1_recorrido)
        self.pelota2 = Pelota((-25, -25), 25, azul, pelota2_recorrido)
        self.totalPelotas = 4
        self.pelotas = []

    def indice_inicial_pelota_mano(self, pelota, totalPelotas):
        rango_entre_pelotas = int(len(pelota.recorrido)/2)
        resto_de_rango_entre_pelotas = len(pelota.recorrido) % totalPelotas

        pelota1 = Pelota((-25,-25), 25, azul, self.pelota1.recorrido)
        pelota1.index_inicio = 0
        pelota2 = Pelota((-25,-25), 25, azul, self.pelota1.recorrido)
        pelota2.index_inicio = len(pelota2.recorrido)//4
        pelota3 = Pelota((-25,-25), 25, azul, self.pelota2.recorrido)
        pelota3.index_inicio = len(self.pelota1.recorrido)//8
        pelota4 = Pelota((-25,-25), 25, azul, self.pelota2.recorrido)
        pelota4.index_inicio = len(pelota4.recorrido)//8 + len(self.pelota1.recorrido)//4

        self.pelotas.append(pelota1)
        self.pelotas.append(pelota2)
        self.pelotas.append(pelota3)
        self.pelotas.append(pelota4)

        self.mano2.index_inicio = 0
        self.mano1.index_inicio = len(pelota1.recorrido)//2
    
    def calcularArrayDeSpeedsPelota(self, pelota: Pelota = None, mano=None):
        total = len(pelota.recorrido)//2
        result = []

        rango = total

        for i in range(rango):
            result.append(2)

        return result
    
    def calcularArrayDeSpeedsMano(self, pelota: Pelota, mano: Mano, totalPelotas):
        total_iter_pelota = len(pelota.recorrido) # 176
        total_iter_mano = len(mano.recorrido) # 
        iter_entre_cada_pelota = int(total_iter_pelota / (totalPelotas / 2))
        velocidad = 1

        result = []

        for i in range(total_iter_pelota):
            if i >= total_iter_mano:
                result.append(0)         # hay un pequenio desface aqui
            elif i <= total_iter_mano // 4:
                result.append(velocidad + 1)
            elif i <=total_iter_mano // 2:
                result.append(0)
            else:
                result.append(velocidad)
        return result

        



