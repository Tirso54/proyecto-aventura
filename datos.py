nombre = ""
clase = ""
vida = 0
vida_max = 0
ataque = 0
oro = 0
pociones = 0

inventario = []
derrotados = set()
runas = set()

camino = ""
arma = ""
arma_magica = ""

CLASES = ("Guerrero", "Mago", "Ladrón")
CAMINOS = ("izquierda", "derecha")
ARMAS = ("espada", "hacha", "varita")
PRECIOS = (15, 20, 25)

DESC_ARMAS = {
    "espada": "Una espada afilada, da +3 de ataque.",
    "hacha": "Un hacha pesada, da +4 de ataque.",
    "varita": "Una varita mágica, da +5 de ataque.",
}

RECOMPENSAS = {
    "murcielago": 5,
    "esqueleto": 10,
    "ogro": 20,
    "dragon": 100,
}

PISTAS_RUNAS = (
    "Brilla como el sol, y todos la adoran.",
    "Tiene patas, pero no camina.",
    "Sin alas vuela, sin boca grita.",
)

RUNAS_CORRECTAS = ("oro", "silla", "viento")
