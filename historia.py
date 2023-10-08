import pygame, sys, time
from assets.defaults.get_imgs import imgs_historia

reloj = pygame.time.Clock()
imgs = []
posx = 1280
posy = 330
parte = 1
cuentaPasos = 0

# funcion para pintar el personaje
def pintarPersonaje(SCREEN, accion):
    global cuentaPasos, px, py

    if accion == "paradoD":
        SCREEN.blit(imgs["paradoD"], (posx, posy))
    elif accion == "paradoI":
        SCREEN.blit(imgs["paradoI"], (posx, posy))

    elif accion == "izquierda":
        if (cuentaPasos + 1) >= 4:
            cuentaPasos = 0
        SCREEN.blit(imgs["izquierda"][cuentaPasos // 1], (posx, posy))
        cuentaPasos += 1

    elif accion == "derecha":
        if (cuentaPasos + 1) >= 4:
            cuentaPasos = 0
        SCREEN.blit(imgs["derecha"][cuentaPasos // 1], (posx , posy))
        cuentaPasos += 1

def historia(SCREEN, personaje):
    global imgs
    global posx
    global posy
    global parte
    global reloj
    reloj.tick(30)
    imgs = imgs_historia(personaje)
    luz = True
    parar = False
    while True:

        SCREEN.blit(imgs["pasillo"], (0, 0))

        if parte == 1:

            if posx >= 700:
                posx -= 10
                pintarPersonaje(SCREEN, "izquierda")    
                SCREEN.blit(imgs["entrada"], (0, 0))
                SCREEN.blit(imgs["sombra"], (0, 0))
            else:
                parte = 2
                pintarPersonaje(SCREEN, "izquierda")    
                SCREEN.blit(imgs["entrada"], (0, 0))
                SCREEN.blit(imgs["sombra"], (0, 0))
            pygame.display.update()

        elif parte == 2:
            SCREEN.blit(imgs["chat"], (650, 200))
            SCREEN.blit(imgs["foco2"], (675, 215))
            pintarPersonaje(SCREEN, "paradoI")
            SCREEN.blit(imgs["sombra"], (0, 0))
            pygame.display.update()
            time.sleep(1)
            parte = 3
        elif parte == 3:
            SCREEN.blit(imgs["chat"], (650, 200))
            SCREEN.blit(imgs["foco"], (675, 215))
            pintarPersonaje(SCREEN, "paradoI")
            SCREEN.blit(imgs["sombra"], (0, 0))
            pygame.display.update()
            time.sleep(1)
            parte = 4
        elif parte == 4:
            SCREEN.blit(imgs["chat"], (650, 200))
            SCREEN.blit(imgs["rayo"], (675, 215))
            pintarPersonaje(SCREEN, "paradoI")
            SCREEN.blit(imgs["sombra"], (0, 0))
            pygame.display.update()
            time.sleep(1)
            parte = 5
        elif parte == 5:

            if posx >= -100:
                posx -= 10
                pintarPersonaje(SCREEN, "izquierda")    
                SCREEN.blit(imgs["entrada"], (0, 0))
                SCREEN.blit(imgs["sombra"], (0, 0))
                pygame.display.update()
            else:
                break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

