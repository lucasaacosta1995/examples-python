from flask import Flask, jsonify
from flask_cors import CORS
from routes.usuario import usuario_bp

app = Flask(__name__)
CORS(app)  # Habilita CORS

# Registrar los Blueprints
app.register_blueprint(usuario_bp, url_prefix='/api')

# Manejo global de errores
@app.errorhandler(Exception)
def manejar_errores(e):
    return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
