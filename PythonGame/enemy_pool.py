from enemy_controller import EnemyController
from random_utills import RandomUtils

class Enemy_pool():

    time_per_enemy_spawn = 1
    actual_time = 0
    is_right = False

    enemy = EnemyController(0,0,0,0)

    is_pool_actived = False
    
    def __init__(self, screen, action_game_over):
        self.screen = screen
        self.enemy_array = []
        self.action_game_over = action_game_over
        self.create_range_enemy(10)
    
    def draw(self):
        for enemy in self.enemy_array:
            enemy.draw()

    def update(self, dt, player):
        for enemy in self.enemy_array:
            enemy.update(player)
        if self.is_pool_actived:
            self.cronometro(dt)

    def create_range_enemy(self, number_enemy):
        for i in range(number_enemy):
            self.create_new_enemy()

    def create_new_enemy(self):
        enemy = EnemyController(RandomUtils.get_random_number_btw_range(0,self.screen.get_width()),0, self.screen, self.action_game_over)
        enemy.set_active(False)
        self.enemy_array.append(enemy)
        self.enemy = enemy

    def get_enemy_pool(self):
        for enemy in self.enemy_array:
            if enemy.is_actived == False:
                self.enemy = enemy
                return

        self.create_new_enemy()
    
    def instantiate_enemy(self):
        self.get_enemy_pool()
        if self.is_right:
            self.enemy.change_position(RandomUtils.get_random_number_btw_range(-400, -100), -100)
        else:
            self.enemy.change_position(RandomUtils.get_random_number_btw_range(100, 400), -100)
        self.is_right = not self.is_right
        self.enemy.set_active(True)

    def cronometro(self, dt):
        self.actual_time += dt
        if self.actual_time > self.time_per_enemy_spawn:
            self.instantiate_enemy()
            self.actual_time = 0
        