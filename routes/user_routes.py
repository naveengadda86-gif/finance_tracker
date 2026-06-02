from flask import request, jsonify
from flask_jwt_extended import jwt_required
from controllers.user_controller import register_user, login_user

def register_user_routes(app):

    @app.route("/register", methods=["POST"])
    def register():
        data = request.get_json()
        response, status = register_user(data)
        return jsonify(response), status

    @app.route("/login", methods=["POST"])
    def login():
        data = request.get_json()
        response, status = login_user(data)
        return jsonify(response), status
