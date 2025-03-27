from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return 'Nova Proxy is working!'

@app.route('/nba/player_search', methods=['GET'])
def proxy_bdl_player_search():
    player = request.args.get('player')
    if not player:
        return jsonify({"error": "Missing player name"}), 400

    try:
        url = f"https://www.balldontlie.io/api/v1/players?search={player}"
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad status codes
        return jsonify(response.json())
    except requests.exceptions.HTTPError as e:
        return jsonify({"error": "HTTP error", "details": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()