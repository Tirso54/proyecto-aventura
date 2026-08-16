import datos

print()
print("*" * 44)
print("  CAPÍTULO 7: EPÍLOGO")
print("*" * 44)
print()
print("Sales de la cueva con el tesoro del rey a cuestas.")
print("El sol te deslumbra. La aldea te recibe con aplausos.")
print()

if "dragon" in datos.derrotados and datos.vida > 5:
    print("--- FINAL GLORIOSO ---")
    print("Derrotaste al dragón y volviste con vida.")
    print("El rey te nombra Héroe del Reino y te da una medalla de oro.")
    datos.inventario.append("medalla de oro")
elif "dragon" in datos.derrotados and datos.vida <= 5:
    print("--- FINAL HEROICO ---")
    print("Derrotaste al dragón, pero volviste herido.")
    print("El rey te agradece con oro, pero te pide que descanses.")
elif datos.vida <= 0:
    print("--- FINAL TRISTE ---")
    print("No conseguiste superar todas las heridas.")
    print("La aldea lloró tu partida, pero recordarán tu valor.")
elif len(datos.derrotados) >= 3:
    print("--- FINAL ASTUTO ---")
    print("Sin matar al dragón, lograste llevarte el tesoro.")
    print("El rey aplaude tu ingenio y te nombra consejero real.")
else:
    print("--- FINAL SENCILLO ---")
    print("El tesoro llega al rey y la aldea celebra.")
    print("Quizás otra gran aventura te espere mañana.")

print()
print("=" * 44)
print("  RESUMEN DE TU AVENTURA")
print("=" * 44)
print("Héroe      : " + datos.nombre)
print("Clase      : " + datos.clase)
print("Vida final : " + str(datos.vida) + " / " + str(datos.vida_max))
print("Oro final  : " + str(datos.oro))
print("Pociones   : " + str(datos.pociones))
print("Objetos    : " + str(len(datos.inventario)))
if len(datos.inventario) > 0:
    print("Inventario : " + str(datos.inventario))
print("Enemigos derrotados: " + str(len(datos.derrotados)))
print("Runas      : " + str(len(datos.runas)))
print()
print("Gracias por jugar a EL TESORO DE LA CUEVA OSCURA.")
print("Pulsa ENTER para terminar.")
input()
