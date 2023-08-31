import pygame, sys, json
from button import Button

# Idioma ---------------------------------------------------------------------

idioma = {}

# Cargamos el archivo de idioma y evitaremos que los caracteres se vean mal
with open("assets/idioma.json", encoding="utf-8") as f:
    idioma = json.load(f)

# solo en desarrollo - para cambiar el idioma desde la consola
opIdioma = "en"
# while True:
#     op = input("Seleccione el idioma / Select the language\n1. Español\n2. English\n")
#     if op == "1":
#         opIdioma = "es"
#         break
#     elif op == "2":
#         opIdioma = "en"
#         break
#     else:
#         print("Opción incorrecta / Incorrect option")

# Musica ---------------------------------------------------------------------

# cargaremos la musica de fondo
pygame.mixer.pre_init(44100, -16, 2, 512) #el 44100 es el estandar de la musica, el -16 es el estandar de la calidad, el 2 es el estandar de los canales y el 512 es el tamaño del buffer
pygame.mixer.init() #inicializamos el mixer
pygame.mixer.music.load("assets/songs/blondes-whats-up.mp3") #cargamos la musica
pygame.mixer.music.play(-1) # ponemos la musica en bucle
pygame.mixer.music.set_volume(0.8) # ponemos el volumen de la musica al 80%

# inicializamos pygame
pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
#imprimimos el titulo de la ventana usando los recursos de idioma
pygame.display.set_caption(idioma[opIdioma]["MenuInicial"]["Titulo"])


#cargamos la imagen de fondo y la escalamos
BG1 = pygame.transform.scale(pygame.image.load("assets/backgrounds/Background.png"), (1280, 720))
BG2 = pygame.transform.scale(pygame.image.load("assets/backgrounds/Background2.png"), (1280, 720))

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def niveles(opIdioma):
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        
        #cambiamos el titulo de la ventana
        pygame.display.set_caption(idioma[opIdioma]["Niveles"]["Titulo"])

        #limpiamos para la nueva pantalla
        SCREEN.fill("black")

        PLAY_BACK = Button(image=None, pos=(640, 460), text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu(opIdioma)

        pygame.display.update()
    
def options(opIdioma):
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

        OPTIONS_BACK = Button(image=None, pos=(50,50), text_input="X", font=get_font(75), base_color="White", hovering_color="Red")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        # Volumen --------------------------------------

        #generamos el texto de las opciones
        txtVolumen = get_font(45).render(idioma[opIdioma]["Opciones"]["Opcion2"], True, "White")
        SCREEN.blit(txtVolumen, (100, 450))
        
        #imprimimos el porcentaje del volumen actual
        txtPorcentaje = get_font(45).render(str(int(pygame.mixer.music.get_volume() * 100)) + "%", True, "White")
        SCREEN.blit(txtPorcentaje, (850, 450))

        btnVolumen1 = Button(image=pygame.transform.scale(pygame.image.load("assets/Play Rect.png"), (75, 50)), pos=(1100, 450), text_input="↑", font=get_font(45), base_color="White", hovering_color="Green")
        btnVolumen1.changeColor(OPTIONS_MOUSE_POS)
        btnVolumen1.update(SCREEN)

        btnVolumen2 = Button(image=pygame.transform.scale(pygame.image.load("assets/Play Rect.png"), (75, 50)), pos=(1100, 500), text_input="↓", font=get_font(45), base_color="White", hovering_color="Green")
        btnVolumen2.changeColor(OPTIONS_MOUSE_POS)
        btnVolumen2.update(SCREEN)

        # idioma --------------------------------------

        #generamos el texto de las opciones
        txtIdiomas = get_font(45).render(idioma[opIdioma]["Opciones"]["Opcion1"], True, "White")
        SCREEN.blit(txtIdiomas, (100, 300))

        btnIdioma1 = Button(image=pygame.transform.scale(pygame.image.load("assets/Play Rect.png"), (350, 100)), pos=(1000, 320), text_input=idioma[opIdioma]["Idioma"], font=get_font(45), base_color="White", hovering_color="Green")
        btnIdioma1.changeColor(OPTIONS_MOUSE_POS)
        btnIdioma1.update(SCREEN)

        # detectamos los eventos ----------------------

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: # detectamos el click del mouse
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):  # detectamos si el click fue en el boton de regresar
                    main_menu(opIdioma) # si fue en el boton de regresar, regresamos al menu principal
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

def main_menu(opIdioma):
    while True:
        SCREEN.blit(BG2, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos() # obtenemos la posicion del mouse

        MENU_TEXT = get_font(70).render(idioma[opIdioma]["Titulo"], True, "#97ffc6")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/Play Rect.png"), (550, 100)), pos=(640, 250),  text_input=idioma[opIdioma]["MenuInicial"]["Opcion1"], font=get_font(75), base_color="#d7fcd4", hovering_color="#97ffc6")
        OPTIONS_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/Play Rect.png"), (620, 100)), pos=(640, 400), text_input=idioma[opIdioma]["MenuInicial"]["Opcion2"], font=get_font(75), base_color="#d7fcd4", hovering_color="#97ffc6")
        QUIT_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/Play Rect.png"), (400, 100)), pos=(640, 550), text_input=idioma[opIdioma]["MenuInicial"]["Opcion3"], font=get_font(75), base_color="#d7fcd4", hovering_color="#97ffc6")

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
                    options(opIdioma) # si fue en el boton de opciones, vamos a la pantalla de opciones
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS): # detectamos si el click fue en el boton de salir
                    pygame.quit() # si fue en el boton de salir, salimos del juego
                    sys.exit()
        
        

        pygame.display.update()

main_menu(opIdioma)