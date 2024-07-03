import sqlite3

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel


router = APIRouter(prefix='/professores')

def get_db():
    conn = sqlite3.connect("shared/escola.db")
    try:
        yield conn
    finally:
        conn.close()

class Professor(BaseModel):
    nome: str

@router.get('/listar_professores')
def listar_professores(conn: sqlite3.Connection = Depends(get_db)):
    cursor = conn.cursor()
    cursor.execute('select * from professores')
    rows = cursor.fetchall()
    prof = [{'id': r[0], 'nome': r[1]} for r in rows]
    return {'professores': prof}

@router.post('/add_professor', response_model=Professor)
def add_professor(prof: Professor, conn: sqlite3.Connection = Depends(get_db)):
    cursor = conn.cursor()
    try:
        dados = (prof.nome,)
        cursor.execute('insert into professores (nome) values (?)', dados)
        prof_id = cursor.lastrowid
        conn.commit()
        return {"id": prof_id, **prof.dict()}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        cursor.close()

@router.delete('/excluir_professor')
def excluir_professor(prof: Professor, conn: sqlite3.Connection = Depends(get_db)):
    cursor = conn.cursor()
    try:
        dados = (prof.nome,)
        cursor.execute('delete from professores where nome = (?)', dados)
        conn.commit()
        return {"Professor excluído": prof.nome}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        cursor.close()
