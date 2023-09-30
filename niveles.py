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
reloj = pygame.time.Clock()

edificio1 = ""
edificio2 = ""
edificio3 = ""

def recargarEdificios(LvlsInfo):
    global edificio1
    global edificio2
    global edificio3

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

def mover_fondo(SCREEN, img, elemento, velocidad):
    posX = (elemento["posX"] - velocidad) % 1280
    SCREEN.blit(img, (posX - 1280, elemento["posY"]))
    if posX < 1280:
        SCREEN.blit(img, (posX, elemento["posY"]))
    elemento["posX"] = posX

def niveles(SCREEN, configJuego, LvlsInfo, elementosFondo):
    if configJuego["indiceMusic"] != 1:
        configJuego["indiceMusic"] = 1
        pygame.mixer.music.load(f"assets/songs/musica{configJuego['indiceMusic']}.wav") #cargamos la musica
        pygame.mixer.music.set_volume(configJuego["Volumen"]) #le bajamos el volumen a la musica
        pygame.mixer.music.play(-1) #reproducimos la musica en bucle

    recargarEdificios(LvlsInfo)
        
    btnLvl1 = Button(image=pygame.transform.scale(imgs["caja"], (270, 100)), pos=(300, 200),  text_input=idioma[configJuego["Idioma"]]["Niveles"]["Opcion1"], font=get_font(35), base_color="#d7fcd4", hovering_color="#f9c447")
    btnLvl2 = Button(image=pygame.transform.scale(imgs["caja"], (270, 100)), pos=(660, 200), text_input=idioma[configJuego["Idioma"]]["Niveles"]["Opcion2"], font=get_font(35), base_color="#d7fcd4", hovering_color="#f9c447")
    btnLvl3 = Button(image=pygame.transform.scale(imgs["caja"], (270, 100)), pos=(1050, 200), text_input=idioma[configJuego["Idioma"]]["Niveles"]["Opcion3"], font=get_font(35), base_color="#d7fcd4", hovering_color="#f9c447")
    btnBack = Button(image=None, pos=(50,50), text_input="←", font=get_font(75), base_color="White", hovering_color="Red")

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        mover_fondo(SCREEN ,imgs["ciudad"] ,elementosFondo["ciudad"], 2)
        mover_fondo(SCREEN ,imgs["luna"] ,elementosFondo["luna"], 0.5)
        mover_fondo(SCREEN ,imgs["nube"] ,elementosFondo["nube"], 1)

        # edificios

        SCREEN.blit(edificio1, (0, 0))
        SCREEN.blit(edificio2, (0, 0))
        SCREEN.blit(edificio3, (0, 0))
        SCREEN.blit(imgs["pasto"], (0, 0))
        
        btnBack.update(SCREEN)
        btnLvl1.update(SCREEN)
        btnLvl2.update(SCREEN)
        btnLvl3.update(SCREEN)

        # detectamos los eventos

        for event in pygame.event.get():
            
            # tomando en cuenta los niveles disponibles cambiamos el color de los botones

            if LvlsInfo["LvlDisponibles"]["lvl1"] == True:
                btnLvl1.changeColor(PLAY_MOUSE_POS) 

            if LvlsInfo["LvlDisponibles"]["lvl2"] == True:
                btnLvl2.changeColor(PLAY_MOUSE_POS)

            if LvlsInfo["LvlDisponibles"]["lvl3"] == True:
                btnLvl3.changeColor(PLAY_MOUSE_POS)

            btnBack.changeColor(PLAY_MOUSE_POS)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btnBack.checkForInput(PLAY_MOUSE_POS):
                    return SCREEN , configJuego, LvlsInfo, elementosFondo
                if btnLvl1.checkForInput(PLAY_MOUSE_POS) and LvlsInfo["LvlDisponibles"]["lvl1"] == True:
                    SCREEN , configJuego, LvlsInfo, elementosFondo = pantalla_lvl1(SCREEN , configJuego, LvlsInfo, elementosFondo)
                    recargarEdificios(LvlsInfo)
                if btnLvl2.checkForInput(PLAY_MOUSE_POS) and LvlsInfo["LvlDisponibles"]["lvl2"] == True:
                    SCREEN , configJuego, LvlsInfo, elementosFondo = pantalla_lvl2(SCREEN , configJuego, LvlsInfo, elementosFondo)
                    recargarEdificios(LvlsInfo)
                if btnLvl3.checkForInput(PLAY_MOUSE_POS) and LvlsInfo["LvlDisponibles"]["lvl3"] == True:
                    SCREEN , configJuego, LvlsInfo, elementosFondo = pantalla_lvl3(SCREEN , configJuego, LvlsInfo, elementosFondo)
                    recargarEdificios(LvlsInfo)
                if configJuego["indiceMusic"] != 1:
                    configJuego["indiceMusic"] = 1
                    pygame.mixer.music.load(f"assets/songs/musica{configJuego['indiceMusic']}.wav") #cargamos la musica
                    pygame.mixer.music.set_volume(configJuego["Volumen"]) #le bajamos el volumen a la musica
                    pygame.mixer.music.play(-1) #reproducimos la musica en bucle

        reloj.tick(20)
        pygame.display.update()

