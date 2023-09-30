import sys, pygame, time
from assets.defaults.button import Button
from assets.defaults.get_fonts import get_font
from assets.defaults.idioma import cargar_idioma
from assets.defaults.get_imgs import imgs_lvls
from opciones_juego import opciones_juego

idioma = cargar_idioma()
imgs = imgs_lvls()

reloj = pygame.time.Clock()
consumoTotal = 0
consumoPorSeg = 0
LimiteConsumo = 0
focos = {}
infoPersonaje = {}

def reinciar():
    
    global consumoTotal
    global consumoPorSeg
    global LimiteConsumo
    global focos
    global infoPersonaje
        
    consumoTotal = 0 # el consumo total de los focos
    consumoPorSeg = 1 # 1 watt por segundo
    LimiteConsumo = 360 # el limite son 350 watts 
    focos = {
        "focosFuncionales": 5,
        "focosEncendidos": 5,
        "focosFundidos": 0,
        "focosTotales": 5,
        "focosEstado": { # 0 = apagado, 1 = encendido, 2 = emepezando a calentarce, 3 = a punto de fundirse, 4 = fundido
            "foco1": {
                "estado": 1,
                "tiempoEncendido": 0,
            },
            "foco2": {
                "estado": 1,
                "tiempoEncendido": 0,
            },
            "foco3": {
                "estado": 1,
                "tiempoEncendido": 0,
            },
            "foco4": {
                "estado": 1,
                "tiempoEncendido": 0,
            },
            "foco5": {
                "estado": 1,
                "tiempoEncendido": 0,
            }
        }
    }

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

def recarga(SCREEN, infoPersonaje):

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

        #reiniciamos el estado del personaje
        infoPersonaje["quieto"] = False


def pantalla_lvl1(SCREEN , configJuego, LvlsInfo, elementosFondo):
    global consumoTotal

    reinciar()

    if configJuego["indiceMusic"] != 2:
        configJuego["indiceMusic"] = 2
        pygame.mixer.music.load(f"assets/songs/musica{configJuego['indiceMusic']}.wav") #cargamos la musica
        pygame.mixer.music.set_volume(configJuego["Volumen"]) #le bajamos el volumen a la musica
        pygame.mixer.music.play(-1) #reproducimos la musica en bucle

    pygame.display.set_caption(idioma[configJuego["Idioma"]]["Nivel1"]["Titulo"])
    btnOpciones = Button(image=None, pos=(1047,57), text_input="||", font=get_font(30), base_color="White", hovering_color="#555f68") # boton de pausa

    # controladores del tiempo
    segundoAnterior = 0
    tiempoPasado = 0

    while True:
            
        reloj.tick(15) #fps
        
        segundero = time.localtime().tm_sec # optenemos el tiempo actual

        if segundero != segundoAnterior: # verificamos si el tiempo cambio 
            tiempoPasado += 1 # si el tiempo cambio sumamos un segundo
            consumoTotal += consumoPorSeg * focos["focosEncendidos"] # sumamos el consumo de los focos encendidos
            segundoAnterior = segundero # actualizamos el tiempo anterior

            for foco in focos["focosEstado"].items(): # recorremos los focos
                if foco[1]["estado"] == 1 or foco[1]["estado"] == 2 or foco[1]["estado"] == 3: # verificamos si el foco esta encendido
                    foco[1]["tiempoEncendido"] += 1 # si el foco esta encendido sumamos un segundo

                    if foco[1]["tiempoEncendido"] >= 60: # verificamos si el foco esta encendido por mas de 30 segundos
                        foco[1]["estado"] = 4

                    elif foco[1]["tiempoEncendido"] >= 45: # verificamos si el foco esta encendido por mas de 45 segundos
                        foco[1]["estado"] = 3

                    elif foco[1]["tiempoEncendido"] >= 30: # verificamos si el foco esta encendido por mas de 60 segundos
                        foco[1]["estado"] = 2

                print(f"{foco[0]}: {foco[1]['estado']} {foco[1]['tiempoEncendido']}")

        if consumoTotal >= LimiteConsumo:
            # mostramos una pantalla de game over o un mensaje de game over
            print("Game Over")

        PLAY_MOUSE_POS = pygame.mouse.get_pos() # obtenemos la posicion del mouse

        #a 120 le restamos el tiempoPasado para tener un temporizador de 2 minutos
        relojF = 121 - tiempoPasado

        # formateamos los segundos de relojF para que se muestre con el formato mm:ss
        minutos = relojF // 60
        segundos = relojF % 60 

        # creamos e imprimimos el tiempo transcurrido

        tiempo = get_font(30).render(f"{idioma[configJuego['Idioma']]['Juego']['Tiempo']}{minutos}:{segundos}s", True, "White")
        tiempoRect = tiempo.get_rect(center=(740, 50))

        # verificamos si el mause esta en el boton de opciones
        
        btnOpciones.changeColor(PLAY_MOUSE_POS)
    
        # colocamos el fondo de la pantalla
        SCREEN.blit(imgs["fondo"], (0,0))

        # colocamos el tempo
        SCREEN.blit(tiempo, tiempoRect)

        # eventos del teclado
        keys = pygame.key.get_pressed()

        # Tecla A
        if keys[pygame.K_a] and infoPersonaje["PX"] > infoPersonaje["velocidad"] and infoPersonaje["PX"] - infoPersonaje["velocidad"] > 100:
            infoPersonaje["PX"] -= infoPersonaje["velocidad"]
            infoPersonaje["direccion"] = "izquierda"
            recarga(SCREEN, infoPersonaje)

        # Tecla D
        elif keys[pygame.K_d] and infoPersonaje["PX"] < 1000 - infoPersonaje["ancho"] - infoPersonaje["velocidad"]:
            infoPersonaje["PX"] += infoPersonaje["velocidad"]
            infoPersonaje["direccion"] = "derecha"
            recarga(SCREEN, infoPersonaje)

        #personaje quieto
        else:
            infoPersonaje["cuentaPasos"] = 1
            infoPersonaje["quieto"] = True
            recarga(SCREEN, infoPersonaje)

        #colocamos la oscuridad en general
        SCREEN.blit(imgs["sombra_lvl1"], (0,0))

        #colocamos el boton de pausa
        btnOpciones.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # eventos del raton
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btnOpciones.checkForInput(PLAY_MOUSE_POS):
                    SCREEN , configJuego, LvlsInfo, elementosFondo, accion = opciones_juego(SCREEN , configJuego, LvlsInfo, elementosFondo)
                    pygame.display.set_caption(idioma[configJuego["Idioma"]]["Nivel1"]["Titulo"])
                    if accion == "salir":
                        return SCREEN , configJuego, LvlsInfo, elementosFondo
                    elif accion == "reiniciar":
                        reinciar()
                        tiempoPasado = 0
                        segundoAnterior = 0
                        
        # recarga(SCREEN, infoPersonaje)
        pygame.display.update()

        # print(f"{idioma[configJuego['Idioma']]['Juego']['Tiempo']}{minutos}:{segundos} s")


        # ! Nota importante:
        # ? porner los focos estaticos en la imagen de fondo 
        # ? poner las puertas estaticas en la imagen de fondo
        # ? agregar decoraciones a los pasillos de forma estatica en el fondo
        # ? agregar sonidos a clicks, pasos, puertas, etc...
        # ? agregar una pantalla de game over
        # ? agregar una pantalla de ganaste