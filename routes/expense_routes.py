from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from controllers.expense_controller import add_expense, get_expenses, delete_expense

def register_expense_routes(app):

    @app.route("/expenses", methods=["POST"])
    @jwt_required()
    def create_expense():
        user_id = get_jwt_identity()
        data = request.get_json()
        response, status = add_expense(user_id, data)
        return jsonify(response), status

    @app.route("/expenses", methods=["GET"])
    @jwt_required()
    def list_expenses():
        user_id = get_jwt_identity()
        response, status = get_expenses(user_id)
        return jsonify(response), status

    @app.route("/expenses/<int:expense_id>", methods=["DELETE"])
    @jwt_required()
    def remove_expense(expense_id):
        user_id = get_jwt_identity()
        response, status = delete_expense(user_id, expense_id)
        return jsonify(response), status
