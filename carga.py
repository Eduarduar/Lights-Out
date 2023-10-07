import sys, pygame, random, time
from assets.defaults.idioma import cargar_idioma
from assets.defaults.get_fonts import get_font
from assets.defaults.get_imgs import imgs_carga

idioma = cargar_idioma()
imgs = imgs_carga()

# crearemos una barra de carga horizontal que avance de poco en 

cuentaPasos = 0
px = 70
py = 40

# funcion para obtener las pausas de la barra de carga
def obtenerPausas(maximo):
    pausas = []
    for i in range(0, 3):
        # sacamos un numero aleatorio entre 0 y 100
        num = (random.randint(0, maximo))
        # redondemao el numero a la decena mas cercana
        num = round(num, -1)
        # si el numero es 0, lo cambiamos a 10
        if num == 0:
            num = 10
        # si el numero es igual al maximo, lo cambiamos a 990
        elif num == maximo:
            num = 990
        # añadimos el numero a la lista de pausas
        pausas.append(num)
    return pausas

# funcion para pintar el personaje
def pintarPersonaje(SCREEN, porcentaje, accion):
    global cuentaPasos, px, py

    if accion == "parado":
        SCREEN.blit(imgs["quieto"], (int(px + porcentaje), int(py)))
    else:

        if (cuentaPasos + 1) >= 15:
            cuentaPasos = 0

        SCREEN.blit(imgs["derecha"][cuentaPasos // 1], (int(px + porcentaje), int(py)))
        cuentaPasos += 1

# funcion para la pantalla de carga
def pantalla_de_carga(SCREEN, configJuego):
    # inicializamos nuestros parametros
    reloj = pygame.time.Clock()
    porcentaje = 0
    maximo = 1000
    pausas = obtenerPausas(maximo)
    pausa = False
    detener = True
    segundoAnterior = 0
    i = 1
    
    # generamos los texto a usar
    Text_text = get_font(20).render(idioma[configJuego["Idioma"]]["Juego"]["Preciona"], True, "#ffffff")
    Text_rect = Text_text.get_rect(center=(640, 700))

    while detener:
        reloj.tick(60)
        segundero = time.localtime().tm_sec # sacamos los segundos del reloj 

        if segundero != segundoAnterior:
            segundoAnterior = segundero
            pausa = False
            if i == 4:
                i = 1
            i += 1

        SCREEN.fill("BLACK") # rellenamos el fondo

        # Cargamos la barra de carga
        pygame.draw.rect(SCREEN, "WHITE", (100, 100, 1000, 50))
        pygame.draw.rect(SCREEN, "GREEN", (100, 100, 0 + porcentaje, 50))


        # Actualizamos el porcentaje
        if porcentaje <= maximo:
            pintarPersonaje(SCREEN, porcentaje, accion = "caminar")
            # si el porcentaje es igual a algun numero de la pausa, pausamos un segundo la carga
            if pausa != True:
                porcentaje += 10

            for numero in pausas:
                if porcentaje == numero:
                    pausa = True
                    break
        else:
            pintarPersonaje(SCREEN, porcentaje, accion = "parado")
            SCREEN.blit(Text_text, Text_rect)

        # texto de carga
        carga = get_font(30).render(idioma[configJuego["Idioma"]]["Carga"][f"Carga{i}"], True, "WHITE")
        SCREEN.blit(carga, (100, 20))

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if porcentaje >= maximo:
                    detener = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Actualizamos la pantalla
        pygame.display.flip()