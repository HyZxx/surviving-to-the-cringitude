import pygame
from comet import Comet

#Constructeur d'event comet
class CometFallEvent:
    #chargement -> Compteur
    def __init__(self,game):
        self.percent = 0
        self.percent_speed = 30
        self.game = game
        self.fall_mode = False
        #définir un groupe de sprite 
        self.all_comets = pygame.sprite.Group()
        
    def add_percent(self):
        self.percent += self.percent_speed / 100
    def is_full_loaded(self):
        return self.percent >= 100
    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        #apparation d'un meteor
        self.all_comets.add(Comet(self))

    def attempt_fall(self):
        #jauge d'event remplis
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            self.meteor_fall()
            self.reset_percent()
            self.fall = True #Activer l'event
    
    def update_bar(self, surface):
        #Ajout du pourcentage de la barre
        self.add_percent()
        #barre en arriere plan (noir)
        pygame.draw.rect(surface, (0,0,0), [0, surface.get_height() - 720, surface.get_width(), 10])
        #barre jauge d'event (rouge)
        pygame.draw.rect(surface, (187,11,11), [0, surface.get_height() - 720, (surface.get_width() / 100) * self.percent, 10])
