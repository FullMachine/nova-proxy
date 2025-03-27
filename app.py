from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Nova Proxy is live!"

@app.route('/nba/player_stats', methods=['GET'])
def proxy_nba_stats():
    player_name = request.args.get('player')
    if not player_name:
        return jsonify({'error': 'Missing player name'}), 400

    try:
        # Step 1: Search for player ID
        search_url = f"https://www.balldontlie.io/api/v1/players?search={player_name}"
        search_response = requests.get(search_url)
        player_data = search_response.json()

        if not player_data['data']:
            return jsonify({'error': 'Player not found'}), 404

        player_id = player_data['data'][0]['id']

        # Step 2: Get season averages
        stats_url = f"https://www.balldontlie.io/api/v1/season_averages?player_ids[]={player_id}"
        stats_response = requests.get(stats_url)
        stats_data = stats_response.json()

        return jsonify(stats_data)

    except Exception as e:
        return jsonify({'error': 'Failed to fetch NBA stats', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run()