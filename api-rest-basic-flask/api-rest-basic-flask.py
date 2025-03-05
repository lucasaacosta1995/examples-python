from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/saludo', methods=['GET'])
def saludo():
    return jsonify({"mensaje": "Hola desde Flask!"})

if __name__ == '__main__':
    app.run(debug=True)
