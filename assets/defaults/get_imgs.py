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
    Caja = pygame.transform.scale(pygame.image.load("assets/img/rect.png"), (550, 100))
    ciudad = pygame.transform.scale(pygame.image.load("assets/backgrounds/ciudad.png"), (1280, 720))
    luna = pygame.image.load("assets/backgrounds/luna.png")
    nube = pygame.image.load("assets/backgrounds/nube.png")
    pasto = pygame.image.load("assets/img/niveles/pasto.png")

    edificios = {
        "edificio1": {
            "estado1": pygame.image.load("assets/img/niveles/edificio1-es1.png"),
            "estado2": pygame.image.load("assets/img/niveles/edificio1-es2.png")
        },
        "edificio2": {
            "estado1": pygame.image.load("assets/img/niveles/edificio2-es1.png"),
            "estado2": pygame.image.load("assets/img/niveles/edificio2-es2.png"),
            "estado3": pygame.image.load("assets/img/niveles/edificio2-es3.png")
        },
        "edificio3": {
            "estado1": pygame.image.load("assets/img/niveles/edificio3-es1.png"),
            "estado2": pygame.image.load("assets/img/niveles/edificio3-es2.png"),
            "estado3": pygame.image.load("assets/img/niveles/edificio3-es3.png")
        },
    }

    imgs = {
        "edificios": edificios,
        "pasto": pasto,
        "ciudad": ciudad,
        "luna": luna,
        "nube": nube,
        "caja": Caja
    }

    return imgs

def imgs_lvls():
    ConfigIcon = pygame.transform.scale(pygame.image.load("assets/img/config icon.png"), (50, 50))
    Caja = pygame.transform.scale(pygame.image.load("assets/img/rect.png"), (550, 100))
    fondo = pygame.image.load("assets/img/lvl1/fondo_lvl1.png")
    sombra_lvl1 = pygame.image.load("assets/img/lvl1/sombra_lvl1.png")
    bombilla0 = pygame.image.load("assets/img/sprites/items/bombillas/Bombilla0.png")
    bombilla1 = pygame.image.load("assets/img/sprites/items/bombillas/Bombilla1.png")
    bombilla2 = pygame.image.load("assets/img/sprites/items/bombillas/Bombilla2.png")
    bombilla3 = pygame.image.load("assets/img/sprites/items/bombillas/Bombilla3.png")
    oscuro = pygame.image.load("assets/img/oscuro.png")

    imgs = {
        "configIcon": ConfigIcon,
        "caja": Caja,
        "oscuro": oscuro,
        "fondo": fondo,
        "sombra_lvl1": sombra_lvl1,
        "bombilla0": bombilla0,
        "bombilla1": bombilla1,
        "bombilla2": bombilla2,
        "bombilla3": bombilla3
    }

    return imgs