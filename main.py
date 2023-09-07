import pygame, sys, json, random
from assets.defaults.button import Button

# Idioma ---------------------------------------------------------------------

idioma = {}
LvlDisponibles = {
    "lvl1": True,
    "lvl2": False,
    "lvl3": False
}
LvlCompletados = {
    "lvl1": False,
    "lvl2": False,
    "lvl3": False
}
opIdioma = "en"

# Cargamos el archivo de idioma y evitaremos que los caracteres se vean mal
with open("assets/lenguage/lenguage.json", encoding="utf-8") as f:
    idioma = json.load(f)

# Musica ---------------------------------------------------------------------

# cargaremos la musica de fondo
pygame.mixer.pre_init(44100, -16, 2, 512) #el 44100 es el estandar de la musica, el -16 es el estandar de la calidad, el 2 es el estandar de los canales y el 512 es el tamaño del buffer
pygame.mixer.init() #inicializamos el mixer
pygame.mixer.music.load("assets/songs/blondes-whats-up.mp3") #cargamos la musica
pygame.mixer.music.set_volume(0.8) # ponemos el volumen de la musica al 80%

# juego ----------------------------------------------------------------------

# inicializamos pygame
pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
#imprimimos el titulo de la ventana usando los recursos de idioma
pygame.display.set_caption(idioma[opIdioma]["MenuInicial"]["Titulo"])


#cargamos la imagen de fondo y la escalamos
BG1 = pygame.transform.scale(pygame.image.load("assets/backgrounds/Background.png"), (1280, 720))
BG2 = pygame.transform.scale(pygame.image.load("assets/backgrounds/Background2.png"), (1280, 720))

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/fonts/font.ttf", size)

def niveles(opIdioma):
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        
        #cambiamos el titulo de la ventana
        pygame.display.set_caption(idioma[opIdioma]["Niveles"]["Titulo"])

        #limpiamos para la nueva pantalla
        SCREEN.fill("black")

        #imprimimos el titulo de la pantalla
        MENU_TEXT = get_font(100).render(idioma[opIdioma]["Niveles"]["Titulo"], True, "#b68f40")

        # creamos 3 botonos correspondientes a los niveles
        
        btnLvl1 = Button(image=pygame.transform.scale(pygame.image.load("assets/img/rect.png"), (550, 100)), pos=(640, 250),  text_input=idioma[opIdioma]["Niveles"]["Opcion1"], font=get_font(75), base_color="#d7fcd4", hovering_color="#f9c447")
        btnLvl2 = Button(image=pygame.transform.scale(pygame.image.load("assets/img/rect.png"), (550, 100)), pos=(640, 400), text_input=idioma[opIdioma]["Niveles"]["Opcion2"], font=get_font(75), base_color="#d7fcd4", hovering_color="#f9c447")
        btnLvl3 = Button(image=pygame.transform.scale(pygame.image.load("assets/img/rect.png"), (550, 100)), pos=(640, 550), text_input=idioma[opIdioma]["Niveles"]["Opcion3"], font=get_font(75), base_color="#d7fcd4", hovering_color="#f9c447")

        # imprimimos el boton de regresar
        
        btnBack = Button(image=None, pos=(50,50), text_input="←", font=get_font(75), base_color="White", hovering_color="Red")
        btnBack.changeColor(PLAY_MOUSE_POS)
        btnBack.update(SCREEN)

        # tomando en cuenta los niveles disponibles cambiamos el color de los botones

        if LvlDisponibles["lvl1"] == True:
            btnLvl1.changeColor(PLAY_MOUSE_POS) 

        if LvlDisponibles["lvl2"] == True:
            btnLvl2.changeColor(PLAY_MOUSE_POS)

        if LvlDisponibles["lvl3"] == True:
            btnLvl3.changeColor(PLAY_MOUSE_POS)
        
        btnLvl1.update(SCREEN)
        btnLvl2.update(SCREEN)
        btnLvl3.update(SCREEN)

        # detectamos los eventos

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btnBack.checkForInput(PLAY_MOUSE_POS):
                    menuPrincipal(opIdioma)
                if btnLvl1.checkForInput(PLAY_MOUSE_POS) and LvlDisponibles["lvl1"] == True:
                    print("lvl1")
                if btnLvl2.checkForInput(PLAY_MOUSE_POS) and LvlDisponibles["lvl2"] == True:
                    print("lvl2")
                if btnLvl3.checkForInput(PLAY_MOUSE_POS) and LvlDisponibles["lvl3"] == True:
                    print("lvl3")

        pygame.display.update()
    
