import pygame
from game import Game
pygame.init()

####################  FENETRE DU JEU  ####################
pygame.display.set_caption("Survive to comet") #Titre de la fenetre
screen = pygame.display.set_mode((1080,720)) #Taille de la fenetre

#Importater l'arrière plan du jeu
background = pygame.image.load('assets/bg.jpg')

#charger le jeu
game = Game()

####################  BOUCLE RUNNING TRUE  ####################
running = True 

while running : 

    #Rajouter l'arrière plan
    screen.blit(background, (0,-200))

    #Rajouter le joueur
    screen.blit(game.player.image, game.player.rect)

    #Actualise la barre de vie du joueur
    game.player.update_health_bar(screen)

    #Rajouter les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    #Rajoute les monstres du jeu
    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    #Rajouter le projectile 
    game.player.all_projectiles.draw(screen)

    #Ensemble d'image du groupe de monstre
    game.all_monsters.draw(screen)

    #Bordure du jeu et touche de déplacement
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < 1110:
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > -30:
        game.player.move_left()    

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