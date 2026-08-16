# EL TESORO DE LA CUEVA OSCURA

Una aventura de texto interactiva escrita en Python **sin funciones (`def`) ni bucles (`for` / `while`)**. Solo usa lo básico: `if / elif / else`, `print`, `input`, variables, listas, sets, tuplas, diccionarios y un poco de lógica.

## Cómo ejecutarlo

Necesitas Python 3. Abre una terminal en esta carpeta y escribe:

```bash
python3 aventura.py
```

## Historia

El rey ha perdido su tesoro más preciado. Un ejército de monstruos lo robó
y se escondió con él en lo más profundo de una cueva encantada. Tú debes
recuperarlo: atravesar el bosque, comprar armas, resolver acertijos, luchar
contra murciélagos, esqueletos y un ogro... y llegar a la cámara del dragón.

## Contenidos que se practican

- Variables y tipos de datos
- `print()` y `input()`
- Condicionales `if / elif / else` con lógica (`and`, `or`, `in`, comparaciones)
- Listas: guardar objetos recogidos, añadir con `.append()`, quitar con `.pop()`
- Sets: enemigos derrotados, runas conseguidas, `.add()`
- Tuplas: datos fijos como nombres de armas, precios y acertijos
- Diccionarios: descripciones de armas y recompensas
- Módulo `random` para el azar de los combates
- Encadenar módulos importando el siguiente capítulo

## Estructura del proyecto

| Archivo | Contenido |
|---|---|
| `aventura.py` | Punto de entrada del juego |
| `datos.py` | Todas las variables, listas, sets, tuplas y diccionarios |
| `capitulo1.py` | La aldea: creas tu héroe y eliges camino |
| `capitulo2.py` | El bosque: acertijo o atajo, y la tienda del mercader |
| `capitulo3.py` | El gran salón: combate contra el murciélago |
| `capitulo4.py` | La biblioteca de las runas: acertijos y el ogro del puente |
| `capitulo5.py` | La mazmorra: esqueleto, trampas y la llave dorada |
| `capitulo6.py` | La cámara del dragón: la batalla final |
| `capitulo7.py` | Epílogo y resumen de tu aventura |

## Consejos de juego

- Responde los acertijos de la biblioteca para conseguir las 3 runas.
- Guarda oro para comprar la varita mágica: es el arma más poderosa contra el dragón.
- Si tu vida baja de 0, un hada te dará una segunda oportunidad en la mazmorra.
- Hay varios finales según cómo actúes. ¡Intenta descubrirlos todos!

## Requisitos

- Python 3.6 o superior
- Sin dependencias externas
