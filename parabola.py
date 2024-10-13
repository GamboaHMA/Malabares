import math

blanco = (255, 255, 255)

class Parabola():
    def __init__(self, centro, coef_parabola, coef_lineal, rango, inversa=False):
        self.centro = centro
        self.coef_parabola = coef_parabola
        self.coef_lineal = coef_lineal
        self.rango = rango
        self.inversa = inversa
        self.points = self.getPoints()

    def getPoints(self):
        puntos = []

        if not self.inversa:
            for x in range(self.rango[0], self.rango[1]):
                y = int(((self.coef_parabola*x) ** 2)*1.6 / 0.01) + self.coef_lineal*x + self.centro[1]
                x_ = x + self.centro[0]
                puntos.append((x_, y))
        else:
            for x in range(self.rango[0], self.rango[1]):
                y = -int(((self.coef_parabola*x) ** 2)*1.6 / 0.01) + self.coef_lineal*x + self.centro[1]
                x_ = x + self.centro[0]
                puntos.append((x_, y))

        return puntos
    

    def draw(self, surface):
        for i in range(len(self.points)):
            surface.set_at((int(self.points[i][0]), int(self.points[i][1])), blanco)

        
    # recorrido es un conjunto de parabolas o curvas, las cuales dependiendo del tipo de malabar, se define un conjunto de puntos
    # los cuales seran las actualizaciones de la posicion de una pelota dada
    def puntosDeRecorrido(self, recorrido, malabar):
        puntos_de_recorrido = []
        for i in range(len(recorrido)):
            if not recorrido[i][1]:
                for j in range(len(recorrido[i][0].points)-1, -1, -1):  # recorremos de atras hacia delante porque esta invertido
                    puntos_de_recorrido.append(recorrido[i][0].points[j])
            else:
                for j in range(len(recorrido[i][0].points)):
                    puntos_de_recorrido.append(recorrido[i][0].points[j])
        
        return puntos_de_recorrido




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



#parabola_izq_der2 = Parabola((int(), ))

recorrido = [
             (parabola_izq_der1, False),
             (parabola_izq_der4, True),
             (parabola_izq_der3, True),
             (parabola_izq_der2, False),
             ]

mano1_recorrido = parabola_izq_der1.puntosDeRecorrido([(parabola_izq_der4, True), (mano1_parabola, False)], malabar='cascada3')
mano2_recorrido = parabola_izq_der1.puntosDeRecorrido([(parabola_izq_der2, False), (mano2_parabola, True)], malabar='cascada3')

puntos_de_recorrido = parabola_izq_der1.puntosDeRecorrido(recorrido=recorrido, malabar='cascada3')

