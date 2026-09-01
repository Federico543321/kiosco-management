from flask import Flask
from backend.app.routes.usuario_routes import usuario_routes

app = Flask(__name__)

app.register_blueprint(usuario_routes)


@app.route("/")
def inicio():
    return "Kiosco Management - Backend funcionando"


if __name__ == "__main__":
    app.run(debug=True)