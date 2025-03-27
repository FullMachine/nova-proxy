from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Nova Proxy is live!"

# ✅ NBA Proxy (BallDontLie)
@app.route("/proxy/nba/player_stats", methods=["GET"])
def proxy_nba_stats():
    player = request.args.get("player")
    if not player:
        return jsonify({"error": "Missing 'player' query parameter"}), 400

    try:
        # Step 1 – Get Player ID
        player_res = requests.get(f"https://www.balldontlie.io/api/v1/players?search={player}")
        player_res.raise_for_status()
        player_data = player_res.json()

        if not player_data["data"]:
            return jsonify({"error": "Player not found"}), 404

        player_id = player_data["data"][0]["id"]

        # Step 2 – Get Season Averages
        stats_res = requests.get(f"https://www.balldontlie.io/api/v1/season_averages?player_ids[]={player_id}")
        stats_res.raise_for_status()
        stats_data = stats_res.json()

        return jsonify(stats_data)
    except requests.exceptions.HTTPError as http_err:
        return jsonify({"error": "HTTP error", "details": str(http_err)}), 500
    except Exception as err:
        return jsonify({"error": "Failed to fetch NBA stats", "details": str(err)}), 500

# You can add more proxies here for soccer or other sports too

if __name__ == "__main__":
    app.run(debug=True)