import pygame
from player import Player
from monster import ogre,shrek
from comet_event import CometFallEvent
from sounds import SoundManager

#Créer la representation du jeu
class Game:
    def __init__(self):
        #définir si le jeu a commencé 
        self.is_playing = False
        #génerer le joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #Génere l'event comet 
        self.comet_event = CometFallEvent(self)
        #groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        #Gérer le son
        self.sound_manager = SoundManager()
        #mettre le score a 0
        self.font = pygame.font.Font("assets/myfonts.ttf", 25)
        self.score = 0
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster(ogre)
        self.spawn_monster(ogre)
        self.spawn_monster(shrek)

    def add_score(self, points=10):
        self.score += points

    def game_over(self):
        #remettre a 0 le jeu 
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.all_projectiles = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        self.sound_manager.play('game_over')

    def update(self, screen):
        #Afficher le score sur l'écran
        score_text = self.font.render(f"Score : {self.score}", 1, (0,0,0))
        screen.blit(score_text, (500,50))

        #Rajouter le joueur
        screen.blit(self.player.image, self.player.rect)
        
        #Actualise la barre de vie du joueur
        self.player.update_health_bar(screen)

        #Actualise la barre d'event comet
        self.comet_event.update_bar(screen)

        #Actualise l'anim du joueur
        self.player.update_animation()

        #Rajouter les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        #Rajoute les monstres du jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        #Rajoute les comet du jeu
        for comet in self.comet_event.all_comets:
            comet.fall()

        #Rajouter le projectile 
        self.player.all_projectiles.draw(screen)

        #Ensemble d'image du groupe de monstre 
        self.all_monsters.draw(screen)

        #Ensemble d'image du groupe comet
        self.comet_event.all_comets.draw(screen)

        #Bordure du jeu et touche de déplacement
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < 1110:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > -30:
            self.player.move_left()
        
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self,monser_class_name):
        self.all_monsters.add(monser_class_name.__call__(self))
