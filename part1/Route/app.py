from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "hello, This is Main Page"


@app.route("/about")
def about():
    return "hello, This is about Page"


@app.route("/user/<username>")
def user_profile(username):

    return f"username : {username}"


# post  요청 날리는 법
# (1) postman
# (2) requests
import requests  # pip3 install requests


@app.route("/test")
def test():
    url = "http://127.0.0.1:5000/submit"
    data = "test data"
    response = requests.post(url=url, data=data)
    return response


@app.route("/submit", methods=["POST", "GET", "PUT", "DELETE"])
def submit():
    print(request.method)
    if request.method == "GET":
        print("GET method")

    if request.method == "POST":
        print("***POST method***", request.data)
    return "seccess"


if __name__ == "__name__":
    app.run()
# http://127.0.0.1:5000
