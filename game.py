import pygame
from player import Player
from monster import Monster

#Créer la representation du jeu
class Game:
    def __init__(self):
        #définir si le jeu a commencé 
        self.is_playing = False
        #génerer le joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        #remettre a 0 le jeu 
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        #Rajouter le joueur
        screen.blit(self.player.image, self.player.rect)

        #Actualise la barre de vie du joueur
        self.player.update_health_bar(screen)

        #Rajouter les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        #Rajoute les monstres du jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        #Rajouter le projectile 
        self.player.all_projectiles.draw(screen)

        #Ensemble d'image du groupe de monstre
        self.all_monsters.draw(screen)

        #Bordure du jeu et touche de déplacement
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < 1110:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > -30:
            self.player.move_left()
        
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)