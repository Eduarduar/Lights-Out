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

def imgs_lvl1(idioma):
    reloj = pygame.transform.scale(pygame.image.load("assets/img/sprites/items/powerUps/reloj.png"), (30,40))
    rayo = pygame.transform.scale(pygame.image.load("assets/img/sprites/items/powerUps/rayo.png"), (30,40))
    abierta = pygame.image.load("assets/img/sprites/items/puerta_departamento/SpritePuertaOn.png")
    Caja = pygame.transform.scale(pygame.image.load("assets/img/rect.png"), (550, 100))
    bombilla0 = pygame.image.load("assets/img/sprites/items/bombillas/Bombilla0.png")
    bombilla1 = pygame.image.load("assets/img/sprites/items/bombillas/Bombilla1.png")
    bombilla2 = pygame.image.load("assets/img/sprites/items/bombillas/Bombilla2.png")
    bombilla3 = pygame.image.load("assets/img/sprites/items/bombillas/Bombilla3.png")
    sombra_lvl1 = pygame.image.load("assets/img/lvl1/sombra_lvl1.png")
    fondo = pygame.image.load("assets/img/lvl1/fondo_lvl1.png")
    sombra1 = pygame.image.load("assets/img/lvl1/sombra1.png")
    sombra2 = pygame.image.load("assets/img/lvl1/sombra2.png")
    sombra3 = pygame.image.load("assets/img/lvl1/sombra3.png")
    sombra4 = pygame.image.load("assets/img/lvl1/sombra4.png")
    sombra5 = pygame.image.load("assets/img/lvl1/sombra5.png")
    oscuro = pygame.image.load("assets/img/oscuro.png")

    if idioma == "es":
        controles = pygame.image.load("assets/img/controlesEs.png")
    else:
        controles = pygame.image.load("assets/img/controlesEn.png")

    sombras = {
        "sombra1": sombra1,
        "sombra2": sombra2,
        "sombra3": sombra3,
        "sombra4": sombra4,
        "sombra5": sombra5
    }

    imgs = {
        "caja": Caja,
        "fondo": fondo,
        "sombra_lvl1": sombra_lvl1,
        "bombilla0": bombilla0,
        "bombilla1": bombilla1,
        "bombilla2": bombilla2,
        "bombilla3": bombilla3,
        "sombras": sombras,
        "oscuro": oscuro,
        "controles": controles,
        "powerUps": {
            "velocidad": rayo,
            "reducirConsumo": reloj
        },
        "abierta": abierta
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

def imgs_carga(personaje):
    
    img1 = pygame.image.load(f"assets/img/sprites/personajes/{personaje}/personaje1.png")
    img2 = pygame.image.load(f"assets/img/sprites/personajes/{personaje}/personaje2.png")
    img3 = pygame.image.load(f"assets/img/sprites/personajes/{personaje}/personaje3.png")
    personaje = [img1, img2, img3]
    derecha = []
    for i in range(0,3):
        for j in range(0,5):
            derecha.append(personaje[i])

    imgs = {
        "derecha": derecha,
        "quieto": img1
    }

    return imgs

def imgs_intro():
    imgs = []
    for i in range(1, 63):
        imgs.append(pygame.image.load("./assets/img/intro/" + str(i) + ".png"))

    return imgs

def imgs_historia(personaje):
    pasillo = pygame.image.load("assets/img/historia/pasillo.png")
    sombra = pygame.image.load("assets/img/historia/sombra.png")
    sombraLuz = pygame.image.load("assets/img/historia/sombra1.png")
    entrada = pygame.image.load("assets/img/historia/entrada.png")
    chat = pygame.transform.scale(pygame.image.load("assets/img/historia/chat.png"), (110, 120))
    #scalamos por 2 los focos
    foco1 = pygame.transform.scale(pygame.image.load("assets/img/sprites/items/bombillas/Bombilla0.png"), (64, 64))
    foco2 = pygame.transform.scale(pygame.image.load("assets/img/sprites/items/bombillas/Bombilla1.png"), (64, 64))
    rayo = pygame.transform.scale(pygame.image.load("assets/img/sprites/items/powerUps/rayo.png"), (64,64))


    derecha = [] 
    izquierda = []
    paradoD = pygame.transform.scale(pygame.image.load(f"assets/img/sprites/personajes/{personaje}/personaje1.png"), (100, 130))
    paradoI = pygame.transform.scale(pygame.image.load(f"assets/img/sprites/personajes/{personaje}/personaje4.png"), (100, 130))
    for i in range(1, 4):
        derecha.append(pygame.transform.scale(pygame.image.load(f"assets/img/sprites/personajes/{personaje}/personaje" + str(i) + ".png"), (100, 130)))

    for i in range(4, 7):
        izquierda.append(pygame.transform.scale(pygame.image.load(f"assets/img/sprites/personajes/{personaje}/personaje" + str(i) + ".png"), (100, 130)))

    imgs = {
        "pasillo": pasillo,
        "sombra": sombra,
        "sombraLuz": sombraLuz,
        "entrada": entrada,
        "derecha": derecha,
        "izquierda": izquierda,
        "paradoD": paradoD,
        "paradoI": paradoI,
        "chat": chat,
        "foco": foco1,
        "foco2": foco2,
        "rayo": rayo
    }

    return imgs