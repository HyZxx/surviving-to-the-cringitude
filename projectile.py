import pygame

#Génerer le projectile
class Projectile(pygame.sprite.Sprite):

    #Le constructeur du projectile
    def __init__(self, player):
        super().__init__()
        self.velocity = 1
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80