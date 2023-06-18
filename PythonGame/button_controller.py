import pygame

class Button:

    is_hovered = False

    def __init__(self, screen, x, y, width, height, text, color, hover_color, action):
        self.font = pygame.font.Font("resources/fonts/Arvo-Regular.ttf", 32)
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.action = action

    def draw(self):
        # Dibujar el botón en la pantalla
        color = self.hover_color if self.is_hovered else self.color

        pygame.draw.rect(self.screen, color, self.rect)
        pygame.draw.rect(self.screen, "black", self.rect, 2)

        # Crear el objeto de texto
        text_surface = self.font.render(self.text, True, "black")
        text_rect = text_surface.get_rect(center=self.rect.center)

        # Dibujar el texto en la pantalla
        self.screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Verificar si se hizo clic en el botón
            if self.rect.collidepoint(event.pos):
                # Ejecutar la acción del botón
                self.action()

        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)


        