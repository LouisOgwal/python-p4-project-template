from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api
from .database import db, init_db
from .models import bcrypt
from .routes import register_routes 

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")


    init_db(app)
    bcrypt.init_app(app)
    Migrate(app, db)

    CORS(app, supports_credentials=True)

    api = Api(app)

    register_routes(api)

    @app.route("/", methods=["GET"])
    def home():
        return jsonify({"message": "Welcome to the Apple Store API!"}), 200

    return app

app = create_app()
