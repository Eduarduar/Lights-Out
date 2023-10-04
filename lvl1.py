import sys, pygame, time, random
from assets.defaults.button import Button
from assets.defaults.get_fonts import get_font
from assets.defaults.idioma import cargar_idioma
from assets.defaults.get_imgs import imgs_lvl1
from opciones_juego import opciones_juego

idioma = cargar_idioma()
imgs = imgs_lvl1()
reloj = pygame.time.Clock()

#inicilizamos las variables
segundoUltimoFoco = 0
segundoAnterior = 0
infoPersonaje = {}
LimiteConsumo = 0
segundoAccion = 0
consumoPorSeg = 0
consumoTotal = 0
tiempoPasado = 0
barraMax = 0
focos = {}
color = ()
fps = 0
powerUps = {}

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

# funcion para reiniciar las variables
def reinciar():
    
    global segundoUltimoFoco
    global segundoAnterior
    global consumoPorSeg
    global LimiteConsumo
    global consumoTotal
    global infoPersonaje
    global segundoAccion
    global tiempoPasado
    global powerUps
    global barraMax
    global focos
    global color
    global fps
        
    
    segundoUltimoFoco = 0
    color = (0, 255, 0)
    segundoAnterior = 0
    LimiteConsumo = 360 # el limite son 350 watts 
    segundoAccion = 0
    consumoPorSeg = 2 # 2 watt por segundo
    consumoTotal = 0 # el consumo total de los focos
    tiempoPasado = 0
    barraMax = 275
    fps = 10
    powerUps = {
        "powerUpsActivos": 0,
        "powerUpsTotales": 0,
        "probabilidad": 15,
        "estados": { 
            "reducirConsumo": {
                "nombre": "reducirConsumo",
                "PX": 0,
                "piso": 0,
                "activo": False,
                "suelto": False,
                "tiempo": 10,
                "alto": 40
            },
            "Velocidad": {
                "nombre": "velocidad",
                "PX": 0,
                "piso": 0,
                "activo": False,
                "suelto": False,
                "tiempo": 10,
                "alto": 40
            }
        }
    }
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
        "PX": 980,
        "PY": 530,
        "ancho": 50,
        "velocidad": 10,
        "direccion": "izquierda",
        "cuentaPasos": 0,
        "quieto": True,
        "piso": 1
    }

# cuando se apague un foco habra una pequeña posibilidad de soltar un powerup
def soltarPowerUp():
    global powerUps
    soltarPowerUp = random.randint(1, 100)
    if soltarPowerUp <= powerUps["probabilidad"]:
        soltarPowerUp = random.randint(1, 100)
        if soltarPowerUp <= 50:
            powerUps["estados"]["reducirConsumo"]["PX"] = random.randint(200, 1000)
            powerUps["estados"]["reducirConsumo"]["piso"] = random.randint(1, 2)
            powerUps["estados"]["reducirConsumo"]["activo"] = False
            powerUps["estados"]["reducirConsumo"]["suelto"] = True
            powerUps["estados"]["reducirConsumo"]["tiempo"] = 10
        else:
            powerUps["estados"]["Velocidad"]["PX"] = random.randint(200, 1000)
            powerUps["estados"]["Velocidad"]["piso"] = random.randint(1, 2)
            powerUps["estados"]["Velocidad"]["activo"] = False
            powerUps["estados"]["Velocidad"]["suelto"] = True
            powerUps["estados"]["Velocidad"]["tiempo"] = 10

