import random

import datos

print()
print("=" * 44)
print("  CAPÍTULO 5: LA MAZMORRA")
print("=" * 44)
print()
print("Al final del puente, una escalera de piedra baja a una mazmorra.")
print("Huele a humedad y algo brilla en la oscuridad.")
print()
print("Un esqueleto armado con un escudo bloquea el pasillo.")
print("1) Atacar")
print("2) Intentar pasar esquivando")
print("3) Retroceder y beber una poción")
opcion = input("¿Qué haces? (1, 2 o 3) ")
if opcion == "1":
    dado = random.randint(1, 6)
    danio_esqueleto = datos.ataque + dado
    print("Golpeas al esqueleto con tu " + datos.arma + ": " + str(danio_esqueleto) + " de daño.")
    if danio_esqueleto >= 12:
        print("El esqueleto se desmorona en huesos. ¡Derrotado!")
        datos.derrotados.add("esqueleto")
        datos.oro = datos.oro + datos.RECOMPENSAS["esqueleto"]
        print("Ganas " + str(datos.RECOMPENSAS["esqueleto"]) + " de oro.")
    else:
        print("El esqueleto contraataca: pierdes 6 de vida.")
        datos.vida = datos.vida - 6
        if datos.vida <= 0:
            datos.vida = 0
        print("Al segundo golpe lo derrotas. Ganas 10 de oro.")
        datos.derrotados.add("esqueleto")
        datos.oro = datos.oro + 10
elif opcion == "2":
    if datos.clase == "Ladrón":
        print("Eres un ladrón: te deslizas entre sus costillas y pasas sin pelear.")
        print("El esqueleto ni siquiera se entera.")
    else:
        print("Intentas esquivar, pero el escudo te golpea: pierdes 5 de vida.")
        datos.vida = datos.vida - 5
        if datos.vida <= 0:
            datos.vida = 0
        print("El esqueleto te deja pasar de mala gana.")
elif opcion == "3":
    if datos.pociones > 0:
        datos.pociones = datos.pociones - 1
        datos.vida = datos.vida + 10
        if datos.vida > datos.vida_max:
            datos.vida = datos.vida_max
        print("Bebes una poción y recuperas 10 de vida. Vida: " + str(datos.vida) + ".")
        print("Con renovada energía derrotas al esqueleto de un golpe.")
        datos.derrotados.add("esqueleto")
        datos.oro = datos.oro + datos.RECOMPENSAS["esqueleto"]
        print("Ganas " + str(datos.RECOMPENSAS["esqueleto"]) + " de oro.")
    else:
        print("No te quedan pociones. El esqueleto ríe y te hace perder 5 de vida.")
        datos.vida = datos.vida - 5
        if datos.vida <= 0:
            datos.vida = 0

print()
print("En una celda abierta encuentras una caja de madera.")
abrir = input("¿Quieres abrirla? (s / n) ").lower()
if abrir == "s":
    print("¡Trampa! Una flecha te roza el hombro: pierdes 4 de vida.")
    datos.vida = datos.vida - 4
    if datos.vida <= 0:
        datos.vida = 0
    print("Dentro de la caja hay una llave dorada. Brilla con luz propia.")
    datos.inventario.append("llave dorada")
else:
    print("La dejas cerrada. El que avisa no es traidor.")

print()
print("Al fondo de la mazmorra hay una puerta enorme de hierro.")
print("Un cartel dice: 'El tesoro del rey está detrás. Pero el dragón")
print("lo vigila. Elige bien tu siguiente paso.'")
print()
if "llave dorada" in datos.inventario and datos.vida > 8:
    print("Tienes la llave dorada y vida de sobra para enfrentarte al dragón.")
elif "llave dorada" in datos.inventario:
    print("Tienes la llave dorada, pero estás muy herido. Ten cuidado.")
else:
    print("Sin llave dorada, tendrás que abrir la puerta con pura fuerza.")

import capitulo6
