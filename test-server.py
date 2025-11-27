# test-server.py

from flask import Flask, jsonify, request, abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory parameter store
PARAMETERS = {
    "max_connections": {
        "key": "max_connections",
        "value": "10",
        "description": "Maximum number of allowed connections",
        "type": "integer",
    },
    "timeout": {
        "key": "timeout",
        "value": "30",
        "description": "Timeout in seconds",
        "type": "integer",
    },
}


@app.get("/parameters")
def get_parameters():
    """
    Return all parameters as a list of objects:
    [{key, value, description}, ...]
    """
    # we ensure that the value is masked as a string
    new_params = {}
    for k, v in PARAMETERS.items():
        new_params[k] = v.copy()
        new_params[k]["value"] = "*" * len(str(v["value"]))
    return jsonify(list(new_params.values())), 200


@app.post("/parameters")
def update_parameter():
    """
    Update a parameter's value.
    Expected JSON body: { "key": "...", "value": "..." }
    """
    data = request.get_json(silent=True) or {}

    key = data.get("key")
    value = data.get("value")

    if not key or value is None:
        return jsonify({"error": "Both 'key' and 'value' are required"}), 400

    if key not in PARAMETERS:
        return jsonify({"error": "Parameter not found"}), 404

    PARAMETERS[key]["value"] = str(value)
    return jsonify({"message": "Parameter updated successfully"}), 200

@app.get("/orders")
def get_orders():
    """
    Return a list of mock orders.
    """
    orders = [
        {
            "id": "order_1",
            "side": "buy",
            "size": 100,
            "price": 50.5,
            "timestamp": "2024-01-01T12:00:00Z",
            "symbol": "AAPL",
            "status": "open"
        },
        {
            "id": "order_2",
            "side": "sell",
            "size": 200,
            "price": 75.0,
            "timestamp": "2024-01-02T15:30:00Z",
            "symbol": "GOOGL",
            "status": "closed"
        }
    ]
    return jsonify(orders), 200

if __name__ == "__main__":
    # pip install flask
    app.run(host="0.0.0.0", port=8000, debug=False)
