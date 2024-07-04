
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

titulo = 'tituloteste'
valor = 50.50
carga_horaria = 190

def test_listar_cursos():
    response = client.get('/cursos/listar_cursos')
    assert response.status_code == 200

    # Verifica se a resposta contém a estrutura esperada
    cursos = response.json().get("cursos")
    assert isinstance(cursos, list)
    if cursos:
        # Verifica a estrutura do primeiro curso se houver cursos na resposta
        assert "id" in cursos[0]
        assert "titulo" in cursos[0]
        assert "valor" in cursos[0]
        assert "carga_horaria" in cursos[0]


def test_add_curso():
    # Dados do novo curso
    novo_curso = {
        "titulo": titulo,
        "valor": valor,
        "carga_horaria": carga_horaria
    }
    response = client.post('/cursos/add_curso', json=novo_curso)
    assert response.status_code == 200

    # Verifica se a resposta contém o id do novo curso e os dados que foram enviados
    curso_adicionado = response.json()
    assert "id" in curso_adicionado
    assert curso_adicionado["titulo"] == novo_curso["titulo"]
    assert curso_adicionado["valor"] == novo_curso["valor"]
    assert curso_adicionado["carga_horaria"] == novo_curso["carga_horaria"]


def test_deletar_curso():
    response = client.delete(f'cursos/excluir_curso?titulo={titulo}')

    assert response.status_code == 200
    assert response.json() == {"Curso excluído": titulo}


if __name__ == '__main__':
    pytest.main()
