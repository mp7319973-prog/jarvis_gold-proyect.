from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    mensaje = data.get("message", "").lower()
    
    if "hola" in mensaje:
        respuesta = "Hola Eduardo. Sistemas en línea en Panamá."
    elif "estado" in mensaje:
        respuesta = "Núcleos estables. Energía al 100%."
    else:
        respuesta = f"Comando '{mensaje}' recibido y procesado."
        
    return jsonify({"response": respuesta})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
