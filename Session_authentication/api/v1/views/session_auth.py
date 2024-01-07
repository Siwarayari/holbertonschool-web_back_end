#!/usr/bin/env python3
""" Module of Users views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """New view for Session Authentication"""
    email = request.form.get("email")
    password = request.form.get("password")
    if email is None:
        return jsonify({"error": "email missing"}), 400
    if password is None:
        return jsonify({"error": "password missing"}), 400

    useremail = User.search({"email": email})

    if not useremail:
        return jsonify({"error": "no user found for this email"}), 404

    for i in useremail:
        if i.is_valid_password(password):
            from api.v1.app import auth
            newses = auth.create_session(i.id)
            to_json = jsonify(i.to_json())
            to_json.set_cookie(getenv('SESSION_NAME'), newses)
            return to_json
        else:
            return jsonify({"error": "wrong password"}), 401


@app_views.route('/api/v1/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """new route DELETE
    /api/v1/auth_session/logout"""
    from api.v1.app import auth
    destroy_session = auth.destroy_session(request)
    if not destroy_session:
        abort(404)
        return False
    else:
        return jsonify({}), 200
