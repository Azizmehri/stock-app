from flask import Flask, jsonify, send_file
from scraper import get_stock

app = Flask(__name__)

@app.route("/")
def index():
    return send_file("index.html")

@app.route("/get-stock")
def get_stock_route():
    stock = get_stock()
    return jsonify({"stock": stock}) if stock else jsonify({"error": "stock indisponible"}), 500

if __name__ == "__main__":
    app.run(debug=True)