# ! Codigo obtimizado

# import sys
# import pygame
# from assets.defaults.button import Button
# from assets.defaults.get_fonts import get_font
# from assets.defaults.idioma import cargar_idioma
# from assets.defaults.get_imgs import imgs_niveles
# from lvl1 import pantalla_lvl1
# from lvl2 import pantalla_lvl2
# from lvl3 import pantalla_lvl3

# def cargar_musica(configJuego):
#     if configJuego["indiceMusic"] != 1:
#         configJuego["indiceMusic"] = 1
#         pygame.mixer.music.load(f"assets/songs/musica{configJuego['indiceMusic']}.wav")
#         pygame.mixer.music.set_volume(configJuego["Volumen"])
#         pygame.mixer.music.play(-1)

# def recargar_edificios(LvlsInfo, imgs):
#     edificios = {}
#     for i in range(1, 4):
#         estado = "estado3" if LvlsInfo["LvlCompletados"]["lvl" + str(i)] else ("estado2" if LvlsInfo["LvlDisponibles"]["lvl" + str(i)] else "estado1")
#         edificios[f"edificio{i}"] = imgs["edificios"]["edificio" + str(i)][estado]
#     return edificios

# def mover_fondo(SCREEN, img, elemento, velocidad):
#     posX = (elemento["posX"] - velocidad) % 1280
#     SCREEN.blit(img, (posX - 1280, elemento["posY"]))
#     if posX < 1280:
#         SCREEN.blit(img, (posX, elemento["posY"]))
#     elemento["posX"] = posX

# def niveles(SCREEN, configJuego, LvlsInfo, elementosFondo):
#     idioma = cargar_idioma()
#     imgs = imgs_niveles()
#     cargar_musica(configJuego)
#     edificios = recargar_edificios(LvlsInfo, imgs)
    
#     btnLvl = []
#     for i, opcion in enumerate([idioma[configJuego["Idioma"]]["Niveles"]["Opcion1"], idioma[configJuego["Idioma"]]["Niveles"]["Opcion2"], idioma[configJuego["Idioma"]]["Niveles"]["Opcion3"]]):
#         btnLvl.append(Button(image=pygame.transform.scale(imgs["caja"], (270, 100)), pos=(300 + i * 360, 200), text_input=opcion, font=get_font(35), base_color="#d7fcd4", hovering_color="#f9c447"))

#     btnBack = Button(image=None, pos=(50,50), text_input="←", font=get_font(75), base_color="White", hovering_color="Red")

#     while True:
#         PLAY_MOUSE_POS = pygame.mouse.get_pos()

#         for elemento in ["ciudad", "luna", "nube"]:
#             mover_fondo(SCREEN, imgs[elemento], elementosFondo[elemento], 2 if elemento == "ciudad" else 0.5 if elemento == "luna" else 1)

#         for edificio in edificios.values():
#             SCREEN.blit(edificio, (0, 0))
#         SCREEN.blit(imgs["pasto"], (0, 0))
        
#         btnBack.update(SCREEN)
#         for btn in btnLvl:
#             btn.changeColor(PLAY_MOUSE_POS)
#             btn.update(SCREEN)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if btnBack.checkForInput(PLAY_MOUSE_POS):
#                     return SCREEN, configJuego, LvlsInfo, elementosFondo
#                 for i, btn in enumerate(btnLvl):
#                     if btn.checkForInput(PLAY_MOUSE_POS) and LvlsInfo["LvlDisponibles"]["lvl" + str(i + 1)]:
#                         pantalla = globals()["pantalla_lvl" + str(i + 1)]
#                         SCREEN, configJuego, LvlsInfo, elementosFondo = pantalla(SCREEN, configJuego, LvlsInfo, elementosFondo)
#                         edificios = recargar_edificios(LvlsInfo, imgs)
#                         cargar_musica(configJuego)
                        
#         pygame.time.Clock().tick(20)
#         pygame.display.update()