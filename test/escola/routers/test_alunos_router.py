
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

nome = 'nometeste'
cpf = 'cpfteste'
email = 'emailteste'

def test_listar_alunos():
    response = client.get('/alunos/listar_alunos')
    assert response.status_code == 200

    # Verifica se a resposta contém a estrutura esperada
    alunos = response.json().get("alunos")
    assert isinstance(alunos, list)
    if alunos:
        # Verifica a estrutura do primeiro aluno se houver alunos na resposta
        assert "id" in alunos[0]
        assert "nome" in alunos[0]
        assert "cpf" in alunos[0]
        assert "e_mail" in alunos[0]


def test_add_aluno():
    # Dados do novo aluno
    novo_aluno = {
        "nome": nome,
        "cpf": cpf,
        "email": email
    }
    response = client.post('/alunos/add_aluno', json=novo_aluno)
    assert response.status_code == 200

    # Verifica se a resposta contém o id do novo aluno e os dados que foram enviados
    aluno_adicionado = response.json()
    assert "id" in aluno_adicionado
    assert aluno_adicionado["nome"] == novo_aluno["nome"]
    assert aluno_adicionado["cpf"] == novo_aluno["cpf"]
    assert aluno_adicionado["email"] == novo_aluno["email"]


def test_deletar_aluno():
    response = client.delete(f'alunos/excluir_aluno?nome={nome}')

    assert response.status_code == 200
    assert response.json() == {"Aluno excluído": nome}


if __name__ == '__main__':
    pytest.main()
