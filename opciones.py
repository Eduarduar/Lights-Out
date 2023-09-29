import sys, pygame
from assets.defaults.button import Button
from assets.defaults.get_fonts import get_font
from assets.defaults.idioma import cargar_idioma
from assets.defaults.get_imgs import imgs_opciones

idioma = cargar_idioma()
imgs = imgs_opciones()

def opciones(SCREEN , configJuego, LvlsInfo, elementosFondo):
    if configJuego["indiceMusic"] != 1:
        configJuego["indiceMusic"] = 1
        pygame.mixer.music.load(f"assets/songs/musica{configJuego['indiceMusic']}.wav") #cargamos la musica
        pygame.mixer.music.set_volume(configJuego["Volumen"]) #le bajamos el volumen a la musica
        pygame.mixer.music.play(-1) #reproducimos la musica en bucle

    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        #cambiamos el titulo de la ventana
        pygame.display.set_caption(idioma[configJuego["Idioma"]]["Opciones"]["Titulo"])

        #limpiamos para la nueva pantalla
        SCREEN.blit(imgs["azul"], (0, 0))

        #generamos el titulo de la pantalla
        MENU_TEXT = get_font(100).render(idioma[configJuego["Idioma"]]["Opciones"]["Titulo"], True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        # Regresar ------------------------------------
        OPTIONS_BACK = Button(image=None, pos=(50,50), text_input="←", font=get_font(75), base_color="White", hovering_color="Red")

        # Volumen --------------------------------------
        #generamos el texto de las opciones
        txtVolumen = get_font(45).render(idioma[configJuego["Idioma"]]["Opciones"]["Opcion2"], True, "White")
        SCREEN.blit(txtVolumen, (100, 450))
        
        #imprimimos el porcentaje del volumen actual
        txtPorcentaje = get_font(45).render(str(int(configJuego["Volumen"] * 100)) + "%", True, "White")
        SCREEN.blit(txtPorcentaje, (850, 450))
        btnVolumen1 = Button(image=pygame.transform.scale(imgs["caja"], (75, 50)), pos=(1100, 450), text_input="↑", font=get_font(45), base_color="White", hovering_color="Green")
        btnVolumen2 = Button(image=pygame.transform.scale(imgs["caja"], (75, 50)), pos=(1100, 500), text_input="↓", font=get_font(45), base_color="White", hovering_color="Green")

        # idioma --------------------------------------

        #generamos el texto de las opciones
        txtIdiomas = get_font(45).render(idioma[configJuego["Idioma"]]["Opciones"]["Opcion1"], True, "White")
        SCREEN.blit(txtIdiomas, (100, 300))
        btnIdioma1 = Button(image=pygame.transform.scale(imgs["caja"], (350, 100)), pos=(1000, 320), text_input=idioma[configJuego["Idioma"]]["Idioma"], font=get_font(45), base_color="White", hovering_color="Green")

        for button in [btnIdioma1, btnVolumen1, btnVolumen2, OPTIONS_BACK]: # recorremos los botones
            button.changeColor(OPTIONS_MOUSE_POS) # cambiamos el color de los botones
            button.update(SCREEN) # actualizamos los botones

        # detectamos los eventos ----------------------

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN: # detectamos el click del mouse
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):  # detectamos si el click fue en el boton de regresar
                    return SCREEN , configJuego, LvlsInfo, elementosFondo # si fue en el boton de regresar, volvemos a la pantalla de menu principal
                if btnVolumen1.checkForInput(OPTIONS_MOUSE_POS): # detectamos si el click fue en el boton de subir volumen
                    
                    if  configJuego["Volumen"] < 1: # si el volumen es menor a 1, lo subimos
                        configJuego["Volumen"] += 0.01
                        pygame.mixer.music.set_volume(configJuego["Volumen"]) # subimos el volumen
                        
                if btnVolumen2.checkForInput(OPTIONS_MOUSE_POS): # detectamos si el click fue en el boton de bajar volumen

                    if configJuego["Volumen"] > 0: # si el volumen es mayor a 0, lo bajamos
                        configJuego["Volumen"] -= 0.01
                        pygame.mixer.music.set_volume(configJuego["Volumen"]) # bajamos el volumen

                if btnIdioma1.checkForInput(OPTIONS_MOUSE_POS): # detectamos si el click fue en el boton de cambiar idioma
                    if configJuego["Idioma"] == "es": # si el idioma es español, lo cambiamos a ingles
                        configJuego["Idioma"] = "en" 
                    else: # si el idioma es ingles, lo cambiamos a español
                        configJuego["Idioma"] = "es"

                        
            # comprobamos si el valor del volumen tiene mas de 2 decimales
            if len(str(configJuego["Volumen"])) > 4:
                # si el valor numero 5 es un 9, redondeamos el valor del volumen un arriba
                if str(configJuego["Volumen"])[4] == "9":
                    configJuego["Volumen"] = float(str(configJuego["Volumen"])[:4]) + 0.01
                else:
                    configJuego["Volumen"] = float(str(configJuego["Volumen"])[:4])
                pygame.mixer.music.set_volume(configJuego["Volumen"]) # bajamos el volumen

        pygame.display.update()