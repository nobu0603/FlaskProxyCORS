from flask import Flask, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/proxy", methods=["GET"])
def proxy():
    api_url = "https://dbd.tricky.lol/api/randomperks?role=survivor"  # ここにAPIエンドポイントを記載する
    response = requests.get(api_url)
    return jsonify(response.json())


if __name__ == "__main__":
    app.run(port=5000)
