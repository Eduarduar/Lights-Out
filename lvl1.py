import sys, pygame
from assets.defaults.button import Button
from assets.defaults.get_fonts import get_font
from assets.defaults.idioma import cargar_idioma
from assets.defaults.get_imgs import imgs_lvls
from opciones_juego import opciones_juego

idioma = cargar_idioma()
imgs = imgs_lvls()

reloj = pygame.time.Clock()

infoPersonaje = {
    "Y": 0,
    "X": 0,
    "PX": 200,
    "PY": 530,
    "ancho": 0,
    "velocidad": 10,
    "direccion": "derecha",
    "cuentaPasos": 0,
    "quieto": True
}

quietoD = pygame.image.load("assets/img/sprites/personajes/jugador/personaje1.png")
quietoI = pygame.image.load("assets/img/sprites/personajes/jugador/personaje4.png")

derecha = [
    pygame.image.load("assets/img/sprites/personajes/jugador/personaje1.png"),
    pygame.image.load("assets/img/sprites/personajes/jugador/personaje2.png"),
    pygame.image.load("assets/img/sprites/personajes/jugador/personaje3.png")]

izquierda = [
    pygame.image.load("assets/img/sprites/personajes/jugador/personaje4.png"),
    pygame.image.load("assets/img/sprites/personajes/jugador/personaje5.png"),
    pygame.image.load("assets/img/sprites/personajes/jugador/personaje6.png")]

def recarga(SCREEN, infoPersonaje, btnOpciones):

        
        # colocamos el fondo de la pantalla
        SCREEN.blit(imgs["fondo"], (0,0))

        # colocamos el personaje segun su estado
        if (infoPersonaje["cuentaPasos"] + 1) >= 3:
            infoPersonaje["cuentaPasos"] = 0

        if infoPersonaje["direccion"] == "derecha" and infoPersonaje["quieto"] != True:
            SCREEN.blit(derecha[infoPersonaje["cuentaPasos"] // 1], (int(infoPersonaje["PX"]), int(infoPersonaje["PY"])))
            infoPersonaje["cuentaPasos"] += 1
        
        elif infoPersonaje["direccion"] == "izquierda" and infoPersonaje["quieto"] != True:
            SCREEN.blit(izquierda[infoPersonaje["cuentaPasos"] // 1], (int(infoPersonaje["PX"]), int(infoPersonaje["PY"])))
            infoPersonaje["cuentaPasos"] += 1
        elif infoPersonaje["direccion"] == "derecha" and infoPersonaje["quieto"] == True:
            SCREEN.blit(quietoD, (int(infoPersonaje["PX"]), int(infoPersonaje["PY"])))
        elif infoPersonaje["direccion"] == "izquierda" and infoPersonaje["quieto"] == True:
            SCREEN.blit(quietoI, (int(infoPersonaje["PX"]), int(infoPersonaje["PY"])))

        #colocamos las ombillas de las estadisticas
        SCREEN.blit(pygame.transform.scale(imgs["bombilla3"], (45, 45)), (1130,565))
        SCREEN.blit(pygame.transform.scale(imgs["bombilla0"], (45, 45)), (1130,645))
        
        #colocamos la oscuridad en general
        SCREEN.blit(imgs["sombra_lvl1"], (0,0))

        #colocamos el boton de pausa
        btnOpciones.update(SCREEN)

        #reiniciamos el estado del personaje
        infoPersonaje["quieto"] = False


def pantalla_lvl1(SCREEN , configJuego, LvlsInfo, elementosFondo):
    if configJuego["indiceMusic"] != 2:
        configJuego["indiceMusic"] = 2
        pygame.mixer.music.load(f"assets/songs/musica{configJuego['indiceMusic']}.wav") #cargamos la musica
        pygame.mixer.music.set_volume(configJuego["Volumen"]) #le bajamos el volumen a la musica
        pygame.mixer.music.play(-1) #reproducimos la musica en bucle

    while True:
            
        reloj.tick(15)

        PLAY_MOUSE_POS = pygame.mouse.get_pos() # obtenemos la posicion del mouse

        pygame.display.set_caption(idioma[configJuego["Idioma"]]["Niveles"]["Titulo"])

        # imprimimos el boton de opciones
        
        btnOpciones = Button(image=None, pos=(1047,57), text_input="||", font=get_font(30), base_color="White", hovering_color="#555f68")
        btnOpciones.changeColor(PLAY_MOUSE_POS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # eventos del teclado
            
            keys = pygame.key.get_pressed()

            # Tecla A
            if keys[pygame.K_a] and infoPersonaje["PX"] > infoPersonaje["velocidad"]:
                infoPersonaje["PX"] -= infoPersonaje["velocidad"]
                infoPersonaje["direccion"] = "izquierda"
                recarga(SCREEN, infoPersonaje, btnOpciones)

            # Tecla D
            elif keys[pygame.K_d] and infoPersonaje["PX"] < 1280 - infoPersonaje["ancho"] - infoPersonaje["velocidad"]:
                infoPersonaje["PX"] += infoPersonaje["velocidad"]
                infoPersonaje["direccion"] = "derecha"
                recarga(SCREEN, infoPersonaje, btnOpciones)

            #personaje quieto
            else:
                infoPersonaje["cuentaPasos"] = 1
                infoPersonaje["quieto"] = True
                recarga(SCREEN, infoPersonaje, btnOpciones)

            # eventos del raton
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btnOpciones.checkForInput(PLAY_MOUSE_POS):
                    SCREEN , configJuego, LvlsInfo, elementosFondo, accion = opciones_juego(SCREEN , configJuego, LvlsInfo, elementosFondo)
                    if accion == "salir":
                        return SCREEN , configJuego, LvlsInfo, elementosFondo
                        
        # recarga(SCREEN, infoPersonaje)
        pygame.display.update()

        print(infoPersonaje["PX"], infoPersonaje["PY"])