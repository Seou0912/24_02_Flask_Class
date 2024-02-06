from flask import Flask, jsonify

app = Flask(__name__)


# Get
# 전체 게시글을 불러오는 API
@app.route("/api/v1/feeds", methods=["Get"])
def show_all_feeds():
    data = {"result": "success", "data": {"feded1": "data1", "feded2": "data2"}}
    return data


# 특정 게시글을 불러오는 API
@app.route("/api/v1/feeds/<int:feed_id>", method=["GET"])
def show_one_feed(feed_id):
    print(feed_id)
    data = {"result": "success", "data": {"feed1": "data1"}}

    return data


# POST
# 게시글 작성하는 API
@app.route("/api/v1/feeds", methods=["POST"])
def create_one_feed():
    name = request.form["name"]
    age = request.form["age"]
    print(name, age)
    return jsonify({"result": "success"})


if __name__ == "__name__":
    app.run(debug=True)
