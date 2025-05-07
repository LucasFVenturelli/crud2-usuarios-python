from flask import Flask, request, jsonify

app = Flask(__name__)
usuarios = []

@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    usuarios.append(request.get_json())
    return {'mensagem' : 'ok' }, 201

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios), 200

@app.route('/usuarios/<cpf>', methods=['GET'])
def buscar_usuario(cpf):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return jsonify(usuario), 200
    return jsonify({'erro': 'Não encontrado'}), 404

@app.route('/usuarios/<cpf>', methods=['DELETE'])
def deletar_usuario(cpf):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            usuarios.remove(usuario)
            return jsonify({'mensagem': 'Usuário removido'}), 200
    return jsonify({'erro': 'Não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)