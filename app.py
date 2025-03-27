from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Nova Proxy is running!"

@app.route('/proxy/balldontlie', methods=['GET'])
def proxy_balldontlie():
    player = request.args.get('player')
    if not player:
        return jsonify({"error": "Missing player name"}), 400

    try:
        search_url = f"https://www.balldontlie.io/api/v1/players?search={player}"
        res = requests.get(search_url)
        res.raise_for_status()
        data = res.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": "Failed to fetch player", "details": str(e)}), 500

if __name__ == "__main__":
    app.run()