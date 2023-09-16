import pygame

def imgs_menu_principal():
    Caja = pygame.transform.scale(pygame.image.load("assets/img/rect.png"), (550, 100))
    ciudad = pygame.transform.scale(pygame.image.load("assets/backgrounds/ciudad.png"), (1280, 720))
    luna = pygame.image.load("assets/backgrounds/luna.png")
    nube = pygame.image.load("assets/backgrounds/nube.png")

    imgs = {
        "ciudad": ciudad,
        "luna": luna,
        "nube": nube,
        "caja": Caja
    }

    return imgs

def imgs_opciones():
    azul = pygame.image.load("assets/backgrounds/azul.jpg")
    Caja = pygame.transform.scale(pygame.image.load("assets/img/rect.png"), (550, 100))

    imgs = {
        "azul": azul,
        "caja": Caja
    }

    return imgs

def imgs_niveles():
    azul = pygame.image.load("assets/backgrounds/azul.jpg")
    Caja = pygame.transform.scale(pygame.image.load("assets/img/rect.png"), (550, 100))

    imgs = {
        "azul": azul,
        "caja": Caja
    }

    return imgs

def imgs_lvls():
    ConfigIcon = pygame.transform.scale(pygame.image.load("assets/img/config icon.png"), (50, 50))
    Caja = pygame.transform.scale(pygame.image.load("assets/img/rect.png"), (550, 100))

    imgs = {
        "configIcon": ConfigIcon,
        "caja": Caja
    }

    return imgs