import pygame
import random

#Constructeur pour les animations
class AnimateSprite(pygame.sprite.Sprite):

    #Définir a faire a la création d'entité
    def __init__(self, sprite_name, size=(150,150)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'assets/{sprite_name}.png').convert_alpha()
        self.imagee = pygame.transform.scale(self.image, size)
        self.current_image = 0 #commencer l'anime a l'image 0
        self.images = animations.get(sprite_name)
        self.animation = False

    #Définir une méthode pour enclencher l'anim
    def start_animation(self):
        self.animation = True

    #définir une methode pour animer le sprite
    def animate(self, loop=False):

        #Vérifie si l'anim est active 
        if self.animation:

            #passer a l'image suivante
            self.current_image += 1
            #Vérifie si on atteint la fin de l'anim
            if self.current_image >= len(self.images):
                #Remettre l'anim au départ
                self.current_image = 0

                #Vérifie si l'anim n'est pas en boucle
                if loop is False:
                    #Désactivation de l'anim
                    self.animation = False
                

            #Modifier l'image précedente par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)


#Définir fonction pour charger l'image d'un sprite
def load_animation_images(sprite_name):
    #Charger les images animé de ce sprite dans le dossier correspondant
    images = []
    #Récuperer le chemin du dossier pour ce sprite
    path = f"assets/{sprite_name}/{sprite_name}"

    #boucle sur chaque image dans ce dossier
    for num in range(1,10): #Jusqu'a combien d'image va t'il récup dans un dossier
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    #Renvoyer le contenu de la liste d'image
    return images

#Définir un dic qui contient les images chargées de chaque sprite
#ogre -> [ogre1.png, ogre2.png, ...]
animations = {
    'ogre': load_animation_images('ogre'),
    'player': load_animation_images('player'),
    'shrek': load_animation_images('shrek')
}

