import sys, pygame, time, random
from assets.defaults.button import Button
from assets.defaults.get_fonts import get_font
from assets.defaults.idioma import cargar_idioma
from assets.defaults.get_imgs import imgs_lvl1
from opciones_juego import opciones_juego

idioma = cargar_idioma()
imgs = imgs_lvl1()

reloj = pygame.time.Clock()
consumoTotal = 0
consumoPorSeg = 0
LimiteConsumo = 0
focos = {}
infoPersonaje = {}
segundoAccion = 0
bararMax = 275
color = (0, 255, 0)

def reinciar():
    
    global consumoTotal
    global consumoPorSeg
    global LimiteConsumo
    global focos
    global infoPersonaje
    global segundoAccion
    global bararMax
    global color
        
    
    segundoAccion = 0
    bararMax = 275
    color = (0, 255, 0)
    consumoTotal = 0 # el consumo total de los focos
    consumoPorSeg = 2 # 2 watt por segundo
    LimiteConsumo = 360 # el limite son 350 watts 
    focos = {
        "focosFuncionales": 5,
        "focosEncendidos": 0,
        "focosFundidos": 0,
        "focosTotales": 5,
        "focosEstado": { # 0 = apagado, 1 = encendido, 2 = emepezando a calentarce, 3 = a punto de fundirse, 4 = fundido
            "foco1": {
                "numero": 1,
                "estado": 0,
                "ultimoEstado": 1,
                "tiempoEncendido": 0,
                "posicion": (341, 286),
                "apagadorX1": 305,
                "apagadorX2": 312,
                "piso": 2
            },
            "foco2": {
                "numero": 2,
                "estado": 0,
                "ultimoEstado": 1,
                "tiempoEncendido": 0,
                "posicion": (613, 286),
                "apagadorX1": 583,
                "apagadorX2": 590,
                "piso": 2
            },
            "foco3": {
                "numero": 3,
                "estado": 0,
                "ultimoEstado": 1,
                "tiempoEncendido": 0,
                "posicion": (916, 286),
                "apagadorX1": 884,
                "apagadorX2": 891,
                "piso": 2
            },
            "foco4": {
                "numero": 4,
                "estado": 0,
                "ultimoEstado": 1,
                "tiempoEncendido": 0,
                "posicion": (498, 465),
                "apagadorX1": 462,
                "apagadorX2": 469,
                "piso": 1
            },
            "foco5": {
                "numero": 5,
                "estado": 0,
                "ultimoEstado": 1,
                "tiempoEncendido": 0,
                "posicion": (832, 465),
                "apagadorX1": 791,
                "apagadorX2": 798,
                "piso": 1
            }
        }
    }

    infoPersonaje = {
        "Y": 0,
        "X": 0,
        "PX": 200,
        "PY": 530,
        "ancho": 50,
        "velocidad": 10,
        "direccion": "derecha",
        "cuentaPasos": 0,
        "quieto": True,
        "piso": 1
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

def recarga(SCREEN, infoPersonaje, accion = "caminar"):
        
        reloj.tick(10) # fps

        if accion == "caminar":

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
        else:
            if infoPersonaje["direccion"] == "derecha":
                SCREEN.blit(quietoD, (int(infoPersonaje["PX"]), int(infoPersonaje["PY"])))
            elif infoPersonaje["direccion"] == "izquierda":
                SCREEN.blit(quietoI, (int(infoPersonaje["PX"]), int(infoPersonaje["PY"])))


def pantalla_lvl1(SCREEN , configJuego, LvlsInfo, elementosFondo):
    global consumoTotal
    global consumoPorSeg
    global LimiteConsumo
    global focos
    global infoPersonaje
    global segundoAccion
    global color
    reinciar()

    if configJuego["indiceMusic"] != 2:
        configJuego["indiceMusic"] = 2
        pygame.mixer.music.load(f"assets/songs/musica{configJuego['indiceMusic']}.wav") #cargamos la musica
        pygame.mixer.music.set_volume(configJuego["Volumen"]) #le bajamos el volumen a la musica
        pygame.mixer.music.play(-1) #reproducimos la musica en bucle

    pygame.display.set_caption(idioma[configJuego["Idioma"]]["Nivel1"]["Titulo"])
    btnOpciones = Button(image=None, pos=(1047,57), text_input="||", font=get_font(30), base_color="White", hovering_color="#555f68") # boton de pausa

    # controladores del tiempo
    segundoUltimoFoco = 0
    segundoAnterior = 0
    tiempoPasado = 0

    while True:
        
        segundero = time.localtime().tm_sec # optenemos el tiempo actual

        if segundero != segundoAnterior: # verificamos si el tiempo cambio 
            tiempoPasado += 1 # si el tiempo cambio sumamos un segundo
            consumoTotal += consumoPorSeg * focos["focosEncendidos"] # sumamos el consumo de los focos encendidos
            segundoAnterior = segundero # actualizamos el tiempo anterior

            for foco in focos["focosEstado"].items(): # recorremos los focos
                if foco[1]["estado"] == 1 or foco[1]["estado"] == 2 or foco[1]["estado"] == 3: # verificamos si el foco esta encendido
                    foco[1]["tiempoEncendido"] += 1 # si el foco esta encendido sumamos un segundo 
                    if (consumoTotal > 120): # color amarillo
                        color = (255, 255, 0)
                    elif (consumoTotal > 240): # color rojo
                        color = (255, 0, 0)

                    if foco[1]["tiempoEncendido"] >= 70: # verificamos si el foco esta encendido por mas de 30 segundos
                        foco[1]["estado"] = 4
                        foco[1]["ultimoEstado"] = 4
                        focos["focosFundidos"] += 1
                        focos["focosEncendidos"] -= 1

                    elif foco[1]["tiempoEncendido"] >= 45: # verificamos si el foco esta encendido por mas de 45 segundos
                        foco[1]["estado"] = 3
                        foco[1]["ultimoEstado"] = 3

                    elif foco[1]["tiempoEncendido"] >= 30: # verificamos si el foco esta encendido por mas de 60 segundos
                        foco[1]["estado"] = 2
                        foco[1]["ultimoEstado"] = 2                    

        if segundoUltimoFoco + 5 <= tiempoPasado and focos["focosEncendidos"] != 5 - focos["focosFundidos"]: # verificamos si pasaron 5 segundos desde que se fundio el ultimo foco
            segundoUltimoFoco = tiempoPasado # actualizamos el tiempo del ultimo foco encendido
            numFoco = 0
            while True: # buscamos un foco apagado
                numFoco = random.randint(1, focos["focosTotales"]) # elegimos un foco al azar
                if focos["focosEstado"][f"foco{numFoco}"]["estado"] == 0: # verificamos si el foco esta apagado
                    break
            focos["focosEstado"][f"foco{numFoco}"]["estado"] = focos["focosEstado"][f"foco{numFoco}"]["ultimoEstado"] # encendemos el foco
            focos["focosEncendidos"] += 1 # sumamos un foco encendido

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

        # colocamos la barra de consumo
        pygame.draw.rect(SCREEN, color, (1147, (509 - consumoTotal), 40, consumoTotal)) # dibujamos la barra de consumo

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

        # Tecla W
        elif keys[pygame.K_w] and ((infoPersonaje["PX"] >= 205 and infoPersonaje["PX"] <= 252) or (infoPersonaje["ancho"] + infoPersonaje["PX"] >= 205 and infoPersonaje["PX"] + infoPersonaje["ancho"] <= 252)):
            if infoPersonaje["piso"] == 1 and segundoAccion != tiempoPasado:
                infoPersonaje["piso"] = 2
                infoPersonaje["PY"] -= 180
            elif segundoAccion != tiempoPasado:
                infoPersonaje["piso"] = 1
                infoPersonaje["PY"] += 180
            segundoAccion = tiempoPasado
            recarga(SCREEN, infoPersonaje, accion = "saltar")

        # Tecla Espacio
        elif keys[pygame.K_SPACE]:
            for foco in focos["focosEstado"].items(): # recorremos los focos
                if foco[1]["estado"] != 0 and foco[1]["estado"] != 4 and infoPersonaje["piso"] == foco[1]["piso"]: # verificamos si el foco esta apagado
                    print(f"El foco {foco[1]['numero']} esta encendido")
                    if infoPersonaje["PX"] >= foco[1]["apagadorX1"] - infoPersonaje["ancho"] and infoPersonaje["PX"] <= foco[1]["apagadorX2"] + infoPersonaje["ancho"]:
                        foco[1]["anteriorEstado"] = foco[1]["estado"]
                        foco[1]["estado"] = 0
                        focos["focosEncendidos"] -= 1
                        break

            recarga(SCREEN, infoPersonaje)

        #personaje quieto
        else:
            infoPersonaje["cuentaPasos"] = 1
            infoPersonaje["quieto"] = True
            recarga(SCREEN, infoPersonaje)

        # pintamos los focos encendidos
        for foco in focos["focosEstado"].items(): # recorremos los focos
            if foco[1]["estado"] != 0 and foco[1]["estado"] != 4: # verificamos si el foco esta apagado
                SCREEN.blit(imgs[f"bombilla{foco[1]['estado']}"], foco[1]["posicion"]) # colocamos el foco en pantalla
            else:
                SCREEN.blit(imgs[f"sombras"][f"sombra{foco[1]['numero']}"], (0, 0))

        #colocamos la oscuridad en general
        SCREEN.blit(imgs["sombra_lvl1"], (0,0))

        if consumoTotal >= LimiteConsumo:
            # mostramos una pantalla de game over o un mensaje de game over
            pygame.image.save(SCREEN, "assets/img/pantalla.png")
            ultimoFrame = pygame.image.load("assets/img/pantalla.png")
            while True:
                for event in pygame.event.get():
                    # si preciona cualquier tecla retorna al menu principal
                    if event.type == pygame.KEYDOWN:
                        return SCREEN , configJuego, LvlsInfo, elementosFondo
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                SCREEN.blit(ultimoFrame, (0,0))
                SCREEN.blit(imgs["oscuro"], (0,0))

                TITULO_TEXT = get_font(100).render(idioma[configJuego["Idioma"]]["Juego"]["Perdiste"], True, "#a1040f")
                TITULO_RECT = TITULO_TEXT.get_rect(center=(640, 200))
                SCREEN.blit(TITULO_TEXT, TITULO_RECT)

                Text_text = get_font(20).render(idioma[configJuego["Idioma"]]["Juego"]["Preciona"], True, "#ffffff")
                Text_rect = Text_text.get_rect(center=(640, 500))
                SCREEN.blit(Text_text, Text_rect)

                pygame.display.flip()

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
                        focos = {}
                        consumoTotal = 0
                        tiempoPasado = 0
                        segundoAccion = 0
                        consumoPorSeg = 0
                        LimiteConsumo = 0
                        infoPersonaje = {}
                        segundoAnterior = 0
                        segundoUltimoFoco = 0
                        reinciar()
                        
        # recarga(SCREEN, infoPersonaje)
        pygame.display.flip()
        # pygame.display.update()


        # ! Nota importante:
        # ? agregar sonidos a clicks, pasos, puertas, etc...
        # ? agregar una pantalla de game over
        # ? agregar una pantalla de ganaste
        # ? agregar Powerups