import pygame
from enemy_pool import Enemy_pool
from player_controller import PlayerController
from button_controller import Button
from menu_controller import MenuController

# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True
dt = 0

def play():
    menu_inicio.set_active(False)
    menu_game_over.set_active(False)
    enemy_pool.is_pool_actived = True
    player.set_active(True)
    player.player_pos.xy = screen.get_width() / 2, screen.get_height() / 2

def show_game_over():
    menu_inicio.set_active(False)
    menu_game_over.set_active(True)
    enemy_pool.is_pool_actived = False
    player.set_active(False)

background_image = pygame.image.load("resources/imgs/Fondo.png")
background_rect = background_image.get_rect()

player = PlayerController(screen.get_width() / 2, screen.get_height() / 2, screen)
player.set_active(False)

enemy_pool = Enemy_pool(screen, show_game_over)

menu_inicio = MenuController()
menu_inicio.add_new_button(Button(screen, screen.get_width() / 2 -100, screen.get_height() / 2 -100, 200, 50, "Jugar", "white", "gray", play))
menu_inicio.add_new_button(Button(screen, screen.get_width() / 2 -100, screen.get_height() / 2 , 200, 50, "Salir", "white", "gray", play))

menu_game_over = MenuController()
menu_game_over.add_new_button(Button(screen, screen.get_width() / 2 -100, screen.get_height() / 2 -100, 200, 50, "Game Over", "white", "gray", play))
menu_game_over.set_active(False)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        menu_inicio.handle_event(event)
        menu_game_over.handle_event(event)


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    screen.blit(background_image, background_rect)

    player.update(dt)
    player.draw()

    enemy_pool.draw()
    enemy_pool.update(dt, player.player_collider)

    menu_inicio.draw()
    menu_game_over.draw()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()