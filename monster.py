import pygame
import random

#Constructeur du monstre
class Monster(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.1
        self.velocity = 0.3 # = random.velocity(1,2) apparait avec une vitesse plus rapide ou plus lente aléatoirement
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540

    def damage(self, amount):
        #infliger des dégats
        self.health -= amount

        #Nombre de vie du monstre est inférieur ou égal a 0
        if self.health <= 0:
            #Réapparaitre nen nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            #self.velocity = random.randint(1,2) apparait avec une vitesse plus rapide ou plus lente aléatoirement
            self.health = self.max_health

    def update_health_bar(self, surface):

        #Creer le contour de la barre de vie 
        pygame.draw.rect(surface, (60 , 63,60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        #Creer la barre de vie 
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def forward(self):
        #déplacement seulement si aucune collision avec joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        #si le monstre est en colission
        else:
            #infliger des dégats (au joueur)
            self.game.player.damage(self.attack)