import sys, pygame
from assets.defaults.button import Button
from assets.defaults.get_fonts import get_font
from assets.defaults.idioma import cargar_idioma
from assets.defaults.get_imgs import imgs_optionsLvls

idioma = cargar_idioma()
imgs = imgs_optionsLvls()

def opciones_juego(SCREEN , configJuego, LvlsInfo, elementosFondo):
            
    configJuego["Volumen"] /= 4
    pygame.mixer.music.set_volume(configJuego["Volumen"])
    SCREEN.blit(imgs["oscuro"], (0,0))
    pygame.mixer.Sound.play(pygame.mixer.Sound("assets/sounds/pausar.ogg"))

    #cambiamos el titulo de la ventana
    pygame.display.set_caption(f'{idioma[configJuego["Idioma"]]["OpcionesLvl"]["Titulo"]} - {idioma[configJuego["Idioma"]]["Nivel1"]["Titulo"]}')

    # imprimimos el titulo de la pantalla encima de la caja
    MENU_TEXT = get_font(75).render(idioma[configJuego["Idioma"]]["OpcionesLvl"]["Titulo"], True, "#b68f40")
    MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
    SCREEN.blit(MENU_TEXT, MENU_RECT)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        configJuego["Volumen"] *= 4
                        pygame.mixer.music.set_volume(configJuego["Volumen"])
                        accion = "continuar"
                        return SCREEN , configJuego, LvlsInfo, elementosFondo, accion

            if event.type == pygame.MOUSEBUTTONDOWN: # detectamos el click del mouse
                if btnContinuar.checkForInput(OPTIONS_MOUSE_POS): 
                    configJuego["Volumen"] *= 4
                    pygame.mixer.music.set_volume(configJuego["Volumen"])
                    accion = "continuar"
                    pygame.mixer.Sound.play(pygame.mixer.Sound("assets/sounds/despausar.mp3"))
                    return SCREEN , configJuego, LvlsInfo, elementosFondo, accion
                if btnReiniciar.checkForInput(OPTIONS_MOUSE_POS): 
                    configJuego["Volumen"] *= 4
                    pygame.mixer.music.set_volume(configJuego["Volumen"])
                    accion = "reiniciar"
                    pygame.mixer.Sound.play(pygame.mixer.Sound("assets/sounds/despausar.mp3"))
                    return SCREEN , configJuego, LvlsInfo, elementosFondo, accion 
                if btnSalir.checkForInput(OPTIONS_MOUSE_POS): 
                    configJuego["Volumen"] *= 4
                    pygame.mixer.music.set_volume(configJuego["Volumen"])
                    accion = "salir"
                    pygame.mixer.Sound.play(pygame.mixer.Sound("assets/sounds/despausar.mp3"))
                    return SCREEN , configJuego, LvlsInfo, elementosFondo , accion
                
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        
        letra = 40
        if configJuego["Idioma"] == "es": 
            letra = 32 

        btnContinuar = Button(image=pygame.transform.scale(imgs["caja"], (300, 100)), pos=(640, 250),  text_input=idioma[configJuego["Idioma"]]["OpcionesLvl"]["Reanudar"], font=get_font(letra), base_color="#d7fcd4", hovering_color="#36ddd4")
        btnReiniciar = Button(image=pygame.transform.scale(imgs["caja"], (300, 100)), pos=(640, 400), text_input=idioma[configJuego["Idioma"]]["OpcionesLvl"]["Reiniciar"], font=get_font(letra), base_color="#d7fcd4", hovering_color="#3d91da")
        btnSalir = Button(image=pygame.transform.scale(imgs["caja"], (300, 100)), pos=(640, 550), text_input=idioma[configJuego["Idioma"]]["OpcionesLvl"]["Salir"], font=get_font(letra), base_color="#d7fcd4", hovering_color="Red")

        for button in [btnContinuar, btnReiniciar, btnSalir]: # recorremos los botones
            button.changeColor(OPTIONS_MOUSE_POS) # cambiamos el color de los botones
            button.update(SCREEN) # actualizamos los botones


        pygame.display.update()