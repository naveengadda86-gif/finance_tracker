from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from database.connection import create_tables
from routes.user_routes import register_user_routes
from routes.category_routes import register_category_routes
from routes.expense_routes import register_expense_routes

app = Flask(__name__)
CORS(app)

app.config["JWT_SECRET_KEY"] = "mysecretkey123"

jwt = JWTManager(app)

# Create tables on startup
create_tables()

# Register all routes
register_user_routes(app)
register_category_routes(app)
register_expense_routes(app)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
