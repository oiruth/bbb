import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as origens

@app.route('/generate-key', methods=['POST'])
def generate_key():
    try:
        # Obtém os dados JSON da requisição
        data = request.get_json()
        user_id = data.get('user_id')
        user_name = data.get('user_name')
        days = data.get('days')

        # Verifica se os dados necessários foram enviados
        if not user_id or not user_name or not days:
            return jsonify({'status': 'error', 'message': 'user_id, user_name e days são necessários'}), 400

        # Lógica para gerar a chave (exemplo simples)
        expiration_date = (datetime.now() + timedelta(days=int(days))).strftime('%Y-%m-%d')
        key = f'{user_id}-{user_name}-{expiration_date}'

        return jsonify({'key': key, 'expiration_date': expiration_date, 'status': 'success'}), 200

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
