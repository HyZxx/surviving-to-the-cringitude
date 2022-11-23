import pygame
import random

#Constructeur comet
class Comet(pygame.sprite.Sprite):
    def __init__(self, comet_event):
        super().__init__()
        #Définir l'image a comet
        self.image = pygame.image.load('assets/comet.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.attack = 20
        self.velocity = random.randint(1,3)
        self.rect.x = random.randint(20,900)
        self.rect.y = - random.randint(0,600)
        self.comet_event = comet_event


    def remove(self):
        self.comet_event.all_comets.remove(self)

    def fall(self):
        self.rect.y += self.velocity

        #ne tombe pas sur le sol 
        if self.rect.y >= 500:
            #Retire la boule de feu
            self.remove()

            #Vérifie si il ya plus de boule de feu
            if len(self.comet_event.all_comets) == 0:
                #Remettre la jauge au départ
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        #Vérifie si la comet touche joueur
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            #Retire la boule de feu
            self.remove()
            #subir des dégats
            self.comet_event.game.player.damage(self.attack)