# funcion que controla los powerUps y los coloca en pantalla
def pintarPowerUps(SCREEN, segundero):
    global powerUps
    global infoPersonaje
    global segundoAnterior
    for powerUp in powerUps["estados"].items():
        if powerUp[1]["suelto"] == True:
            if powerUp[1]["activo"] == False:
                # verificamos si el personaje toco el powerUp
                if infoPersonaje["PX"] >= powerUp[1]["PX"] - infoPersonaje["ancho"] and infoPersonaje["PX"] <= powerUp[1]["PX"] + 40:
                    if infoPersonaje["piso"] == powerUp[1]["piso"]:
                        powerUp[1]["activo"] = True
                        powerUp[1]["suelto"] = False
                        powerUps["powerUpsActivos"] += 1
                        print("powerUp activado")
                elif powerUp[1]["piso"] == 1:
                    SCREEN.blit(imgs["powerUps"][powerUp[1]["nombre"]], (powerUp[1]["PX"], 530 + powerUp[1]["alto"]))
                else:
                    SCREEN.blit(imgs["powerUps"][powerUp[1]["nombre"]], (powerUp[1]["PX"], 350 + powerUp[1]["alto"]))
                print(powerUp[1]["tiempo"])
        else:  
            if powerUp[1]["activo"] == True:
                if segundero != segundoAnterior: # verificamos si el tiempo cambio 
                    powerUp[1]["tiempo"] -= 1 # si el tiempo cambio restamos un segundo
                    if powerUp[1]["tiempo"] <= 0: # verificamos si el powerUp se acabo
                        powerUp[1]["tiempo"] = 10
                        powerUp[1]["activo"] = False
                        powerUp[1]["suelto"] = False
                        powerUps["powerUpsActivos"] -= 1

# funcion para mostrar una pantalla de pausa antes de iniciar
def pausaInicio(SCREEN, configJuego):
    detener = True
    while detener:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                detener = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        SCREEN.blit(imgs["fondo"], (0,0))
        SCREEN.blit(izquierda[0], (int(infoPersonaje["PX"]), int(infoPersonaje["PY"])))
        SCREEN.blit(imgs["sombra_lvl1"], (0,0))
        SCREEN.blit(imgs["sombras"]["sombra1"], (0,0))
        SCREEN.blit(imgs["sombras"]["sombra2"], (0,0))
        SCREEN.blit(imgs["sombras"]["sombra3"], (0,0))
        SCREEN.blit(imgs["sombras"]["sombra4"], (0,0))
        SCREEN.blit(imgs["sombras"]["sombra5"], (0,0))
        SCREEN.blit(imgs["controles"], (0,0))

        # imprimimos texto de presionar cualquier tecla para continuar

        Text_text = get_font(20).render(idioma[configJuego["Idioma"]]["Juego"]["Preciona"], True, "#ffffff")
        Text_rect = Text_text.get_rect(center=(640, 500))
        SCREEN.blit(Text_text, Text_rect)

        pygame.display.flip()
        reloj.tick(10)

# funcion para pintar al personaje
def pintarPersonaje(SCREEN, accion = "caminar"):
        global infoPersonaje
        global fps
        if powerUps["estados"]["Velocidad"]["activo"] == True: # verificamos si el powerUp de velocidad esta activo
            fps = 20 # aumentamos los fps
        else:
            fps = 10 # reiniciamos los fps
        reloj.tick(fps) # fps

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

# funcion para mover al personaje
def moverPersonaje(SCREEN):
        global infoPersonaje
        global segundoAccion
        global tiempoPasado
        global focos

        keys = pygame.key.get_pressed() # eventos del teclado

        # Tecla A
        if keys[pygame.K_a] and infoPersonaje["PX"] > infoPersonaje["velocidad"] and infoPersonaje["PX"] - infoPersonaje["velocidad"] > 100:
            infoPersonaje["PX"] -= infoPersonaje["velocidad"]
            infoPersonaje["direccion"] = "izquierda"
            pintarPersonaje(SCREEN, accion="caminar")

        # Tecla D
        elif keys[pygame.K_d] and infoPersonaje["PX"] < 1000 - infoPersonaje["ancho"] - infoPersonaje["velocidad"]:
            infoPersonaje["PX"] += infoPersonaje["velocidad"]
            infoPersonaje["direccion"] = "derecha"
            pintarPersonaje(SCREEN, accion="caminar")

        # Tecla W
        elif keys[pygame.K_w] and ((infoPersonaje["PX"] >= 205 and infoPersonaje["PX"] <= 252) or (infoPersonaje["ancho"] + infoPersonaje["PX"] >= 205 and infoPersonaje["PX"] + infoPersonaje["ancho"] <= 252)):
            if infoPersonaje["piso"] == 1 and segundoAccion != tiempoPasado:
                infoPersonaje["piso"] = 2
                infoPersonaje["PY"] -= 180
            elif segundoAccion != tiempoPasado:
                infoPersonaje["piso"] = 1
                infoPersonaje["PY"] += 180
            segundoAccion = tiempoPasado
            pintarPersonaje(SCREEN)

        # Tecla Espacio
        elif keys[pygame.K_SPACE]:
            for foco in focos["focosEstado"].items(): # recorremos los focos
                if foco[1]["estado"] != 0 and foco[1]["estado"] != 4 and infoPersonaje["piso"] == foco[1]["piso"]: # verificamos si el foco esta apagado
                    if infoPersonaje["PX"] >= foco[1]["apagadorX1"] - infoPersonaje["ancho"] and infoPersonaje["PX"] <= foco[1]["apagadorX2"] + infoPersonaje["ancho"]:
                        foco[1]["anteriorEstado"] = foco[1]["estado"]
                        foco[1]["estado"] = 0
                        focos["focosEncendidos"] -= 1
                        soltarPowerUp()
                        break
            pintarPersonaje(SCREEN, accion="apagar")

        #personaje quieto
        else:
            infoPersonaje["cuentaPasos"] = 1
            infoPersonaje["quieto"] = True
            pintarPersonaje(SCREEN, accion="quieto")

