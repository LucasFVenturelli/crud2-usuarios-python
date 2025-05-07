from app.main import usuarios, app

def test_criar_usuario():
    usuarios.clear()  
    client = app.test_client()
    resposta = client.post('/usuarios', json={
        'nome': 'andre',
        'email': 'andre123@email.com',
        'senha': '123456',
        'cpf': '12345678900'
    })
    assert resposta.status_code == 201

def test_listar_usuarios():
    usuarios.clear()
    client = app.test_client()
    client.post('/usuarios', json={
        'nome': 'genesio',
        'email': 'genesio@email.com',
        'senha': 'senha',
        'cpf': '98765432100'
    })
    resposta = client.get('/usuarios')
    assert resposta.status_code == 200
    assert isinstance(resposta.get_json(), list)

def test_buscar_usuario_existente():
    usuarios.clear()
    client = app.test_client()
    client.post('/usuarios', json={
        'nome': 'Carlos',
        'email': 'carlos@email.com',
        'senha': 'abc123',
        'cpf': '00011122233'
    })
    resposta = client.get('/usuarios/00011122233')
    assert resposta.status_code == 200
    assert resposta.get_json()['nome'] == 'Carlos'

def test_buscar_usuario_inexistente():
    usuarios.clear()
    client = app.test_client()
    resposta = client.get('/usuarios/99999999999')
    assert resposta.status_code == 404

def test_deletar_usuario_existente():
    usuarios.clear()
    client = app.test_client()
    client.post('/usuarios', json={
        'nome': 'Ana',
        'email': 'ana@email.com',
        'senha': 'senha123',
        'cpf': '44455566677'
    })
    resposta = client.delete('/usuarios/44455566677')
    assert resposta.status_code == 200

def test_deletar_usuario_inexistente():
    usuarios.clear()
    client = app.test_client()
    resposta = client.delete('/usuarios/00000000000')
    assert resposta.status_code == 404