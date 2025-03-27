from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Proxy is live!"

@app.route('/proxy/balldontlie', methods=['GET'])
def proxy_balldontlie():
    player_name = request.args.get('player')
    if not player_name:
        return jsonify({'error': 'Missing player name'}), 400

    try:
        url = f"https://www.balldontlie.io/api/v1/players?search={player_name}"
        response = requests.get(url)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/proxy/balldontlie/stats', methods=['GET'])
def proxy_bdl_stats():
    player_id = request.args.get('id')
    if not player_id:
        return jsonify({'error': 'Missing player ID'}), 400

    try:
        stats_url = f"https://www.balldontlie.io/api/v1/season_averages?player_ids[]={player_id}"
        response = requests.get(stats_url)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)