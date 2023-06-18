import pygame

class EnemyController():

    speed = 4
    is_actived = True

    myimage = pygame.image.load("resources/imgs/orco1.png")
    imagerect = myimage.get_rect()


    def __init__(self, pos_x, pos_y, screen, action_game_over):
        self.enemy_pos = pygame.Vector2(pos_x, pos_y)
        self.screen = screen
        self.action_game_over = action_game_over

    def update(self, player):
        if self.is_actived:
            self.enemy_pos.y += self.speed

            if self.enemy_object.colliderect(player):
                self.action_game_over()

            if self.enemy_pos.y >= self.screen.get_height():
                self.set_active(False)


    def draw(self):
        if self.is_actived:
            self.enemy_object = pygame.draw.rect(self.screen, "green", (self.enemy_pos.x, self.enemy_pos.y, self.imagerect.width, self.imagerect.height))

            self.imagerect.x = self.enemy_pos.x
            self.imagerect.y = self.enemy_pos.y
            self.screen.blit(self.myimage, self.imagerect)

    def change_position(self, pos_x, pos_y):
        self.enemy_pos.xy = pos_x, pos_y 

    def set_active(self, new_is_actived):
        self.is_actived = new_is_actived
