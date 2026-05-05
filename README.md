# Modelos y Simulación

Plataforma web para visualizar y comparar 6 métodos de generación de números pseudoaleatorios.

---

## Cómo ejecutar

### 1. Clonar el repositorio

```bash
git clone https://github.com/UrielMaximiliano/modelos-y-simulacion.git
cd modelos-y-simulacion
```

### 2. Crear el entorno virtual (solo la primera vez)

```bash
python -m venv venv
```

### 3. Activar el entorno virtual

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
venv\Scripts\activate.bat
```

**Linux / Mac:**
```bash
source venv/bin/activate
```

### 4. Instalar dependencias (solo la primera vez)

```bash
pip install -r requirements.txt
```

### 5. Levantar el servidor

```bash
python app.py
```

### 6. Abrir en el navegador

Ir a **http://127.0.0.1:5000**

Desde ahí se navegan los 6 métodos con el menú lateral.

---

## Métodos disponibles en la web

| #  | Método                     | Ruta en la web                |
|----|----------------------------|-------------------------------|
| 1  | Fibonacci (Aditivo)        | `/`                           |
| 2  | Von Neumann (Cuadrado Medio) | `/von_neuman`              |
| 3  | Producto Medio             | `/producto_medio`             |
| 4  | Congruencial Multiplicativo| `/congruencial_multiplicativo`|
| 5  | Congruencial Mixto (Lineal)| `/congruencial_mixto`         |
| 6  | Congruencial Aditivo       | `/congruencial_aditivo`       |

---

## Ejecución por consola (opcional)

Los scripts individuales también se pueden correr directo por terminal:

### Congruencial Multiplicativo

```bash
python congruencial_multiplicativo/congruencial_multiplicativo.py 7 5 32 10
```

Parámetros: `semilla`, `a` (multiplicador), `m` (módulo), `n` (cantidad)

### Producto Medio

```bash
python producto_medio/producto_medio.py 5015 5734 4 10
```

Parámetros: `x0`, `x1` (semillas), `d` (dígitos), `n` (cantidad)

### Von Neumann

```bash
python von_neuman/von_neuman.py
```

Modo interactivo. Pide: `n_digitos`, `semilla`, `cantidad`.

### Congruencial Mixto

```bash
python congruencial_mixto/mixto.py
```

Modo interactivo. Pide: `x0`, `a`, `c`, `m`, `cantidad`.

### Congruencial Aditivo

```bash
python congruencial_aditivo/congruencial_aditivo.py 65 89 98 3 69 100 10
```

Parámetros: `semillas...` (separadas por espacio), `m` (módulo), `n` (cantidad)

---

## Estructura del proyecto

```
modelos-y-simulacion/
├── app.py                          # Servidor web Flask (raíz)
├── requirements.txt                # Dependencias Python
├── static/                         # CSS y JS
├── templates/                      # Plantillas HTML
├── fibonacci/generadores/          # Lógica Fibonacci + Congruencial comparativa
├── von_neuman/                     # Lógica Von Neumann
├── producto_medio/                 # Lógica Producto Medio
├── congruencial_multiplicativo/    # Lógica Congruencial Multiplicativo
├── congruencial_mixto/             # Lógica Congruencial Mixto
├── congruencial_aditivo/           # Lógica Congruencial Aditivo
└── venv/                           # Entorno virtual (no subir)
```

## Tecnologías

- **Backend:** Python 3 + Flask
- **Frontend:** HTML5, Vanilla CSS, Chart.js
- **Tipografía:** Syne + DM Sans (Google Fonts)
