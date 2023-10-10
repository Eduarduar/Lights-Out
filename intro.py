import pygame
from assets.defaults.get_imgs import imgs_intro

imgs = imgs_intro()
reloj = pygame.time.Clock()

def intro(SCREEN):
    pygame.display.set_caption("Lights Out")
    i = 1
    muestra = 1
    while True:
        reloj.tick(40)

        SCREEN.blit(imgs[i], (0, 0))
        pygame.display.update()

        i += 1

        if i >= 62:
            if muestra == 1:
                i = 1
                muestra = 2
            else:
                break