# funcion para pintar los focos
def pintarFocos(SCREEN, segundero):
    global segundoUltimoFoco
    global segundoAnterior
    global consumoPorSeg
    global consumoTotal
    global tiempoPasado
    global powerUps
    global focos
    global color
    if segundero != segundoAnterior: # verificamos si el tiempo cambio 
            tiempoPasado += 1 # si el tiempo cambio sumamos un segundo
            if powerUps["estados"]["reducirConsumo"]["activo"] == True: # verificamos si el powerUp de reducir consumo esta activo
                consumoTotal += (consumoPorSeg / 2) * focos["focosEncendidos"] # reducimos a la mitad el consumo de los focos encendidos
            else:
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

    # pintamos los focos encendidos
    for foco in focos["focosEstado"].items(): # recorremos los focos
        if foco[1]["estado"] != 0 and foco[1]["estado"] != 4: # verificamos si el foco esta apagado
            SCREEN.blit(imgs[f"bombilla{foco[1]['estado']}"], foco[1]["posicion"]) # colocamos el foco en pantalla
        else:
            SCREEN.blit(imgs[f"sombras"][f"sombra{foco[1]['numero']}"], (0, 0))

# funcion para mostrar una pantalla de game over
def perder(SCREEN, configJuego, LvlsInfo, elementosFondo):
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

# funcion para mostrar una pantalla de ganaste
def ganar(SCREEN, configJuego, LvlsInfo, elementosFondo):
    # mostramos una pantalla de ganaste o un mensaje de ganaste
    pygame.image.save(SCREEN, "assets/img/pantalla.png")
    ultimoFrame = pygame.image.load("assets/img/pantalla.png")
    while True:
        for event in pygame.event.get():
            # si preciona cualquier tecla retorna al menu principal
            if event.type == pygame.KEYDOWN:
                LvlsInfo["LvlDisponibles"]["lvl2"] = True
                LvlsInfo["LvlCompletados"]["lvl1"] = True
                return SCREEN , configJuego, LvlsInfo, elementosFondo
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        SCREEN.blit(ultimoFrame, (0,0))
        SCREEN.blit(imgs["oscuro"], (0,0))

        TITULO_TEXT = get_font(100).render(idioma[configJuego["Idioma"]]["Juego"]["Ganaste"], True, "#70f4c1")
        TITULO_RECT = TITULO_TEXT.get_rect(center=(640, 200))
        SCREEN.blit(TITULO_TEXT, TITULO_RECT)

        Text_text = get_font(20).render(idioma[configJuego["Idioma"]]["Juego"]["Preciona"], True, "#ffffff")
        Text_rect = Text_text.get_rect(center=(640, 500))
        SCREEN.blit(Text_text, Text_rect)

        pygame.display.flip()

# funcion para pintar el tiempo transcurrido
def pintarTiempo(SCREEN, tiempoPasado, configJuego):    
        #a 120 le restamos el tiempoPasado para tener un temporizador de 2 minutos
        relojF = 121 - tiempoPasado

        # formateamos los segundos de relojF para que se muestre con el formato mm:ss
        minutos = relojF // 60
        segundos = relojF % 60 

        # creamos e imprimimos el tiempo transcurrido

        tiempo = get_font(30).render(f"{idioma[configJuego['Idioma']]['Juego']['Tiempo']}{minutos}:{segundos}s", True, "White")
        tiempoRect = tiempo.get_rect(center=(740, 50))

        # colocamos el tempo
        SCREEN.blit(tiempo, tiempoRect)

        return relojF

