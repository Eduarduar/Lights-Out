import sys, pygame
from assets.defaults.button import Button
from assets.defaults.get_fonts import get_font
from assets.defaults.idioma import cargar_idioma
from assets.defaults.get_imgs import imgs_lvls
from opciones_juego import opciones_juego

idioma = cargar_idioma()
imgs = imgs_lvls()

def pantalla_lvl1(SCREEN , configJuego, LvlsInfo, elementosFondo):
    if configJuego["indiceMusic"] != 2:
        configJuego["indiceMusic"] = 2
        pygame.mixer.music.load(f"assets/songs/musica{configJuego['indiceMusic']}.wav") #cargamos la musica
        pygame.mixer.music.set_volume(configJuego["Volumen"]) #le bajamos el volumen a la musica
        pygame.mixer.music.play(-1) #reproducimos la musica en bucle

    while True:
        SCREEN.fill("black")

        PLAY_MOUSE_POS = pygame.mouse.get_pos() # obtenemos la posicion del mouse

        pygame.display.set_caption(idioma[configJuego["Idioma"]]["Niveles"]["Titulo"])

        # imprimimos el boton de opciones
        
        btnOpciones = Button(image=pygame.transform.scale(imgs["configIcon"], (50, 50)), pos=(1230,50), text_input="", font=get_font(75), base_color="White", hovering_color="Red")
        btnOpciones.changeColor(PLAY_MOUSE_POS)
        btnOpciones.update(SCREEN)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btnOpciones.checkForInput(PLAY_MOUSE_POS):
                    SCREEN , configJuego, LvlsInfo, elementosFondo, accion = opciones_juego(SCREEN , configJuego, LvlsInfo, elementosFondo)
                    if accion == "salir":
                        return SCREEN , configJuego, LvlsInfo, elementosFondo
                        
        pygame.display.update()