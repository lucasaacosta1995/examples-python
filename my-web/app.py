from flask import Flask
from routes.user_routes import user_routes

app = Flask(__name__)

# Registramos las rutas del usuario
app.register_blueprint(user_routes, url_prefix='/users')

if __name__ == '__main__':
    app.run(debug=True)
