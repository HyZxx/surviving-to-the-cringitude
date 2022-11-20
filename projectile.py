import pygame

#Génerer le projectile
class Projectile(pygame.sprite.Sprite):

    #Le constructeur du projectile
    def __init__(self, player):
        super().__init__()
        self.velocity = 1
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        #tourner le projectile
        self.angle += 8
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)
        

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        #Vérifie projectile entre en collision
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            #Supprime le projectile
            self.remove()
            #infliger des dégats
            monster.damage(self.player.attack)

        #Vérifie projectile n'est plus sur l'écran
        if self.rect.x > 1080:
            #supprime le projectile
            self.remove()
            