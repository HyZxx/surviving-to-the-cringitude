import pygame
from player import Player
from monster import Monster

#Créer la representation du jeu
class Game:
    def __init__(self):
        #génerer le joueur
        self.player = Player()
        #groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()

    def spawn_monster(self):
        monster = Monster()
        self.all_monsters.add(monster)