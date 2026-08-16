import random

import datos

print()
print("=" * 44)
print("  CAPÍTULO 4: LA BIBLIOTECA DE LAS RUNAS")
print("=" * 44)
print()
print("Tras el salón encuentras una biblioteca llena de libros podridos.")
print("En la pared hay tres piedras con runas. Tres acertijos esconden")
print("tres runas. Si las juntas, ganarás una gran recompensa.")
print()

print("Primer acertijo: '" + datos.PISTAS_RUNAS[0] + "'")
print("1) La luna   2) El oro   3) El fuego")
respuesta1 = input("Tu respuesta (1, 2 o 3): ")
if respuesta1 == "2":
    print("¡La runa de oro brilla y se despega de la pared!")
    datos.runas.add("oro")
else:
    print("La piedra no se mueve. Sigue con la siguiente.")

print()
print("Segundo acertijo: '" + datos.PISTAS_RUNAS[1] + "'")
print("1) La mesa   2) El caballo   3) La silla")
respuesta2 = input("Tu respuesta (1, 2 o 3): ")
if respuesta2 == "3":
    print("¡La runa de madera se enciende y se despega!")
    datos.runas.add("silla")
else:
    print("La piedra permanece muda.")

print()
print("Tercer acertijo: '" + datos.PISTAS_RUNAS[2] + "'")
print("1) El viento   2) El trueno   3) El río")
respuesta3 = input("Tu respuesta (1, 2 o 3): ")
if respuesta3 == "1":
    print("¡La runa de viento levita hasta tu mano!")
    datos.runas.add("viento")
else:
    print("La piedra se queda quieta.")

print()
print("Has reunido " + str(len(datos.runas)) + " runas de 3.")
if len(datos.runas) == 3:
    print("¡Perfecto! Un muro secreto se desliza y aparece una cámara.")
    print("Dentro encuentras un saco con 30 monedas.")
    datos.oro = datos.oro + 30
    datos.inventario.append("saco de monedas")
    print("Oro actual: " + str(datos.oro))
elif len(datos.runas) == 2:
    print("Dos runas emiten un leve destello y te dan 10 monedas.")
    datos.oro = datos.oro + 10
    print("Oro actual: " + str(datos.oro))
elif len(datos.runas) == 1:
    print("Una sola runa no abre nada, pero la guardas como recuerdo.")
else:
    print("Ninguna runa te obedeció. Quizás la magia no es lo tuyo.")

print()
print("Al fondo de la biblioteca hay un pasadizo estrecho.")
print("Oyes el rugido de un ogro al otro lado del puente.")
print("Cruzas y te encuentras con él.")
print()
print("El ogro gruñe: 'Para pasar, paga 15 de oro o hazme reír.'")
print("1) Pagar los 15 de oro")
print("2) Contar un chiste malo")
print("3) Enfrentarte al ogro")
opcion = input("¿Qué haces? (1, 2 o 3) ")
if opcion == "1":
    if datos.oro >= 15:
        datos.oro = datos.oro - 15
        print("Pagas al ogro y cruzas el puente sin problemas.")
    else:
        print("¡No tienes suficiente oro! El ogro se enfada y te da un empujón.")
        datos.vida = datos.vida - 6
        print("Pierdes 6 de vida.")
        if datos.vida <= 0:
            datos.vida = 0
elif opcion == "2":
    print("'¿Qué le dice una iguana a su hija? ¡Iguana hija!'")
    print("El ogro se ríe tanto que se le caen las lágrimas.")
    print("Te deja pasar y de regalo te da 5 monedas.")
    datos.oro = datos.oro + 5
else:
    print("Te lanzas contra el ogro con tu " + datos.arma + ".")
    dado = random.randint(1, 6)
    danio_ogro = datos.ataque + dado
    print("Le causas " + str(danio_ogro) + " de daño.")
    if danio_ogro >= 15:
        print("¡El ogro cae derrotado con un temblor en el puente!")
        datos.derrotados.add("ogro")
        datos.oro = datos.oro + datos.RECOMPENSAS["ogro"]
        print("Ganas " + str(datos.RECOMPENSAS["ogro"]) + " de oro.")
    else:
        print("El ogro te alcanza con su garrote: pierdes 8 de vida.")
        datos.vida = datos.vida - 8
        if datos.vida <= 0:
            datos.vida = 0
        print("Aun así logras hacerlo retroceder y cruzas el puente.")

print()
if datos.vida <= 0:
    print("Estás al borde de la muerte, pero el destino te da otra oportunidad.")
    print("Un hada aparece y te cura 15 de vida.")
    datos.vida = datos.vida + 15
    if datos.vida > datos.vida_max:
        datos.vida = datos.vida_max
    print("Vida actual: " + str(datos.vida))
print("Vida: " + str(datos.vida) + " | Oro: " + str(datos.oro) + " | Runas: " + str(len(datos.runas)))

import capitulo5
