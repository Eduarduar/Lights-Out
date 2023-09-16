import sys, pygame, random
from assets.defaults.idioma import cargar_idioma
from assets.defaults.get_fonts import get_font
from menu_principal import menu_principal

idioma = cargar_idioma()

def pantalla_de_carga(SCREEN, configJuego, LvlsInfo, elementosFondo):
    while True:

        # creamos un bucle for que repita el codigo de abajo 4 veces donde la variable i empieze en 1

        cantidad = random.randint(1, 3)
        for i in range(1, cantidad):
            for e in range(1, 5):
                SCREEN.fill("black")
                CARGA_TEXT = get_font(50).render(idioma[configJuego["Idioma"]][f"Carga"][f"Carga{e}"], True, "White")
                CARGA_RECT = CARGA_TEXT.get_rect(center=(640, 360))

                SCREEN.blit(CARGA_TEXT, CARGA_RECT)

                pygame.display.update()

                # despuesde 3 segundos cambiamos a la pantalla de menu principal
                pygame.time.delay(300)
        
        menu_principal(SCREEN, configJuego, LvlsInfo, elementosFondo)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()