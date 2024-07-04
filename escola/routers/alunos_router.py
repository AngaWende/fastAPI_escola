import sqlite3, os
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from shared.database import get_db


router = APIRouter(prefix='/alunos')


class AlunoResponse(BaseModel):
    nome: str
    cpf: str
    email: str

@router.get('/listar_alunos')
def listar_alunos(conn: sqlite3.Connection = Depends(get_db)):
    cursor = conn.cursor()
    cursor.execute('select * from alunos')
    rows = cursor.fetchall()
    alunos = [{'id': row[0], 'nome': row[1], 'cpf': row[2], 'e_mail': row[3]} for row in rows]
    return {'alunos': alunos}

@router.post('/add_aluno')
def add_aluno(aluno: AlunoResponse, conn: sqlite3.Connection = Depends(get_db)):
    cursor = conn.cursor()
    try:
        dados = (aluno.nome, aluno.cpf, aluno.email)
        cursor.execute('insert into alunos (nome, cpf, email) values (?,?,?)', dados)
        aluno_id = cursor.lastrowid
        conn.commit()
        return {"id": aluno_id, **aluno.dict()}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        cursor.close()

@router.delete('/excluir_aluno')
def excluir_aluno(nome, conn: sqlite3.Connection = Depends(get_db)):
    cursor = conn.cursor()
    try:
        dados = (nome,)
        cursor.execute('delete from alunos where nome = (?)', dados)
        conn.commit()
        return {"Aluno excluído": nome}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        cursor.close()