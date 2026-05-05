from flask import Flask, render_template, request, jsonify
from generadores.fibonacci import generar_fibonacci
from generadores.congruencial import generar_congruencial_lineal

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('fibonacci.html')

@app.route('/api/generar/fibonacci', methods=['POST'])
def api_generar_fibonacci():
    data = request.json
    x0 = int(data.get('x0', 1))
    x1 = int(data.get('x1', 1))
    m = int(data.get('m', 100))
    n = int(data.get('n', 1000))
    
    resultados = generar_fibonacci(x0, x1, m, n)
    return jsonify(resultados)

@app.route('/api/generar/congruencial', methods=['POST'])
def api_generar_congruencial():
    data = request.json
    x0 = int(data.get('x0', 1))
    a = int(data.get('a', 5))
    c = int(data.get('c', 3))
    m = int(data.get('m', 100))
    n = int(data.get('n', 1000))
    
    resultados = generar_congruencial_lineal(x0, a, c, m, n)
    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=True)
