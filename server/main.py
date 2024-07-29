from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Ruta para obtener usuarios de la base de datos (devuelve un)
@app.route('/api/v1/users', methods=['GET'])
def index():
    return jsonify({
            "users": [
                {"name": "John", "email": "john@example.com", "last_name": "Harvard"},
                {"name": "Peter", "email": "peter@example.com", "last_name": "Griffin"},
                {"name": "Susan", "email": "susan@example.com", "last_name": "Jackson"}
            ]
        }),200

# Ruta para actualizar los datos de un user existente (devuelve los datos enviados desde el front)
@app.route('/api/v1/users', methods=['POST'])
def add_user():
    new_user = request.json
    return jsonify(new_user),200

# Ruta para hacer update a un user existente (retorna la data proporcionada por el front)
@app.route('/api/v1/users', methods=['PATCH'])
def add_user():
    new_user_data = request.json
    return jsonify(new_user_data),200

# Ruta para eliminar a un usuario de la db (solo retorna true simulando que funciona)
@app.route('/api/v1/users', methods=['DELETE'])
def add_user():
    return jsonify({"success": True}),200


if __name__ == '__main__':
    app.run(debug=True)
