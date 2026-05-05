"""
Metodo Congruencial Aditivo
1) Xi = (X_{i-1} + X_{i-k}) mod m
2) Ri = Xi / (m - 1)  o  Ri = Xi / m
"""

import sys

def generar_congruencial_aditivo(semillas, m, n):
    """
    semillas: Lista de enteros iniciales [X_1, X_2, ..., X_k]
    m: Modulo
    n: Cantidad de numeros a generar
    """
    if not isinstance(m, int) or m <= 0:
        raise ValueError("El modulo 'm' debe ser un entero positivo.")
    if not isinstance(n, int) or n <= 0:
        raise ValueError("La cantidad 'n' debe ser un entero positivo.")
    if len(semillas) < 2:
        raise ValueError("Se necesitan al menos 2 semillas iniciales.")
        
    k = len(semillas)
    secuencia = list(semillas)
    resultados = []
    
    for i in range(1, n + 1):
        # El nuevo numero es la suma del anterior X_{i-1} y el X_{i-k} (el primero de la ventana)
        x_nuevo = (secuencia[-1] + secuencia[-k]) % m
        r_i = x_nuevo / m  # O (m-1) dependiendo de la convención de la cátedra
        
        resultados.append({
            "i": i + k,
            "x_i_1": secuencia[-1],
            "x_i_k": secuencia[-k],
            "x_nuevo": x_nuevo,
            "r_i": round(r_i, 5)
        })
        
        # Agregamos a la secuencia
        secuencia.append(x_nuevo)
        
    return resultados


def imprimir_tabla(resultados):
    print(f"{'i':>4} {'X_{i-1}':>8} {'X_{i-k}':>8} {'X_i':>8} {'R_i':>8}")
    print("-" * 42)
    for fila in resultados:
        print(
            f"{fila['i']:>4} "
            f"{fila['x_i_1']:>8} "
            f"{fila['x_i_k']:>8} "
            f"{fila['x_nuevo']:>8} "
            f"{fila['r_i']:>8.5f}"
        )


def mostrar_uso():
    print("Uso:")
    print("  python congruencial_aditivo.py <semilla_1> <semilla_2> ... <semilla_k> <m> <n>")
    print("  python congruencial_aditivo.py  (modo interactivo)")
    print("Ejemplo (5 semillas, m=100, n=10):")
    print("  python congruencial_aditivo.py 65 89 98 3 69 100 10")


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada invalida. Escribi un numero entero.")


def main():
    try:
        if len(sys.argv) >= 4:
            # Los ultimos dos argumentos son m y n. El resto son semillas
            args_enteros = list(map(int, sys.argv[1:]))
            m = args_enteros[-2]
            n = args_enteros[-1]
            semillas = args_enteros[:-2]
        elif len(sys.argv) == 1:
            print("Modo interactivo - Congruencial Aditivo")
            k = leer_entero("Cantidad de semillas iniciales (k): ")
            semillas = []
            for i in range(k):
                semilla = leer_entero(f"Semilla {i+1}: ")
                semillas.append(semilla)
            m = leer_entero("Modulo (m): ")
            n = leer_entero("Cantidad de numeros a generar (n): ")
        else:
            mostrar_uso()
            return 1

        tabla = generar_congruencial_aditivo(semillas, m, n)
        imprimir_tabla(tabla)
        return 0
    except ValueError as error:
        print(f"Error: {error}")
        mostrar_uso()
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
