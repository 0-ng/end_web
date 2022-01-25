import time
from flask import Flask, request, session, jsonify, make_response, send_from_directory, abort
app = Flask(__name__)


# 首次Get请求下发CSRF-TOKEN
@app.route('/login', methods=["GET", "POST"])
def first_request():
    """首次Get请求下发CSRF-TOKEN以及相关cookies数据

    :return: json格式字符串
    """
    # response = response()
    result = {"code": 200, 'data': '0ng'}
    resp = make_response(jsonify(result))
    # 指定cookie放在/位置
    resp.headers['Access-Control-Expose-Headers'] = 'csrf_token,Set-Cookie'
    resp.headers['supportsCredentials'] = True
    resp.headers['Access-Control-Allow-Origin'] = '*'
    # resp.headers['Access-Control-Allow-Credentials'] = True
    return resp


@app.route('/')
def hello():
    return 'Hello World! I have been seen {} times.\n'.format(6)


if __name__ == '__main__':
    app.run(debug=True)