
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

nome = 'nometeste'

def test_listar_professores():
    response = client.get('/professores/listar_professores')
    assert response.status_code == 200

    # Verifica se a resposta contém a estrutura esperada
    professores = response.json().get("professores")
    assert isinstance(professores, list)
    if professores:
        # Verifica a estrutura do primeiro professor se houver professores na resposta
        assert "id" in professores[0]
        assert "nome" in professores[0]
       


def test_add_professor():
    # Dados do novo professor
    novo_professor = {
        "nome": nome,
    }
    response = client.post('/professores/add_professor', json=novo_professor)
    assert response.status_code == 200

    # Verifica se a resposta contém o id do novo professor e os dados que foram enviados
    professor_adicionado = response.json()
    assert "nome" in professor_adicionado
    assert professor_adicionado["nome"] == novo_professor["nome"]


def test_deletar_professor():
    response = client.delete(f'professores/excluir_professor?nome={nome}')

    assert response.status_code == 200
    assert response.json() == {"Professor excluído": nome}


if __name__ == '__main__':
    pytest.main()
