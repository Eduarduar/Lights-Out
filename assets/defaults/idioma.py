import json

def cargar_idioma():
    idioma = {}
    # Cargamos el archivo de idioma y evitaremos que los caracteres se vean mal
    with open("assets/lenguage/lenguage.json", encoding="utf-8") as f:
        idioma = json.load(f)
    return idioma
