from flask import Flask
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"},
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(
        users.get(username), password):
        return username
    else:
        return False

@app.route('/basic-protected')
@auth.login_required
def index():
    if auth.current_user() is False:
        return "401 Unauthorized", 401





if __name__ == "__main__":
    app.run()
