import pygame
pygame.init()

#Creer le joueur

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.health = 100
        self.max_healt = 100
        self.attach = 10
        self.velocity = 5 

#Créer la fenetre du jeu

pygame.display.set_caption("Survive to comet") #Titre de la fenetre
screen = pygame.display.set_mode((1080,720)) #Taille de la fenetre

#Importer l'asset d'arrière plan du jeu

background = pygame.image.load('assets/bg.jpg')


#Boucle tant que running est True
running = True 

while running : 

    #Appliquer l'arrière plan du jeu
    screen.blit(background, (0,-200))

    #Mettre a jour l'écran
    pygame.display.flip()

    #Si le joueur ferme cette fenetre 
    for event in pygame.event.get():
        #que l'évenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
