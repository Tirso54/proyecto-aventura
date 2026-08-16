import random

import datos

print()
print("=" * 44)
print("  CAPÍTULO 3: EL GRAN SALÓN")
print("=" * 44)
print()
print("Un salón enorme se abre ante ti. Columnas rotas y polvo")
print("por todas partes. Un aleteo rasga el silencio.")
print()
print("¡Un murciélago gigante se lanza contra ti!")
print()

ataque_total = datos.ataque
if datos.arma == "espada":
    ataque_total = ataque_total + 3
elif datos.arma == "hacha":
    ataque_total = ataque_total + 4
elif datos.arma == "varita":
    ataque_total = ataque_total + 5
elif datos.arma == "palo":
    ataque_total = ataque_total + 1
elif datos.arma == "piedra":
    ataque_total = ataque_total + 2

print("Tu ataque ahora es " + str(ataque_total) + ".")
print("¿Qué haces?")
print("1) Atacar con todo")
print("2) Beber una poción y después atacar")
opcion = input("Tu elección (1 o 2): ")
if opcion == "2" and datos.pociones > 0:
    datos.pociones = datos.pociones - 1
    datos.vida = datos.vida + 10
    if datos.vida > datos.vida_max:
        datos.vida = datos.vida_max
    print("Bebes la poción. Vida actual: " + str(datos.vida) + ".")
elif opcion == "2":
    print("¡No te quedan pociones! Atacas igualmente.")
else:
    print("Atacas sin pensarlo dos veces.")

dado = random.randint(1, 6)
danio_murcielago = ataque_total + dado
print("Golpeas al murciélago con fuerza: " + str(danio_murcielago) + " de daño.")
if danio_murcielago >= 10:
    print("¡El murciélago cae al suelo derrotado!")
    datos.derrotados.add("murcielago")
    datos.oro = datos.oro + datos.RECOMPENSAS["murcielago"]
    print("Ganas " + str(datos.RECOMPENSAS["murcielago"]) + " de oro.")
else:
    print("El murciélago esquiva el golpe y te muerde.")
    print("Pierdes 4 de vida.")
    datos.vida = datos.vida - 4
    if datos.vida <= 0:
        datos.vida = 0
    print("Respiras hondo y lo rematas. ¡Derrotado!")
    datos.derrotados.add("murcielago")
    datos.oro = datos.oro + datos.RECOMPENSAS["murcielago"]
    print("Ganas " + str(datos.RECOMPENSAS["murcielago"]) + " de oro.")

print()
if "murcielago" in datos.derrotados:
    print("El salón queda en silencio. Encuentras un cofre pequeño.")
    print("¿Lo abres? (s / n)")
    abrir = input("> ").lower()
    if abrir == "s":
        print("Dentro hay 12 monedas y una llave de hierro.")
        datos.oro = datos.oro + 12
        datos.inventario.append("llave de hierro")
    else:
        print("Lo dejas donde está. La precaución también es valentía.")
else:
    print("Algo se esconde en la penumbra...")

print()
print("Oro actual: " + str(datos.oro) + " | Vida: " + str(datos.vida) + " | Pociones: " + str(datos.pociones))
print("Inventario: " + str(datos.inventario))
print("Enemigos derrotados: " + str(len(datos.derrotados)))

import capitulo4
