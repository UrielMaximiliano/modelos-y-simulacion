"""
Metodo congruencial multiplicativo
Formula: X(i+1) = (a * Xi) mod m
Numero pseudoaleatorio: Ri = Xi / m
"""

import sys


def generar_congruencial_multiplicativo(semilla, a, m, n):
    if not all(isinstance(x, int) for x in (semilla, a, m, n)):
        raise ValueError("Todos los parametros deben ser enteros.")

    if m <= 1:
        raise ValueError("m debe ser mayor que 1.")

    if semilla <= 0 or semilla >= m:
        raise ValueError("La semilla debe cumplir: 0 < semilla < m.")

    if a <= 0 or a >= m:
        raise ValueError("a debe cumplir: 0 < a < m.")

    if n <= 0:
        raise ValueError("n debe ser mayor que 0.")

    resultados = []
    xi = semilla

    for i in range(1, n + 1):
        xi = (a * xi) % m
        resultados.append(
            {
                "i": i,
                "xi": xi,
                "ri": f"{xi / m:.6f}",
            }
        )

    return resultados


def imprimir_tabla(resultados):
    print(f"{'i':>3} {'Xi':>10} {'Ri':>10}")
    print("-" * 26)
    for fila in resultados:
        print(f"{fila['i']:>3} {fila['xi']:>10} {fila['ri']:>10}")


def mostrar_uso():
    print("Uso:")
    print("  python congruencial_multiplicativo.py <semilla> <a> <m> <n>")
    print("  python congruencial_multiplicativo.py  (modo interactivo)")
    print("Ejemplo:")
    print("  python congruencial_multiplicativo.py 7 5 32 10")


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada invalida. Escribi un numero entero.")


def main():
    try:
        if len(sys.argv) == 5:
            semilla, a, m, n = map(int, sys.argv[1:])
        elif len(sys.argv) == 1:
            print("Modo interactivo - Congruencial multiplicativo")
            semilla = leer_entero("Semilla (X0): ")
            a = leer_entero("Multiplicador (a): ")
            m = leer_entero("Modulo (m): ")
            n = leer_entero("Cantidad de numeros (n): ")
        else:
            mostrar_uso()
            return 1

        tabla = generar_congruencial_multiplicativo(semilla, a, m, n)
        imprimir_tabla(tabla)
        return 0
    except ValueError as error:
        print(f"Error: {error}")
        mostrar_uso()
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
