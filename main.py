import pygame
from game import Game
pygame.init()

####################  FENETRE DU JEU  ####################
pygame.display.set_caption("Survive to comet") #Titre de la fenetre
screen = pygame.display.set_mode((1080,720)) #Taille de la fenetre

#Importer l'asset d'arrière plan du jeu
background = pygame.image.load('assets/bg.jpg')

#charger le jeu
game = Game()

####################  BOUCLE RUNNING TRUE  ####################
running = True 

while running : 

    #Appliquer l'arrière plan du jeu
    screen.blit(background, (0,-200))

    #Appliquer le joueur
    screen.blit(game.player.image, game.player.rect)

    #Mettre a jour l'écran
    pygame.display.flip()

    #Si le joueur ferme cette fenetre 
    for event in pygame.event.get():
        #que l'évenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
