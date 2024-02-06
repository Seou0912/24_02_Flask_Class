# from flask_smorest import abort

# # 오류 상황에서 abort 호출
# abort(404, message="Resource not found")

# ---------------------------------------------------------------------------
# (1) abort를 사용한 오류 처리
from flask import Flask, abort

app = Flask(__name__)


@app.route("/example")
def example():
    # 어떠한 조건에서 오류를 발생시키고 처리
    error_condition = True

    if error_condition:
        abort(500, description="An error occurred while processing the request.")

    # 정상적인 응답
    return "Success!"


if __name__ == "__main__":
    app.run()

# ------------------------------------------------------------------------------
# (2) abort를 사용하지 않은 오류 처리

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/example")
def example():
    # 어떠한 조건에서 오류를 발생시키고 처리
    error_condition = True

    if error_condition:
        error_response = jsonify(
            {"error": "An error occurred while processing the request."}
        )
        error_response.status_code = 500
        return error_response

    # 정상적인 응답
    return "Success!"
