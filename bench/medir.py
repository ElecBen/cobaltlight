"""Mide contraste() sobre muchos pares de colores.

Se ejecuta desde la raiz del repo para que `colores` este en la ruta:

    python -m bench.medir
"""
import random
import time

from colores import contraste


def main():
    pares = [((random.randrange(256), random.randrange(256),
               random.randrange(256)),
              (random.randrange(256), random.randrange(256),
               random.randrange(256)))
             for _ in range(50000)]
    arranque = time.perf_counter()
    peor = min(contraste(a, b) for a, b in pares)
    print("%d pares en %.3f s" % (len(pares), time.perf_counter() - arranque))
    print("contraste mas bajo: %.2f" % peor)


if __name__ == "__main__":
    main()
