from flask import Flask, request, jsonify

app = Flask(__name__)

datas = [{"items": [{"name": "item1", "price": 10}]}]


@app.route("/api/v1/datas", methods=["GET"])
def get_datas():
    return {"datas": datas}


@app.route("/api/v1/datas", methods=["POST"])
def create_data():
    request_data = request.get_json()
    new_data = {"items": request_data.get("items", [])}
    datas.append(new_data)
    return new_data, 201
