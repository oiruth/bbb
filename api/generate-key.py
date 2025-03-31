from flask import Flask, jsonify, request
from flask_cors import CORS  # Importa a biblioteca CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as origens

# Endpoint para gerar a chave
@app.route('/generate-key', methods=['POST'])
def generate_key():
    try:
        # Obtém os dados JSON da requisição
        data = request.get_json()
        user_id = data.get('user_id')
        days = data.get('days')

        # Verifica se os dados necessários foram enviados
        if not user_id or not days:
            return jsonify({'status': 'error', 'message': 'user_id e days são necessários'}), 400

        # Lógica para gerar a chave (exemplo simples)
        key = f'{user_id}-{days}'

        return jsonify({'key': key, 'status': 'success'}), 200

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Executa o servidor Flask
