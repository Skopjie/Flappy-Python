import pygame

class PlayerController():

    speed = 1

    is_actived = True

    player_image = pygame.image.load("resources/imgs/orco1.png")
    player_rect = player_image.get_rect()


    def __init__(self, pos_x, pos_y, screen):
        self.player_pos = pygame.Vector2(pos_x, pos_y)
        self.screen = screen
        self.player_collider = pygame.draw.rect(screen, "red", (self.player_pos.x,self.player_pos.y, self.player_rect.width, self.player_rect.height))

    def update(self, dt):
        if self.is_actived:
            self.inputs(dt)
            self.block_positions_limits()


    def block_positions_limits(self):
        # eje x
        if self.player_pos.x < 0:
            self.player_pos.x = 0
        if self.player_pos.x > self.screen.get_width() - self.player_rect.width:
            self.player_pos.x = self.screen.get_width() -self.player_rect.width

        # eje y
        if self.player_pos.y < 0:
            self.player_pos.y = 0
        if self.player_pos.y > self.screen.get_height() - self.player_rect.height:
            self.player_pos.y = self.screen.get_height() -self.player_rect.height

    def inputs(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player_pos.y -= 300 * dt * self.speed
        if keys[pygame.K_s]:
            self.player_pos.y += 300 * dt * self.speed
        if keys[pygame.K_a]:
            self.player_pos.x -= 300 * dt * self.speed
        if keys[pygame.K_d]:
            self.player_pos.x += 300 * dt * self.speed


    def draw(self):
        if self.is_actived:
            self.player_collider = pygame.draw.rect(self.screen, "red", (self.player_pos.x, self.player_pos.y, self.player_rect.width, self.player_rect.height))

            self.player_rect.x = self.player_pos.x
            self.player_rect.y = self.player_pos.y
            self.screen.blit(self.player_image, self.player_rect)

    def change_position(self, pos_x, pos_y):
        self.enemy_pos.xy = pos_x, pos_y 

    def set_active(self, new_is_actived):
        self.is_actived = new_is_actived
