from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Nova Proxy is live!"

@app.route("/proxy/ball_dont_lie/player", methods=["GET"])
def proxy_ball_dont_lie():
    player_name = request.args.get("player")
    if not player_name:
        return jsonify({"error": "Missing player name"}), 400

    try:
        url = f"https://balldontlie.io/api/v1/players?search={player_name}"
        response = requests.get(url)
        data = response.json()
        return jsonify(data), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/proxy/ball_dont_lie/season_avg", methods=["GET"])
def proxy_season_avg():
    player_id = request.args.get("player_id")
    if not player_id:
        return jsonify({"error": "Missing player_id"}), 400

    try:
        url = f"https://www.balldontlie.io/api/v1/season_averages?player_ids[]={player_id}"
        response = requests.get(url)
        data = response.json()
        return jsonify(data), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)