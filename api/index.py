import os
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Health endpoint para Vercel
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

# Exemplo de endpoint (adicione outros conforme necessário)
@app.route('/motos', methods=['GET'])
def listar_motos():
    return jsonify({'motos': []})

# Exporta o app para Vercel
handler = app
