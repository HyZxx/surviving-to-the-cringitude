import pygame
from player import Player

#Créer la representation du jeu
class Game:
    def __init__(self):
        #génerer le joueur
        self.player = Player()
        self.pressed = {}