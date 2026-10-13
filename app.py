from flask import Flask, jsonify, request

from duckfine import DuckFine

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/fine")
def fine():
    try:
        days = int(request.args.get("days"))
    except (TypeError, ValueError):
        return jsonify(error="days must be a non-negative integer"), 400

    if days < 0:
        return jsonify(error="days must be a non-negative integer"), 400

    deluxe = request.args.get("deluxe") == "1"
    fee = DuckFine("api").charge(days, deluxe=deluxe)
    return jsonify(fee=fee)


if __name__ == "__main__":
    app.run()