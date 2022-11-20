import pygame
from projectile import Projectile

#Creer le joueur
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_healt = 100
        self.attach = 10
        self.velocity = 1
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def launch_projectile(self):
        #creer l'instance du projectile du joueur
        projectile = Projectile()
        self.all_projectiles.add(Projectile())


    #Déplacement du joueur
    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity