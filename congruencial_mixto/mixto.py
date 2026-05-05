"""
Metodo Congruencial Lineal Mixto (MCL).

Formula:
    X_(n+1) = (a * X_n + c) mod m
Normalizacion:
    U_n = X_n / m
"""


def congruencial_mixto(x0: int, a: int, c: int, m: int, cantidad: int):
    """
    Genera una secuencia con el metodo congruencial mixto.
    Devuelve una lista con: n, x_n, a*x_n+c, x_n+1, u_n+1.
    """
    if m <= 0:
        raise ValueError("m debe ser mayor a 0.")
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor a 0.")
    if x0 < 0 or a < 0 or c < 0:
        raise ValueError("x0, a y c deben ser no negativos.")

    resultados = []
    x_n = x0

    for i in range(cantidad):
        expresion = a * x_n + c
        siguiente = expresion % m
        u_n = siguiente / m

        resultados.append(
            {
                "n": i,
                "x_n": x_n,
                "ax_mas_c": expresion,
                "x_sig": siguiente,
                "u_n": u_n,
            }
        )

        # El siguiente valor pasa a ser el actual en la proxima iteracion.
        x_n = siguiente

    return resultados


def imprimir_tabla(resultados):
    """Imprime la secuencia en formato de tabla."""
    print(f"{'n':>3} {'x_n':>6} {'a*x_n+c':>10} {'x_n+1':>8} {'u_n+1':>10}")
    print("-" * 45)
    for fila in resultados:
        print(
            f"{fila['n']:>3} {fila['x_n']:>6} {fila['ax_mas_c']:>10} "
            f"{fila['x_sig']:>8} {fila['u_n']:>10.6f}"
        )


def pedir_entero(mensaje: str) -> int:
    """Pide un entero por consola hasta que el usuario ingrese uno valido."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada invalida. Debes ingresar un numero entero.")


if __name__ == "__main__":
    print("Metodo Congruencial Lineal Mixto")
    print("-" * 40)

    # Entradas para ejecutar el metodo desde consola.
    x0 = pedir_entero("Semilla inicial x0: ")
    a = pedir_entero("Multiplicador a: ")
    c = pedir_entero("Constante aditiva c: ")
    m = pedir_entero("Modulo m: ")
    cantidad = pedir_entero("Cantidad de numeros a generar: ")

    serie = congruencial_mixto(x0, a, c, m, cantidad)
    imprimir_tabla(serie)
