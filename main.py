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

        pelota1 = Pelota((550, 528), 25, azul, puntos_de_recorrido)
        mano1 = Mano((528, 452),(550, 529), mano1_recorrido)
        mano2 = Mano((790, 452),(765, 529), mano2_recorrido)
        malabar = Malabar((mano1, mano2),puntos_de_recorrido, pelota1, 3)



        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # obtener pos del pixel clickeado
                    x,y = event.pos

                for boton in menu.boton_stack:
                    boton_:Boton = boton
                    boton_.manejar_evento(event)

                    
            self.screen.fill('black')
            self.level.run()
            debug(f'{x,y}')
            menu.dibujar(self.screen)
        
            pygame.draw.line(self.screen, blanco, (550, 382), (528, 452),4)
            pygame.draw.line(self.screen, blanco, (766, 382), (790, 452),4)

            #parabola_izq_der1.draw(self.screen)
            #parabola_izq_der2.draw(self.screen)
            #parabola_izq_der3.draw(self.screen)
            #parabola_izq_der4.draw(self.screen)

            #mano1_parabola.draw(self.screen)
            #mano2_parabola.draw(self.screen)

            malabar.update()
            malabar.draw(self.screen)
            #mano1.draw(self.screen)
            #mano2.draw(self.screen)
            
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()