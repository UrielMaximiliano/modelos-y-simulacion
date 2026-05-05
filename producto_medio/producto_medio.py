"""
Metodo de producto medio
1) Yi = Xi * Xi+1
2) Tomar los D digitos centrales de Yi
3) Ri = 0.<digitos centrales>
"""

import sys


def digitos_centrales(numero, d):
    texto = str(numero).zfill(2 * d)
    inicio = (len(texto) - d) // 2
    return texto[inicio : inicio + d]


def generar_producto_medio(x0, x1, d, n):
    if not all(isinstance(x, int) for x in (x0, x1, d, n)):
        raise ValueError("Todos los parametros deben ser enteros.")

    if d < 2:
        raise ValueError("d debe ser mayor o igual que 2.")

    if n <= 0:
        raise ValueError("n debe ser mayor que 0.")

    limite = 10**d
    if x0 < 0 or x0 >= limite or x1 < 0 or x1 >= limite:
        raise ValueError("x0 y x1 deben tener como maximo d digitos.")

    resultados = []
    xi = x0
    xi1 = x1

    for i in range(1, n + 1):
        yi = xi * xi1
        x_sig_texto = digitos_centrales(yi, d)
        x_sig = int(x_sig_texto)

        resultados.append(
            {
                "i": i,
                "xi": str(xi).zfill(d),
                "xi1": str(xi1).zfill(d),
                "yi": str(yi).zfill(2 * d),
                "xSig": x_sig_texto,
                "ri": f"0.{x_sig_texto}",
            }
        )

        xi = xi1
        xi1 = x_sig

    return resultados


def imprimir_tabla(resultados):
    print(f"{'i':>3} {'Xi':>8} {'Xi+1':>8} {'Yi':>12} {'Xsig':>8} {'Ri':>8}")
    print("-" * 54)
    for fila in resultados:
        print(
            f"{fila['i']:>3} "
            f"{fila['xi']:>8} "
            f"{fila['xi1']:>8} "
            f"{fila['yi']:>12} "
            f"{fila['xSig']:>8} "
            f"{fila['ri']:>8}"
        )


def mostrar_uso():
    print("Uso:")
    print("  python producto_medio.py <x0> <x1> <d> <n>")
    print("  python producto_medio.py  (modo interactivo)")
    print("Ejemplo:")
    print("  python producto_medio.py 5015 5734 4 10")


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada invalida. Escribi un numero entero.")


def main():
    try:
        if len(sys.argv) == 5:
            x0, x1, d, n = map(int, sys.argv[1:])
        elif len(sys.argv) == 1:
            print("Modo interactivo - Producto medio")
            x0 = leer_entero("Primera semilla (x0): ")
            x1 = leer_entero("Segunda semilla (x1): ")
            d = leer_entero("Cantidad de digitos (d): ")
            n = leer_entero("Cantidad de numeros (n): ")
        else:
            mostrar_uso()
            return 1

        tabla = generar_producto_medio(x0, x1, d, n)
        imprimir_tabla(tabla)
        return 0
    except ValueError as error:
        print(f"Error: {error}")
        mostrar_uso()
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
