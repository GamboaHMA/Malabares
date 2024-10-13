import pygame

# colores
blanco = (255, 255, 255)
azul = (0, 255, 255)
verde = (100, 255, 200)

def cambiar_color(boton):
    boton.activado = not boton.activado


class Boton():
    def __init__(self, texto, tamanio, color, color_al_activar, accion):
        self.texto = texto
        self.tamanio = tamanio
        self.color = color
        self.color_al_activar = color_al_activar
        self.accion = accion
        self.activado = False  # estado del boton
        
    def dibujar(self, pos, surface):

        # color basado en el estado del boton
        color = self.color if not self.activado else self.color_al_activar
        self.rect = pygame.Rect(pos, self.tamanio)
        pygame.draw.rect(surface, color, self.rect)

        # dibujar texto en el centro del boton
        fuente = pygame.font.Font(None, 16)
        texto_surface = fuente.render(self.texto, True, blanco)
        texto_rect = texto_surface.get_rect(center = self.rect.center)
        surface.blit(texto_surface, texto_rect)

    def manejar_evento(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(evento.pos):
                self.accion(self)

boton1 = Boton('Click', (150, 50), verde, azul, cambiar_color)
boton2 = Boton('Click', (150, 50), verde, azul, cambiar_color)
boton3 = Boton('Click', (150, 50), verde, azul, cambiar_color)
boton4 = Boton('Click', (150, 50), verde, azul, cambiar_color)
boton5 = Boton('Click', (150, 50), verde, azul, cambiar_color)
boton6 = Boton('Click', (150, 50), verde, azul, cambiar_color)


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