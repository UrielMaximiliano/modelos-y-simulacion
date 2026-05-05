from flask import Flask, render_template, request, jsonify

# Importar generadores
from fibonacci.generadores.fibonacci import generar_fibonacci
from fibonacci.generadores.congruencial import generar_congruencial_lineal
from von_neuman.von_neuman import von_neumann
from producto_medio.producto_medio import generar_producto_medio
from congruencial_multiplicativo.congruencial_multiplicativo import generar_congruencial_multiplicativo
from congruencial_mixto.mixto import congruencial_mixto
from congruencial_aditivo.congruencial_aditivo import generar_congruencial_aditivo

app = Flask(__name__)

# Rutas de páginas HTML
@app.route('/')
def index():
    return render_template('fibonacci.html', active_page='fibonacci')

@app.route('/von_neuman')
def page_von_neuman():
    return render_template('von_neuman.html', active_page='von_neuman')

@app.route('/producto_medio')
def page_producto_medio():
    return render_template('producto_medio.html', active_page='producto_medio')

@app.route('/congruencial_multiplicativo')
def page_congruencial_multiplicativo():
    return render_template('congruencial_multiplicativo.html', active_page='congruencial_multiplicativo')

@app.route('/congruencial_mixto')
def page_congruencial_mixto():
    return render_template('congruencial_mixto.html', active_page='congruencial_mixto')

@app.route('/congruencial_aditivo')
def page_congruencial_aditivo():
    return render_template('congruencial_aditivo.html', active_page='congruencial_aditivo')


# --- ENDPOINTS API ---

@app.route('/api/generar/fibonacci', methods=['POST'])
def api_generar_fibonacci():
    data = request.json
    x0, x1, m, n = int(data.get('x0', 1)), int(data.get('x1', 1)), int(data.get('m', 100)), int(data.get('n', 1000))
    resultados = generar_fibonacci(x0, x1, m, n)
    return jsonify(resultados)

@app.route('/api/generar/congruencial', methods=['POST'])
def api_generar_congruencial():
    data = request.json
    x0, a, c, m, n = int(data.get('x0', 1)), int(data.get('a', 5)), int(data.get('c', 3)), int(data.get('m', 100)), int(data.get('n', 1000))
    resultados = generar_congruencial_lineal(x0, a, c, m, n)
    return jsonify(resultados)

@app.route('/api/generar/von_neuman', methods=['POST'])
def api_generar_von_neuman():
    data = request.json
    semilla = int(data.get('semilla', 1234))
    n_digitos = int(data.get('n_digitos', 4))
    n_cant = int(data.get('n', 1000))
    
    bruto = von_neumann(semilla, n_digitos, n_cant)
    # Adaptar para el frontend
    adaptado = [{"iteracion": r["n"], "x_n": r["x_n"], "r_n": round(r["u_n"], 4), "r_n_raw": r["u_n"]} for r in bruto]
    return jsonify(adaptado)

@app.route('/api/generar/producto_medio', methods=['POST'])
def api_generar_producto_medio():
    data = request.json
    x0, x1 = int(data.get('x0', 5015)), int(data.get('x1', 5734))
    d, n = int(data.get('d', 4)), int(data.get('n', 1000))
    
    bruto = generar_producto_medio(x0, x1, d, n)
    adaptado = [{"iteracion": r["i"], "x_n": r["yi"], "r_n": r["ri"], "r_n_raw": float(r["ri"])} for r in bruto]
    return jsonify(adaptado)

@app.route('/api/generar/congruencial_multiplicativo', methods=['POST'])
def api_generar_congruencial_multiplicativo():
    data = request.json
    semilla, a, m, n = int(data.get('semilla', 7)), int(data.get('a', 5)), int(data.get('m', 32)), int(data.get('n', 1000))
    
    bruto = generar_congruencial_multiplicativo(semilla, a, m, n)
    adaptado = [{"iteracion": r["i"], "x_n": r["xi"], "r_n": r["ri"], "r_n_raw": float(r["ri"])} for r in bruto]
    return jsonify(adaptado)

@app.route('/api/generar/congruencial_mixto', methods=['POST'])
def api_generar_congruencial_mixto():
    data = request.json
    x0, a, c, m, n = int(data.get('x0', 1)), int(data.get('a', 5)), int(data.get('c', 3)), int(data.get('m', 100)), int(data.get('n', 1000))
    
    bruto = congruencial_mixto(x0, a, c, m, n)
    adaptado = [{"iteracion": r["n"], "x_n": r["x_n"], "r_n": round(r["u_n"], 4), "r_n_raw": r["u_n"]} for r in bruto]
    return jsonify(adaptado)

@app.route('/api/generar/congruencial_aditivo', methods=['POST'])
def api_generar_congruencial_aditivo():
    data = request.json
    # Recibimos una lista de semillas separadas por coma en string, o un string
    semillas_str = data.get('semillas', '65, 89, 98, 3, 69')
    semillas = [int(s.strip()) for s in semillas_str.split(',')]
    m, n = int(data.get('m', 100)), int(data.get('n', 1000))
    
    bruto = generar_congruencial_aditivo(semillas, m, n)
    adaptado = [{"iteracion": r["i"], "x_n": r["x_nuevo"], "r_n": r["r_i"], "r_n_raw": float(r["r_i"])} for r in bruto]
    return jsonify(adaptado)

if __name__ == '__main__':
    app.run(debug=True)
