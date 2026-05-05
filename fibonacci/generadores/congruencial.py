def generar_congruencial_lineal(x0, a, c, m, n):
    """
    Genera números pseudoaleatorios usando el método Congruencial Lineal clásico.
    X_n = (a * X_{n-1} + c) mod m
    r_n = X_n / m
    """
    numeros = []
    x_n = x0
    
    for i in range(n):
        x_n = (a * x_n + c) % m
        r_n = x_n / m
        numeros.append({
            'iteracion': i + 1,
            'x_n': x_n,
            'r_n': round(r_n, 4),
            'r_n_raw': r_n
        })
        
    return numeros
