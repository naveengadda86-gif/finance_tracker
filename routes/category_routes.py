from flask import request, jsonify
from flask_jwt_extended import jwt_required
from controllers.category_controller import add_category, get_all_categories

def register_category_routes(app):

    @app.route("/categories", methods=["POST"])
    @jwt_required()
    def create_category():
        data = request.get_json()
        response, status = add_category(data)
        return jsonify(response), status

    @app.route("/categories", methods=["GET"])
    @jwt_required()
    def list_categories():
        response, status = get_all_categories()
        return jsonify(response), status
