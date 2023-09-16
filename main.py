import pygame
from carga import pantalla_de_carga

configJuego = {
    "Idioma": "es",
    "Volumen": 0.50,
    "indiceMusic": 0,
}

elementosFondo = {
    "Luna": {
        "posX" : 1200,
        "posY" : 30
    },
    "nube": {
        "posX" : 0,
        "posY" : 80
    },
    "ciudad": {
        "posX" : -320,
        "posY" : 0
    }
}

LvlsInfo = {
    "LvlDisponibles" : {
        "lvl1": True,
        "lvl2": False,
        "lvl3": False
    },
    "LvlCompletados":{
        "lvl1": False,
        "lvl2": False,
        "lvl3": False
    }
}

def main():
    pygame.init()
    SCREEN = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Light Out")

    pantalla_de_carga(SCREEN, configJuego, LvlsInfo, elementosFondo)

if __name__ == "__main__":
    main()
