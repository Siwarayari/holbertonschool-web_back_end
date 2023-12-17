#!/usr/bin/env python3
"""app Module"""
from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'])
def hello_world():
    """function return jsonfy message"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'])
def Register():
    """If the user does not exist, the end-point
    should register it and respond"""
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email,
                        "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=['POST'])
def Login():
    """If the login information is incorrect,
    use flask.abort to respond with a 401 HTTP status"""
    email = request.form.get('email')
    password = request.form.get('password')
    if not email:
        return None
    if not password:
        return None
    valid_login = AUTH.valid_login(email, password)
    if valid_login:
        newses = AUTH.create_session(email)
        response = make_response()
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", newses)
        return response
    else:
        abort(401)


@app.route("/sessions", methods=['DELETE'])
def Logout():
    """request is expected to contain the
    session ID as a cookie with key session_id"""
    requestcookies = request.cookies.get("session_id")
    findeduser = AUTH.get_user_from_session_id(requestcookies)
    if not findeduser:
        abort(403)
    else:
        AUTH.destroy_session(findeduser)
        return redirect("/")


@app.route("/profile", methods=['GET'])
def profile():
    """request is expected to contain a session_id
    cookie. Use it to find the user. If the user exist, respond
    with a 200 HTTP status and the following JSON payload"""
    requestcookies = request.cookies.get("session_id")
    findeduser = AUTH.get_user_from_session_id(requestcookies)
    email = request.form.get('email')
    if not findeduser:
        abort(403)
    else:
        return jsonify({"email": findeduser.email})


@app.route("/reset_password", methods=['POST'])
def get_reset_password_token():
    """If the email is not registered, respond with a
    403 status code. Otherwise, generate a token and
    respond with a 200 HTTP status and the
    following JSON payload:"""
    try:
        email = request.form.get('email')
        reset = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset}), 200
    except Exception:
        abort(403)


@app.route("/reset_password", methods=['PUT'])
def update_password():
    """Update the password. If the token is invalid,
    catch the exception and respond with a 403 HTTP code
    request is expected to contain form data with fields
    "email", "reset_token" and "new_password"""
    try:
        email = request.form.get('email')
        reset_token = request.form.get('reset_token')
        new_password = request.form.get('new_password')
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email,
                        "message": "Password updated"}), 200
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
