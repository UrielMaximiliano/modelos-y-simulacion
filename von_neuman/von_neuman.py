"""
Metodo del Cuadrado Medio (Von Neumann).

Genera numeros pseudoaleatorios a partir de una semilla de n digitos:
1) Se eleva la semilla al cuadrado.
2) Se completa con ceros hasta 2n digitos.
3) Se toman los n digitos centrales como nueva semilla.
4) Se normaliza dividiendo por 10^n.
"""


def extraer_centro(numero_texto: str, n: int) -> str:
    """Devuelve los n digitos centrales de un texto de longitud 2n."""
    inicio = (len(numero_texto) - n) // 2
    fin = inicio + n
    return numero_texto[inicio:fin]


def von_neumann(semilla: int, n_digitos: int, cantidad: int):
    """
    Ejecuta el metodo de Von Neumann y devuelve una lista de iteraciones.
    Cada elemento tiene: n, x_n, x_n^2, centro, u_n.
    """
    if semilla <= 0:
        raise ValueError("La semilla debe ser un entero positivo.")
    if len(str(semilla)) != n_digitos:
        raise ValueError("La semilla debe tener exactamente n_digitos.")
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor a 0.")

    resultados = []
    x_n = semilla

    for i in range(cantidad):
        cuadrado = x_n**2

        # zfill agrega ceros a la izquierda para forzar longitud 2n.
        cuadrado_texto = str(cuadrado).zfill(2 * n_digitos)

        # Tomamos la parte central (n digitos) como nueva semilla.
        centro_texto = extraer_centro(cuadrado_texto, n_digitos)
        siguiente = int(centro_texto)

        # Normalizacion al rango [0,1) usando 10^n.
        u_n = siguiente / (10**n_digitos)

        resultados.append(
            {
                "n": i,
                "x_n": x_n,
                "x_n2": cuadrado_texto,
                "centro": centro_texto,
                "u_n": u_n,
            }
        )

        # La nueva semilla para la siguiente vuelta es el centro extraido.
        x_n = siguiente

    return resultados


def imprimir_tabla(resultados):
    """Muestra los resultados de forma simple en consola."""
    print(f"{'n':>3} {'x_n':>8} {'x_n^2':>12} {'centro':>8} {'u_n':>10}")
    print("-" * 48)
    for fila in resultados:
        print(
            f"{fila['n']:>3} {fila['x_n']:>8} {fila['x_n2']:>12} "
            f"{fila['centro']:>8} {fila['u_n']:>10.6f}"
        )


def pedir_entero(mensaje: str) -> int:
    """Pide un entero por consola hasta que el usuario ingrese uno valido."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada invalida. Debes ingresar un numero entero.")


if __name__ == "__main__":
    print("Metodo de Von Neumann (Cuadrado Medio)")
    print("-" * 40)

    # Entradas para usar el metodo desde consola.
    n_digitos = pedir_entero("Cantidad de digitos de la semilla (n): ")
    semilla_inicial = pedir_entero("Semilla inicial: ")
    cantidad = pedir_entero("Cantidad de numeros a generar: ")

    serie = von_neumann(semilla_inicial, n_digitos, cantidad)
    imprimir_tabla(serie)
