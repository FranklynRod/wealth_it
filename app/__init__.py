from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)

    #DB Configuration
    app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "SQLALCHEMY_DATABASE_URI")
   

    #Import Models Alembic Setup
    from app.models.account import Asset
    from app.models.debt import Debt

    db.init_app(app)
    migrate.init_app(app,db)

    #Register Blueprints
    from routes.debt_routes import debt_bp
    app.register_blueprint(debt_bp)
    from routes.asset_routes import asset_bp
    app.register_blueprint(asset_bp)

    CORS(app)
    return app

