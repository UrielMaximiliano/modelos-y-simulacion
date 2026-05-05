def generar_fibonacci(x0, x1, m, n):
    """
    Genera números pseudoaleatorios usando el método de Fibonacci.
    X_n = (X_{n-1} + X_{n-2}) mod m
    r_n = X_n / m
    """
    numeros = []
    valores_x = [x0, x1]
    
    for i in range(n):
        nuevo_x = (valores_x[-1] + valores_x[-2]) % m
        r_n = nuevo_x / m
        numeros.append({
            'iteracion': i + 1,
            'x_n': nuevo_x,
            'r_n': round(r_n, 4),
            'r_n_raw': r_n
        })
        valores_x.append(nuevo_x)
        
    return numeros
