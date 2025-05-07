from flask import Flask, request, jsonify


app = Flask(__name__)
usuarios = []

@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = request.get_json()
    if not all(k in dados for k in ['nome', 'email', 'senha', 'cpf']):
        return {'erro': 'Campos obrigatórios ausentes'}, 400
    if any(u['cpf'] == dados['cpf'] for u in usuarios):
        return {'erro': 'CPF já cadastrado'}, 400
    usuarios.append(dados)
    return {'mensagem': 'Usuário criado'}, 201

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios)

@app.route('/usuarios/<cpf>', methods=['GET'])
def buscar_usuario(cpf):
    u = next((u for u in usuarios if u['cpf'] == cpf), None)
    return (jsonify(u), 200) if u else ({'erro': 'Não encontrado'}, 404)

@app.route('/usuarios/<cpf>', methods=['DELETE'])
def deletar_usuario(cpf):
    global usuarios
    if any(u['cpf'] == cpf for u in usuarios):
        usuarios = [u for u in usuarios if u['cpf'] != cpf]
        return {'mensagem': 'Usuário removido'}, 200
    return {'erro': 'Não encontrado'}, 404

if __name__ == '__main__':
    app.run(debug=True)
