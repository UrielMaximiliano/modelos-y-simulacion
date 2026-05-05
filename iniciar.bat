@echo off
echo === Modelos y Simulacion - Setup ===
python -m venv venv
call venv\Scripts\activate.bat
pip install -r requirements.txt
echo.
echo Listo! Abri http://127.0.0.1:5000
echo.
python app.py
