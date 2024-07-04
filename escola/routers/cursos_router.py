import sqlite3

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from shared.database import get_db



router = APIRouter(prefix='/cursos')

class CursoResponse(BaseModel):
    id: int
    titulo: str
    valor: float
    carga_horaria: int


class CursoRequest(BaseModel):
    titulo: str
    valor: float
    carga_horaria: int

@router.get('/listar_cursos')
def listar_cursos(conn: sqlite3.Connection = Depends(get_db)):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cursos')
    rows = cursor.fetchall()
    cursos = [{"id": row[0], "titulo": row[1], "valor": row[2], 'carga_horaria': row[3]} for row in rows]
    return {"cursos": cursos}

@router.post('/add_curso', response_model=CursoResponse)
def inserir_curso(curso: CursoRequest, conn: sqlite3.Connection = Depends(get_db)):
    cursor = conn.cursor()
    try:
        dados = (curso.titulo, curso.valor, curso.carga_horaria)
        cursor.execute('insert into cursos (titulo, valor, carga_horaria) values (?,?,?)', dados)
        curso_id = cursor.lastrowid
        conn.commit()
        return {'id': curso_id, **curso.dict()}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        cursor.close()

@router.delete('/excluir_curso')
def excluir_curso(titulo, conn: sqlite3.Connection = Depends(get_db)):
    cursor = conn.cursor()
    try:
        dados = (titulo,)
        cursor.execute('delete from cursos where titulo = (?)', dados)
        conn.commit()
        return {"Curso excluído": titulo}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        cursor.close()

