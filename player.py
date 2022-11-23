import pygame
from projectile import Projectile
import animation

#Creer le joueur
class Player(animation.AnimateSprite):
    def __init__(self, game):
        super().__init__('player')
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        if self.health - amount > amount:
           self.health -= amount
        else:
            #si le joueur n'a pu de vie
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):

        #Creer le contour de la barre de vie 
        pygame.draw.rect(surface, (60 , 63,60), [self.rect.x + 20, self.rect.y - 20, self.max_health, 7])
        #Creer la barre de vie 
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 20, self.rect.y - 20, self.health, 7])    

    def launch_projectile(self):
        #creer l'instance du projectile du joueur
        self.all_projectiles.add(Projectile(self))
        #Démarre l'anim du lancé
        self.start_animation()
        #jouer le tir 
        self.game.sound_manager.play('tir')

    #Déplacement du joueur
    def move_right(self):
        #joueur n'est pas en collision
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
