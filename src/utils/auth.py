from email import message
from flask import  jsonify,  session, render_template, redirect, request
from flask_httpauth import HTTPTokenAuth, HTTPBasicAuth, MultiAuth
from werkzeug.security import generate_password_hash, check_password_hash
from utils.tools  import get_dashboard_conf

token_auth = HTTPTokenAuth(scheme='Szyh')
basic_auth = HTTPBasicAuth()

config = get_dashboard_conf()

multi_auth = MultiAuth(basic_auth, token_auth)


@basic_auth.verify_password
def verify_password(username, password):
    for user in username:
        print(username)
        # if user == config["Account"]["username"]:
        if username == "admin":
            # password = hashlib.sha256(data['password'].encode())
            return True
    return False


tokens = {
    "admin": "admin",
    "secret-token-2": "Susan"
}
# 回调函数，验证 token 是否合法
@token_auth.verify_token
def verify_token(token):
    if token in tokens:
        print(token)
        #g.token = tokens[token]
        return True
    return False


'''
def login_required(func):
    def inner(*args, **kwargs):
        # 从session获取用户信息，如果有，则用户已登录，否则没有登录

        msg = ""
        if "message" in session:
            return render_template('index.html',  message=msg)

        return render_template('signin.html', message=message)
        #return func(*args, **kwargs)
    return inner

'''