def opciones(opIdioma):
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        #cambiamos el titulo de la ventana
        pygame.display.set_caption(idioma[opIdioma]["Opciones"]["Titulo"])

        #limpiamos para la nueva pantalla
        SCREEN.blit(BG1, (0, 0))

        #generamos el titulo de la pantalla
        MENU_TEXT = get_font(100).render(idioma[opIdioma]["Opciones"]["Titulo"], True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        # Regresar ------------------------------------

        OPTIONS_BACK = Button(image=None, pos=(50,50), text_input="←", font=get_font(75), base_color="White", hovering_color="Red")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        # Volumen --------------------------------------

        #generamos el texto de las opciones
        txtVolumen = get_font(45).render(idioma[opIdioma]["Opciones"]["Opcion2"], True, "White")
        SCREEN.blit(txtVolumen, (100, 450))
        
        #imprimimos el porcentaje del volumen actual
        txtPorcentaje = get_font(45).render(str(int(pygame.mixer.music.get_volume() * 100)) + "%", True, "White")
        SCREEN.blit(txtPorcentaje, (850, 450))

        btnVolumen1 = Button(image=pygame.transform.scale(pygame.image.load("assets/img/rect.png"), (75, 50)), pos=(1100, 450), text_input="↑", font=get_font(45), base_color="White", hovering_color="Green")
        btnVolumen1.changeColor(OPTIONS_MOUSE_POS)
        btnVolumen1.update(SCREEN)

        btnVolumen2 = Button(image=pygame.transform.scale(pygame.image.load("assets/img/rect.png"), (75, 50)), pos=(1100, 500), text_input="↓", font=get_font(45), base_color="White", hovering_color="Green")
        btnVolumen2.changeColor(OPTIONS_MOUSE_POS)
        btnVolumen2.update(SCREEN)

        # idioma --------------------------------------

        #generamos el texto de las opciones
        txtIdiomas = get_font(45).render(idioma[opIdioma]["Opciones"]["Opcion1"], True, "White")
        SCREEN.blit(txtIdiomas, (100, 300))

        btnIdioma1 = Button(image=pygame.transform.scale(pygame.image.load("assets/img/rect.png"), (350, 100)), pos=(1000, 320), text_input=idioma[opIdioma]["Idioma"], font=get_font(45), base_color="White", hovering_color="Green")
        btnIdioma1.changeColor(OPTIONS_MOUSE_POS)
        btnIdioma1.update(SCREEN)

        # detectamos los eventos ----------------------

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: # detectamos el click del mouse
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):  # detectamos si el click fue en el boton de regresar
                    menuPrincipal(opIdioma) # si fue en el boton de regresar, regresamos al menu principal
                if btnVolumen1.checkForInput(OPTIONS_MOUSE_POS): # detectamos si el click fue en el boton de subir volumen
                    if pygame.mixer.music.get_volume() < 1: # si el volumen es menor a 1, lo subimos
                        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01) # subimos el volumen
                if btnVolumen2.checkForInput(OPTIONS_MOUSE_POS): # detectamos si el click fue en el boton de bajar volumen
                    if pygame.mixer.music.get_volume() > 0: # si el volumen es mayor a 0, lo bajamos
                        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.01) # bajamos el volumen
                if btnIdioma1.checkForInput(OPTIONS_MOUSE_POS): # detectamos si el click fue en el boton de cambiar idioma
                    if opIdioma == "es": # si el idioma es español, lo cambiamos a ingles
                        opIdioma = "en" 
                    else: # si el idioma es ingles, lo cambiamos a español
                        opIdioma = "es"

        pygame.display.update()

def menuPrincipal(opIdioma):
    while True:
        SCREEN.blit(BG2, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos() # obtenemos la posicion del mouse

        MENU_TEXT = get_font(70).render(idioma[opIdioma]["Titulo"], True, "#97ffc6")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/img/rect.png"), (550, 100)), pos=(640, 250),  text_input=idioma[opIdioma]["MenuInicial"]["Opcion1"], font=get_font(75), base_color="#d7fcd4", hovering_color="#97ffc6")
        OPTIONS_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/img/rect.png"), (620, 100)), pos=(640, 400), text_input=idioma[opIdioma]["MenuInicial"]["Opcion2"], font=get_font(75), base_color="#d7fcd4", hovering_color="#97ffc6")
        QUIT_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/img/rect.png"), (400, 100)), pos=(640, 550), text_input=idioma[opIdioma]["MenuInicial"]["Opcion3"], font=get_font(75), base_color="#d7fcd4", hovering_color="#97ffc6")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]: # recorremos los botones
            button.changeColor(MENU_MOUSE_POS) # cambiamos el color de los botones
            button.update(SCREEN) # actualizamos los botones
        
        for event in pygame.event.get(): # detectamos los eventos
            if event.type == pygame.QUIT: # si el evento es salir, salimos del juego
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: # si el evento es un click del mouse
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS): # detectamos si el click fue en el boton de jugar
                    niveles(opIdioma) # si fue en el boton de jugar, vamos a la pantalla de niveles
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS): # detectamos si el click fue en el boton de opciones
                    opciones(opIdioma) # si fue en el boton de opciones, vamos a la pantalla de opciones
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS): # detectamos si el click fue en el boton de salir
                    pygame.quit() # si fue en el boton de salir, salimos del juego
                    sys.exit()
        pygame.display.update()

def pantallaDeCarga(opIdioma):
    while True:

        # creamos un bucle for que repita el codigo de abajo 4 veces donde la variable i empieze en 1

        cantidad = random.randint(1, 3)
        for i in range(1, cantidad):
            for e in range(1, 5):
                SCREEN.fill("black")
                CARGA_TEXT = get_font(50).render(idioma[opIdioma][f"Carga"][f"Carga{e}"], True, "White")
                CARGA_RECT = CARGA_TEXT.get_rect(center=(640, 360))

                SCREEN.blit(CARGA_TEXT, CARGA_RECT)

                pygame.display.update()

                # despuesde 3 segundos cambiamos a la pantalla de menu principal
                pygame.time.delay(300)
        
        pygame.mixer.music.play(-1) # ponemos la musica en bucle
        menuPrincipal(opIdioma)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

# niveles en desarrollo

def pantallaLvl1():
    while True:
        SCREEN.fill("black")

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        
def pantallaLvl2():
    while True:
        SCREEN.fill("black")

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        
def pantallaLvl2():
    while True:
        SCREEN.fill("black")

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        

pantallaDeCarga(opIdioma)
