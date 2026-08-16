import datos

print()
print("=" * 44)
print("  CAPÍTULO 2: EL BOSQUE")
print("=" * 44)
print()

if datos.camino == "izquierda":
    print("Los árboles susurran a tu paso. De pronto, una voz grave dice:")
    print("Responde mi acertijo y te dejaré pasar con un regalo.")
    print()
    print("Acertijo: 'Sin alas vuela, sin boca grita.'")
    print("1) El viento   2) El pájaro   3) La nube")
    respuesta = input("Tu respuesta (1, 2 o 3): ")
    if respuesta == "1":
        print("¡Correcto! El espíritu del bosque te sonríe y te da 10 monedas.")
        datos.oro = datos.oro + 10
    elif respuesta == "2":
        print("El espíritu se ríe. No era correcto, pero te da 5 monedas por intentarlo.")
        datos.oro = datos.oro + 5
    else:
        print("El espíritu niega con la cabeza. Sigue tu camino con las manos vacías.")
else:
    print("El atajo de los lobos está lleno de ramas rotas y huellas.")
    print("Al final del sendero encuentras una bolsa tirada en el barro.")
    recoger = input("¿La recoges? (s / n) ").lower()
    if recoger == "s":
        print("Dentro hay 8 monedas. ¡Suerte en tu camino!")
        datos.oro = datos.oro + 8
        datos.inventario.append("bolsa de cuero")
        print("Añades la 'bolsa de cuero' a tu inventario.")
    else:
        print("Prefieres no tentar a la suerte y sigues de largo.")

print()
print("Al salir del bosque ves la entrada de la cueva.")
print("Antes de entrar, un mercader ha montado su tienda.")
print("Tiene armas a la venta y acepta buen oro.")
print()
print("Estas son sus armas (usa tu oro para comprar):")
print("1) " + datos.ARMAS[0] + "  -> " + str(datos.PRECIOS[0]) + " de oro")
print("2) " + datos.ARMAS[1] + "  -> " + str(datos.PRECIOS[1]) + " de oro")
print("3) " + datos.ARMAS[2] + "  -> " + str(datos.PRECIOS[2]) + " de oro")
print("4) No comprar nada y entrar con las manos vacías")
print()
print("Tienes " + str(datos.oro) + " de oro.")
compra = input("¿Qué quieres comprar? (1, 2, 3 o 4) ")
if compra == "1":
    if datos.oro >= datos.PRECIOS[0]:
        datos.oro = datos.oro - datos.PRECIOS[0]
        datos.arma = datos.ARMAS[0]
        datos.inventario.append(datos.arma)
        print("Compras la espada. " + datos.DESC_ARMAS["espada"])
    else:
        print("No tienes suficiente oro para la espada.")
        print("El mercader se apiada y te da un palo afilado.")
        datos.arma = "palo"
        datos.inventario.append("palo")
elif compra == "2":
    if datos.oro >= datos.PRECIOS[1]:
        datos.oro = datos.oro - datos.PRECIOS[1]
        datos.arma = datos.ARMAS[1]
        datos.inventario.append(datos.arma)
        print("Compras el hacha. " + datos.DESC_ARMAS["hacha"])
    else:
        print("No tienes suficiente oro para el hacha.")
        print("El mercader te regala una piedra afilada.")
        datos.arma = "piedra"
        datos.inventario.append("piedra")
elif compra == "3":
    if datos.oro >= datos.PRECIOS[2]:
        datos.oro = datos.oro - datos.PRECIOS[2]
        datos.arma = datos.ARMAS[2]
        datos.arma_magica = True
        datos.inventario.append(datos.arma)
        print("Compras la varita mágica. " + datos.DESC_ARMAS["varita"])
    else:
        print("No tienes suficiente oro para la varita.")
        print("El mercader suspira y te da una rama torcida.")
        datos.arma = "rama"
        datos.inventario.append("rama")
else:
    print("Entras en la cueva con las manos vacías, pero con valor.")

print()
print("Te acercas a la boca de la cueva. La oscuridad te traga.")
print("Vida: " + str(datos.vida) + " | Ataque: " + str(datos.ataque) + " | Oro: " + str(datos.oro))

import capitulo3
