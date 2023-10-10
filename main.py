import pygame
from menu_principal import menu_principal
from intro import intro

print("Lights Out - v0.1.0")
# convertimos el input a mayusculas para evitar errores
sexo = input("Elija el sexo (H/M): ")

configJuego = {
    "Idioma": "es",
    "Volumen": 0.50,
    "indiceMusic": 0,
    "historia": True,
    "personaje": "mujer"
}

if sexo == "m" or sexo == "M":
    configJuego["personaje"] = "mujer"
else:
    configJuego["personaje"] = "hombre"

elementosFondo = {
    "luna": {
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
    pygame.display.set_caption("Lights Out")

    intro(SCREEN)
    menu_principal(SCREEN, configJuego, LvlsInfo, elementosFondo)

main()
