import random

import datos

print()
print("=" * 44)
print("  CAPÍTULO 6: LA CÁMARA DEL DRAGÓN")
print("=" * 44)
print()
print("Abres la puerta de hierro con un chirrido. Una cámara enorme,")
print("llena de monedas de oro, joyas y cofres. Y en el centro...")
print("un dragón verde dormita sobre el tesoro.")
print()
print("El tesoro del rey es tuyo si logras pasar. ¿Cómo actuarás?")
print("1) Atacar al dragón directamente")
print("2) Esperar a que despierte y negociar")
print("3) Deslizarte en silencio para robar el tesoro")
opcion = input("Tu elección (1, 2 o 3) ")
print()

if opcion == "1":
    print("Te lanzas contra el dragón con tu " + datos.arma + ".")
    dado = random.randint(1, 6)
    danio_dragon = datos.ataque + dado
    if datos.arma == "varita":
        danio_dragon = danio_dragon + 5
        print("La varita lanza un rayo mágico de energía extra.")
    elif datos.arma == "hacha":
        danio_dragon = danio_dragon + 4
    elif datos.arma == "espada":
        danio_dragon = danio_dragon + 3
    print("Causas " + str(danio_dragon) + " de daño al dragón.")
    if danio_dragon >= 20 and "varita" == datos.arma:
        print("¡El dragón ruge y cae! El tesoro queda sin guardián.")
        datos.derrotados.add("dragon")
        datos.oro = datos.oro + datos.RECOMPENSAS["dragon"]
        print("Ganas " + str(datos.RECOMPENSAS["dragon"]) + " de oro.")
    elif danio_dragon >= 20:
        print("¡Golpe brutal! El dragón cae derrotado.")
        datos.derrotados.add("dragon")
        datos.oro = datos.oro + datos.RECOMPENSAS["dragon"]
        print("Ganas " + str(datos.RECOMPENSAS["dragon"]) + " de oro.")
    else:
        print("El dragón despierte furioso y te abrasa con su aliento.")
        print("Pierdes 12 de vida.")
        datos.vida = datos.vida - 12
        if datos.vida <= 0:
            datos.vida = 0
        print("Aun así, le das el golpe final. ¡El dragón cae!")
        datos.derrotados.add("dragon")
        datos.oro = datos.oro + datos.RECOMPENSAS["dragon"]
        print("Ganas " + str(datos.RECOMPENSAS["dragon"]) + " de oro.")

elif opcion == "2":
    print("El dragón abre un ojo y te mira.")
    print("'¿Negociar? Está bien, me aburro. Dame 30 de oro y un objeto'")
    print("'valioso de tu inventario, y te dejaré coger el tesoro.'")
    if datos.oro >= 30 and len(datos.inventario) > 0:
        datos.oro = datos.oro - 30
        objeto_regalado = datos.inventario.pop()
        print("Le das 30 de oro y '" + objeto_regalado + "'.")
        print("El dragón sonríe y aparta su cola del tesoro.")
        print("Consigues el tesoro sin derramar sangre.")
    else:
        print("No tienes suficiente oro o inventario. El dragón se ríe.")
        print("Te da un zarpazo: pierdes 8 de vida.")
        datos.vida = datos.vida - 8
        if datos.vida <= 0:
            datos.vida = 0
        print("El dragón te deja escapar, pero el tesoro sigue custodiado.")
        datos.oro = datos.oro + 0

else:
    print("Te deslizas como una sombra entre las monedas.")
    print("Un ruido... el dragón abre un ojo y te ve.")
    print("¡Te atrapa con su garra! Pierdes 10 de vida.")
    datos.vida = datos.vida - 10
    if datos.vida <= 0:
        datos.vida = 0
    print("El dragón, impresionado por tu valor, te suelta.")
    print("Te quedas con el tesoro en las manos.")
    datos.oro = datos.oro + 50

print()
print("Vida: " + str(datos.vida) + " | Oro: " + str(datos.oro))
print("Dragón derrotado: " + str("dragon" in datos.derrotados))

import capitulo7
