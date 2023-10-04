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

def imgs_lvl1():
    ConfigIcon = pygame.transform.scale(pygame.image.load("assets/img/config icon.png"), (50, 50))
    Caja = pygame.transform.scale(pygame.image.load("assets/img/rect.png"), (550, 100))
    fondo = pygame.image.load("assets/img/lvl1/fondo_lvl1.png")
    sombra_lvl1 = pygame.image.load("assets/img/lvl1/sombra_lvl1.png")
    bombilla0 = pygame.image.load("assets/img/sprites/items/bombillas/Bombilla0.png")
    bombilla1 = pygame.image.load("assets/img/sprites/items/bombillas/Bombilla1.png")
    bombilla2 = pygame.image.load("assets/img/sprites/items/bombillas/Bombilla2.png")
    bombilla3 = pygame.image.load("assets/img/sprites/items/bombillas/Bombilla3.png")
    sombra1 = pygame.image.load("assets/img/lvl1/sombra1.png")
    sombra2 = pygame.image.load("assets/img/lvl1/sombra2.png")
    sombra3 = pygame.image.load("assets/img/lvl1/sombra3.png")
    sombra4 = pygame.image.load("assets/img/lvl1/sombra4.png")
    sombra5 = pygame.image.load("assets/img/lvl1/sombra5.png")
    controles = pygame.image.load("assets/img/controles.png")
    oscuro = pygame.image.load("assets/img/oscuro.png")
    
    sombras = {
        "sombra1": sombra1,
        "sombra2": sombra2,
        "sombra3": sombra3,
        "sombra4": sombra4,
        "sombra5": sombra5
    }

    imgs = {
        "configIcon": ConfigIcon,
        "caja": Caja,
        "fondo": fondo,
        "sombra_lvl1": sombra_lvl1,
        "bombilla0": bombilla0,
        "bombilla1": bombilla1,
        "bombilla2": bombilla2,
        "bombilla3": bombilla3,
        "sombras": sombras,
        "oscuro": oscuro,
        "controles": controles
    }

    return imgs

def imgs_lvl2():
    ConfigIcon = pygame.transform.scale(pygame.image.load("assets/img/config icon.png"), (50, 50))
    Caja = pygame.transform.scale(pygame.image.load("assets/img/rect.png"), (550, 100))
    fondo = pygame.image.load("assets/img/lvl1/fondo_lvl1.png")
    sombra_lvl1 = pygame.image.load("assets/img/lvl1/sombra_lvl1.png")
    bombilla0 = pygame.image.load("assets/img/sprites/items/bombillas/Bombilla0.png")
    bombilla1 = pygame.image.load("assets/img/sprites/items/bombillas/Bombilla1.png")
    bombilla2 = pygame.image.load("assets/img/sprites/items/bombillas/Bombilla2.png")
    bombilla3 = pygame.image.load("assets/img/sprites/items/bombillas/Bombilla3.png")

    sombras = {

    }

    imgs = {
        "configIcon": ConfigIcon,
        "caja": Caja,
        "fondo": fondo,
        "sombra_lvl1": sombra_lvl1,
        "bombilla0": bombilla0,
        "bombilla1": bombilla1,
        "bombilla2": bombilla2,
        "bombilla3": bombilla3
    }

    return imgs

def imgs_lvl3():
    ConfigIcon = pygame.transform.scale(pygame.image.load("assets/img/config icon.png"), (50, 50))
    Caja = pygame.transform.scale(pygame.image.load("assets/img/rect.png"), (550, 100))
    fondo = pygame.image.load("assets/img/lvl1/fondo_lvl1.png")
    sombra_lvl1 = pygame.image.load("assets/img/lvl1/sombra_lvl1.png")
    bombilla0 = pygame.image.load("assets/img/sprites/items/bombillas/Bombilla0.png")
    bombilla1 = pygame.image.load("assets/img/sprites/items/bombillas/Bombilla1.png")
    bombilla2 = pygame.image.load("assets/img/sprites/items/bombillas/Bombilla2.png")
    bombilla3 = pygame.image.load("assets/img/sprites/items/bombillas/Bombilla3.png")
    sombras = {

    }

    imgs = {
        "configIcon": ConfigIcon,
        "caja": Caja,
        "fondo": fondo,
        "sombra_lvl1": sombra_lvl1,
        "bombilla0": bombilla0,
        "bombilla1": bombilla1,
        "bombilla2": bombilla2,
        "bombilla3": bombilla3
    }

    return imgs

def imgs_optionsLvls():
    Caja = pygame.transform.scale(pygame.image.load("assets/img/rect.png"), (550, 100))
    oscuro = pygame.image.load("assets/img/oscuro.png")

    imgs = {
        "caja": Caja,
        "oscuro": oscuro
    }

    return imgs
