import random

import datos

print("=" * 44)
print("  EL TESORO DE LA CUEVA OSCURA")
print("  Una aventura de texto en Python")
print("=" * 44)
print()
print("Hace muchos años, el rey escondió su tesoro más preciado")
print("en una cueva encantada. Un ejército de monstruos lo robó")
print("y ahora vive en el fondo de la cueva.")
print()
print("El rey ha prometido una gran recompensa a quien lo recupere.")
print()
print("Despiertas en una aldea tranquila. El anciano del pueblo")
print("te observa con una sonrisa.")
print()

datos.nombre = input("El anciano pregunta: ¿cómo te llamas, joven? ")
if datos.nombre == "":
    datos.nombre = "Héroe sin nombre"
print("Encantado, " + datos.nombre + ".")
print()
print("El anciano te dice: elige tu oficio, y te prepararé para la aventura.")
print("1) Guerrero  -> mucha vida, poco ataque")
print("2) Mago      -> poca vida, mucho ataque")
print("3) Ladrón    -> equilibrio")
print()
opcion = input("Escribe el número de tu oficio: ")
if opcion == "1":
    datos.clase = "Guerrero"
    datos.vida = 30
    datos.ataque = 8
    datos.pociones = 3
elif opcion == "2":
    datos.clase = "Mago"
    datos.vida = 20
    datos.ataque = 12
    datos.pociones = 5
elif opcion == "3":
    datos.clase = "Ladrón"
    datos.vida = 25
    datos.ataque = 10
    datos.pociones = 4
else:
    print("Ese número no existe. Serás Ladron por defecto.")
    datos.clase = "Ladron"
    datos.vida = 25
    datos.ataque = 10
    datos.pociones = 4
datos.vida_max = datos.vida
datos.oro = 20

print()
print("Eres un " + datos.clase + " con " + str(datos.vida) + " de vida y " + str(datos.ataque) + " de ataque.")
print("El anciano te da " + str(datos.pociones) + " pociones y " + str(datos.oro) + " monedas de oro.")
print()

print("El anciano señala el mapa de la montaña.")
print("Hay dos caminos para llegar a la cueva:")
print("- izquierda: el bosque de los acertijos, más seguro.")
print("- derecha: el atajo de los lobos, más rápido pero peligroso.")
print()
datos.camino = input("¿Por dónde quieres ir? (izquierda / derecha) ").lower()
if datos.camino == "izquierda":
    print("Te adentras en el bosque de los acertijos.")
elif datos.camino == "derecha":
    print("Te adentras por el atajo de los lobos.")
    print("Un lobo te muerde el brazo. Pierdes 3 de vida.")
    datos.vida = datos.vida - 3
    if datos.vida < 0:
        datos.vida = 0
else:
    print("No entendí, así que eliges el camino de la izquierda.")
    datos.camino = "izquierda"
print()

if datos.vida <= 5:
    print("Con esa poca vida, más te vale ser prudente.")
elif datos.vida <= 10:
    print("Aún puedes continuar, pero con cuidado.")
else:
    print("Te sientes fuerte para la aventura.")

import capitulo2
