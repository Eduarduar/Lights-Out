import sys, pygame
from niveles import niveles
from opciones import opciones
from assets.defaults.button import Button
from assets.defaults.idioma import cargar_idioma
from assets.defaults.get_fonts import get_font
from assets.defaults.get_imgs import imgs_menu_principal

imgs = imgs_menu_principal()
reloj = pygame.time.Clock()
idioma = cargar_idioma()

def menu_principal(SCREEN , configJuego, LvlsInfo, elementosFondo):
    if configJuego["indiceMusic"] != 1:
        configJuego["indiceMusic"] = 1
        pygame.mixer.music.load(f"assets/songs/musica{configJuego['indiceMusic']}.wav") #cargamos la musica
        pygame.mixer.music.set_volume(configJuego["Volumen"]) #le bajamos el volumen a la musica
        pygame.mixer.music.play(-1) #reproducimos la musica en bucle

    pygame.display.set_caption(idioma[configJuego["Idioma"]]["MenuInicial"]["Titulo"])

    while True:
        # hacemos que el fondo se mueva en bucle 

        ciudadPosX = elementosFondo["ciudad"]["posX"] % 1280
        SCREEN.blit(imgs["ciudad"], (ciudadPosX - 1280 , elementosFondo["ciudad"]["posY"]))
        if ciudadPosX < 1280:
            SCREEN.blit(imgs["ciudad"], (ciudadPosX, elementosFondo["ciudad"]["posY"]))
        elementosFondo["ciudad"]["posX"] -= 2

        lunaposX = (elementosFondo["Luna"]["posX"]) % 1280
        SCREEN.blit(imgs["luna"], (lunaposX, elementosFondo["Luna"]["posY"]))
        if lunaposX < 1280:
            SCREEN.blit(imgs["luna"], (lunaposX - 1280, elementosFondo["Luna"]["posY"]))
        elementosFondo["Luna"]["posX"] -= 0.5

        nubeposX = (elementosFondo["nube"]["posX"]) % 1280
        SCREEN.blit(imgs["nube"], (nubeposX - 1280, elementosFondo["nube"]["posY"]))
        if nubeposX < 1280:
            SCREEN.blit(imgs["nube"], (nubeposX, elementosFondo["nube"]["posY"]))
        elementosFondo["nube"]["posX"] -= 1

        MENU_MOUSE_POS = pygame.mouse.get_pos() # obtenemos la posicion del mouse

        MENU_TEXT = get_font(70).render(idioma[configJuego["Idioma"]]["Titulo"], True, "#97ffc6")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.transform.scale(imgs["caja"], (550, 100)), pos=(640, 250),  text_input=idioma[configJuego["Idioma"]]["MenuInicial"]["Opcion1"], font=get_font(75), base_color="#d7fcd4", hovering_color="#97ffc6")
        OPTIONS_BUTTON = Button(image=pygame.transform.scale(imgs["caja"], (620, 100)), pos=(640, 400), text_input=idioma[configJuego["Idioma"]]["MenuInicial"]["Opcion2"], font=get_font(75), base_color="#d7fcd4", hovering_color="#97ffc6")
        QUIT_BUTTON = Button(image=pygame.transform.scale(imgs["caja"], (400, 100)), pos=(640, 550), text_input=idioma[configJuego["Idioma"]]["MenuInicial"]["Opcion3"], font=get_font(75), base_color="#d7fcd4", hovering_color="#97ffc6")

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
                    SCREEN , configJuego, LvlsInfo, elementosFondo = niveles(SCREEN , configJuego, LvlsInfo, elementosFondo) # si fue en el boton de jugar, vamos a la pantalla de niveles
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS): # detectamos si el click fue en el boton de opciones
                    SCREEN , configJuego, LvlsInfo, elementosFondo = opciones(SCREEN , configJuego, LvlsInfo, elementosFondo) # si fue en el boton de opciones, vamos a la pantalla de opciones
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS): # detectamos si el click fue en el boton de salir
                    pygame.quit() # si fue en el boton de salir, salimos del juego
                    sys.exit()

        pygame.display.update()
        reloj.tick(30)