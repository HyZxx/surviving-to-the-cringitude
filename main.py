import pygame
import math
from game import Game
pygame.init()

#définir une clock
clock = pygame.time.Clock()
FPS = 60

####################  FENETRE DU JEU  ####################
pygame.display.set_caption("Survive to comet") #Titre de la fenetre
screen = pygame.display.set_mode((1080,720)) #Taille de la fenetre

#Importater l'arrière plan du jeu
background = pygame.image.load('assets/bg2.jpg').convert_alpha()

#Importer la bannière
banner = pygame.image.load('assets/banner.png').convert_alpha()
banner = pygame.transform.scale(banner, (500,500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

#Importer le bouton
play_button = pygame.image.load('assets/button.png').convert_alpha()
play_button = pygame.transform.scale(play_button, (400,150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 1.80)

#charger le jeu
game = Game()

####################  BOUCLE RUNNING TRUE  ####################
running = True 

while running : 

    #Rajouter l'arrière plan
    screen.blit(background, (-1600,-1200))    

    #Vérifie si le jeu a commencé
    if game.is_playing:
        #déclencher les instructions du jeu
        game.update(screen)
    #Vérifie si le jeu a pas commencé 
    else:
        #Ajoute l'écran de bienvenue
        screen.blit(play_button, (play_button_rect))
        screen.blit(banner, banner_rect)

    #Mettre a jour l'écran
    pygame.display.flip()

    #Si le joueur ferme cette fenetre 
    for event in pygame.event.get():
        #que l'évenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        #Détecter les touches du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            #Détecter si le projectile est déclenché
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #Vérifie si souris est en collision avec bouton 
            if play_button_rect.collidepoint(event.pos):
                #Mettre le jeu en mode "lancé"
                game.start()
    #Fixer le nom de fps sur ma clock
    clock.tick(FPS)

