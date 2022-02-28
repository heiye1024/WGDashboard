from flask import  g
from flask_httpauth import HTTPTokenAuth, HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


auths = HTTPTokenAuth(scheme='Token')
baseauth = HTTPBasicAuth()

@baseauth.verify_password
def verify_password(username, password):
    user = filter(lambda user: user['username'] == username, users)
    if user and check_password_hash(user[0]['password'], password):
        g.user = username
        return True
    return False


tokens = {"secret-token-1": "admin"}
# 回调函数，验证 token 是否合法
@auths.verify_token
def verify_token(token):
    if token in tokens:
        g.token = tokens[token]
        return True
    return False


