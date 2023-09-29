import sys, pygame
from assets.defaults.button import Button
from assets.defaults.get_fonts import get_font
from assets.defaults.idioma import cargar_idioma
from assets.defaults.get_imgs import imgs_niveles
from lvl1 import pantalla_lvl1
from lvl2 import pantalla_lvl2
from lvl3 import pantalla_lvl3

idioma = cargar_idioma()
imgs = imgs_niveles()


def niveles(SCREEN , configJuego, LvlsInfo, elementosFondo):
    if configJuego["indiceMusic"] != 1:
        configJuego["indiceMusic"] = 1
        pygame.mixer.music.load(f"assets/songs/musica{configJuego['indiceMusic']}.wav") #cargamos la musica
        pygame.mixer.music.set_volume(configJuego["Volumen"]) #le bajamos el volumen a la musica
        pygame.mixer.music.play(-1) #reproducimos la musica en bucle

    # creamos las variables donde almacenaremos nuestras variables de los edificios

    edificio1 = ""
    edificio2 = ""
    edificio3 = ""

    # identificamos que edificios estan disponibles y cuales no

    if LvlsInfo["LvlDisponibles"]["lvl1"] == True:
        if LvlsInfo["LvlCompletados"]["lvl1"] == True:
            edificio1 = imgs["edificios"]["edificio1"]["estado2"]
        else:
            edificio1 = imgs["edificios"]["edificio1"]["estado1"]

    if LvlsInfo["LvlDisponibles"]["lvl2"] == True:
        if LvlsInfo["LvlCompletados"]["lvl2"] == True:
            edificio2 = imgs["edificios"]["edificio2"]["estado3"]
        else:
            edificio2 = imgs["edificios"]["edificio2"]["estado2"]
    else:
        edificio2 = imgs["edificios"]["edificio2"]["estado1"]

    if LvlsInfo["LvlDisponibles"]["lvl3"] == True:
        if LvlsInfo["LvlCompletados"]["lvl3"] == True:
            edificio3 = imgs["edificios"]["edificio3"]["estado3"]
        else:
            edificio3 = imgs["edificios"]["edificio3"]["estado2"]
    else:
        edificio3 = imgs["edificios"]["edificio3"]["estado1"]

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()    

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

        # edificios

        SCREEN.blit(edificio1, (0, 0))
        SCREEN.blit(edificio2, (0, 0))
        SCREEN.blit(edificio3, (0, 0))
        SCREEN.blit(imgs["pasto"], (0, 0))

        # creamos 3 botonos correspondientes a los niveles

        btnLvl1 = Button(image=pygame.transform.scale(imgs["caja"], (270, 100)), pos=(300, 200),  text_input=idioma[configJuego["Idioma"]]["Niveles"]["Opcion1"], font=get_font(40), base_color="#d7fcd4", hovering_color="#f9c447")
        btnLvl2 = Button(image=pygame.transform.scale(imgs["caja"], (270, 100)), pos=(660, 200), text_input=idioma[configJuego["Idioma"]]["Niveles"]["Opcion2"], font=get_font(40), base_color="#d7fcd4", hovering_color="#f9c447")
        btnLvl3 = Button(image=pygame.transform.scale(imgs["caja"], (270, 100)), pos=(1050, 200), text_input=idioma[configJuego["Idioma"]]["Niveles"]["Opcion3"], font=get_font(40), base_color="#d7fcd4", hovering_color="#f9c447")

        # imprimimos el boton de regresar
        
        btnBack = Button(image=None, pos=(50,50), text_input="←", font=get_font(75), base_color="White", hovering_color="Red")
        btnBack.changeColor(PLAY_MOUSE_POS)
        btnBack.update(SCREEN)

        # tomando en cuenta los niveles disponibles cambiamos el color de los botones

        if LvlsInfo["LvlDisponibles"]["lvl1"] == True:
            btnLvl1.changeColor(PLAY_MOUSE_POS) 

        if LvlsInfo["LvlDisponibles"]["lvl2"] == True:
            btnLvl2.changeColor(PLAY_MOUSE_POS)

        if LvlsInfo["LvlDisponibles"]["lvl3"] == True:
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
                    return SCREEN , configJuego, LvlsInfo, elementosFondo
                if btnLvl1.checkForInput(PLAY_MOUSE_POS) and LvlsInfo["LvlDisponibles"]["lvl1"] == True:
                    pantalla_lvl1(SCREEN , configJuego, LvlsInfo, elementosFondo)
                if btnLvl2.checkForInput(PLAY_MOUSE_POS) and LvlsInfo["LvlDisponibles"]["lvl2"] == True:
                    pantalla_lvl2(SCREEN , configJuego, LvlsInfo, elementosFondo)
                if btnLvl3.checkForInput(PLAY_MOUSE_POS) and LvlsInfo["LvlDisponibles"]["lvl3"] == True:
                    pantalla_lvl3(SCREEN , configJuego, LvlsInfo, elementosFondo)
                if configJuego["indiceMusic"] != 1:
                    configJuego["indiceMusic"] = 1
                    pygame.mixer.music.load(f"assets/songs/musica{configJuego['indiceMusic']}.wav") #cargamos la musica
                    pygame.mixer.music.set_volume(configJuego["Volumen"]) #le bajamos el volumen a la musica
                    pygame.mixer.music.play(-1) #reproducimos la musica en bucle

        pygame.display.update()
