import pygame, sys
from settings import *
from level import *
from debug import *
from button import *
from pelota import *
from parabola import *
from malabar import *

class Game():
    def __init__(self):
        
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Malabares')
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        x,y = 0,0

        cascade31 = Cascade3()
        cascade4 = Cascade4()
        cascade5 = Cascade5()
        cascade6 = Cascade6()
        cascade3i = Cascade3Inverso()
        circular3 = Circular3()

        #parab_izq_der2_ = Parabola(centro_par_izq_der2, 0.01, 0, (-40, 40), inversa=True)
        #p_izq_der = Parabola((centro_par_izq_der2[0], centro_par_izq_der2[1] - 400), 0.01, 0, (-48, 48), mod1=16)
        #p_der_izq = Parabola((centro_par_izq_der2[0] - 285, centro_par_izq_der2[1] - 400), 0.01, 0, (-48, 48), mod1=16)
        #parab_izq_der1_ = Parabola((centro_par_izq_der2[0], centro_par_izq_der2[1] - 465), 0.01, 0, (-60, 60), mod1=12)



        malabares = [cascade31, cascade4, cascade5, cascade6, cascade3i, circular3]

        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                #if event.type == pygame.MOUSEBUTTONDOWN:
                #    # obtener pos del pixel clickeado
                #    x,y = event.pos

                for boton in menu.boton_stack:
                    boton_:Boton = boton
                    boton_.manejar_evento(event, menu.boton_stack, malabares)
                

                    
            self.screen.fill('black')
            self.level.run()
            #debug(f'{x,y}')
            menu.dibujar(self.screen)
        
            pygame.draw.line(self.screen, blanco, (550, 382), (528, 452),4)
            pygame.draw.line(self.screen, blanco, (766, 382), (790, 452),4)

            for malabar in malabares:
                malabar.update()
                malabar.draw(self.screen)
            
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()