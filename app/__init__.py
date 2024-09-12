from flask import Flask

def create_app():
    # Creating flask app instance
    app = Flask(__name__, template_folder='templates')

    # importing blueprints
    from app.blueprints.root import index

    # Registering blueprints
    app.register_blueprint(index.bp)

    return app