# funcion para mostrar el nivel 1
def pantalla_lvl1(SCREEN , configJuego, LvlsInfo, elementosFondo):
    global segundoUltimoFoco
    global segundoAnterior
    global consumoPorSeg
    global LimiteConsumo
    global consumoTotal
    global infoPersonaje
    global segundoAccion
    global tiempoPasado
    global barraMax
    global focos
    global color
    reinciar()

    if configJuego["indiceMusic"] != 2:
        configJuego["indiceMusic"] = 2
        pygame.mixer.music.load(f"assets/songs/musica{configJuego['indiceMusic']}.wav") #cargamos la musica
        pygame.mixer.music.set_volume(configJuego["Volumen"]) #le bajamos el volumen a la musica
        pygame.mixer.music.play(-1) #reproducimos la musica en bucle

    pygame.display.set_caption(idioma[configJuego["Idioma"]]["Nivel1"]["Titulo"])
    btnOpciones = Button(image=None, pos=(1047,57), text_input="||", font=get_font(30), base_color="White", hovering_color="#555f68") # boton de pausa

    pausaInicio(SCREEN, configJuego) # pantalla antes de iniciar

    # bucle del juego
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # eventos del raton
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btnOpciones.checkForInput(posicionMause):
                    SCREEN , configJuego, LvlsInfo, elementosFondo, accion = opciones_juego(SCREEN , configJuego, LvlsInfo, elementosFondo)
                    pygame.display.set_caption(idioma[configJuego["Idioma"]]["Nivel1"]["Titulo"])
                    if accion == "salir":
                        return SCREEN , configJuego, LvlsInfo, elementosFondo
                    elif accion == "reiniciar":
                        segundoUltimoFoco = 0
                        segundoAnterior = 0
                        infoPersonaje = {}
                        LimiteConsumo = 0
                        segundoAccion = 0
                        consumoPorSeg = 0
                        consumoTotal = 0
                        tiempoPasado = 0
                        barraMax = 0
                        focos = {}
                        color = ()
                        reinciar()

        segundero = time.localtime().tm_sec # optenemos el tiempo actual

        posicionMause = pygame.mouse.get_pos() # obtenemos la posicion del mouse
        
        SCREEN.blit(imgs["fondo"], (0,0)) # colocamos el fondo del nivel

        btnOpciones.changeColor(posicionMause) # verificamos si el mause esta en el boton de opciones
        btnOpciones.update(SCREEN) #colocamos el boton de pausa

        pygame.draw.rect(SCREEN, color, (1147, (509 - consumoTotal), 40, consumoTotal)) # dibujamos la barra de consumo

        pintarFocos(SCREEN, segundero) # actualizamos los estados de los focos

        pintarPowerUps(SCREEN, segundero) # actualizamos los estados de los powerUps

        moverPersonaje(SCREEN) # movemos al personaje

        relojF = pintarTiempo(SCREEN, tiempoPasado, configJuego) # colocamos el tiempo transcurrido y obtenemos el tiempo restante

        SCREEN.blit(imgs["sombra_lvl1"], (0,0)) # colocamos la sombra de los pasillos

        if consumoTotal >= LimiteConsumo or(relojF > 0 and focos["focosFundidos"] == 5): # verificamos si el jugador perdio
            SCREEN , configJuego, LvlsInfo, elementosFondo = perder(SCREEN, configJuego, LvlsInfo, elementosFondo)
            return SCREEN , configJuego, LvlsInfo, elementosFondo

        if relojF <= 0 and focos["focosFundidos"] < 5: # verificamos si el jugador gano
            SCREEN , configJuego, LvlsInfo, elementosFondo = ganar(SCREEN, configJuego, LvlsInfo, elementosFondo)
            return SCREEN , configJuego, LvlsInfo, elementosFondo

        pygame.display.flip() # actualizamos la pantalla


# ! Nota importante:
# ? agregar sonidos a clicks, pasos, puertas, etc...
# ? agregar Powerups