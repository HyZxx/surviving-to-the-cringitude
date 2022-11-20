import pygame

#Génerer le projectile
class Projectile(pygame.sprite.Sprite):

    #Le constructeur du projectile
    def __init__(self):
        super().__init__()
        self.velocity = 1
        self.image = pygame.image.load('assets/projectile.png')
        self.rect = self.image.get_rect()