import pygame

# colores
blanco = (255, 255, 255)
azul = (0, 155, 155)
verde = (100, 155, 100)

def cambiar_color(boton, botones, malabares):
    boton.activate = not boton.activate
    for i in range(len(botones)):
        if botones[i].index != boton.index:
            botones[i].activate = False
        if boton.index == i:
            malabares[i].is_activate = not malabares[i].is_activate
        else:
            malabares[i].is_activate = False


class Boton():
    def __init__(self,index, texto, tamanio, color, color_al_activar, accion):
        self.index = index
        self.texto = texto
        self.tamanio = tamanio
        self.color = color
        self.color_al_activar = color_al_activar
        self.accion = accion
        self.activate = False  # estado del boton
        
    def dibujar(self, pos, surface):

        # color basado en el estado del boton
        color = self.color if not self.activate else self.color_al_activar
        self.rect = pygame.Rect(pos, self.tamanio)
        pygame.draw.rect(surface, color, self.rect)

        # dibujar texto en el centro del boton
        fuente = pygame.font.Font(None, 16)
        texto_surface = fuente.render(self.texto, True, blanco)
        texto_rect = texto_surface.get_rect(center = self.rect.center)
        surface.blit(texto_surface, texto_rect)

    def manejar_evento(self, evento, botones, malabares):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(evento.pos):
                self.accion(self, botones, malabares)
            

boton1 = Boton(0, 'Cascada 3', (150, 50), verde, azul, cambiar_color)
boton2 = Boton(1, 'Cascada 4', (150, 50), verde, azul, cambiar_color)
boton3 = Boton(2, 'Cascada 5', (150, 50), verde, azul, cambiar_color)
boton4 = Boton(3, 'Cascada 6', (150, 50), verde, azul, cambiar_color)
boton5 = Boton(4, 'Cascada 3 Inversa', (150, 50), verde, azul, cambiar_color)
boton6 = Boton(5, 'Circular 3', (150, 50), verde, azul, cambiar_color)


class Menu():
    def __init__(self, pos):
        self.pos = pos
        self.boton_stack = []

    def dibujar(self, surface):
        for boton in self.boton_stack:
            boton.dibujar(boton.pos, surface)

    def agregar_botones(self, botones, index):
        self.boton_stack = self.boton_stack[:index] + botones + self.boton_stack[index:]
        for i in range(len(self.boton_stack)):
            self.boton_stack[i].pos = (self.pos[0], i*(self.boton_stack[i].tamanio[1] + 10) + self.pos[1])



menu = Menu((10, 50))
menu.agregar_botones([boton1, boton2, boton6], 0)
menu.agregar_botones([boton3, boton4, boton5], 2)