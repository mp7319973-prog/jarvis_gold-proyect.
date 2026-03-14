from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json.get("message", "").lower()
    hora_actual = datetime.now().strftime("%H:%M")
    
    # Inteligencia básica inicial
    if "hola" in user_message:
        bot_response = f"Hola Eduardo. Sistemas en línea. Hora en el servidor: {hora_actual}."
    elif "estado" in user_message:
        bot_response = "Todos los núcleos están operativos en Panamá. Conexión estable."
    else:
        bot_response = f"He recibido tu comando: '{user_message}'. Estoy listo para aprender más."
        
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
