import sqlite3

from fastapi import APIRouter, Depends, HTTPException

from escola.routers.cursos_router import CursoResponse
from escola.routers.professores_router import Professor
from shared.database import get_db

router = APIRouter(prefix='/vinculo_professor')


@router.post('/listar_aulas')
def listar_aulas(professor_ou_curso: str, conn: sqlite3.Connection = Depends(get_db)):
    cursor = conn.cursor()
    if professor_ou_curso == 'professor':
        cursor.execute('select prof, curso from ensina order by prof')
        rows = cursor.fetchall()
        aulas = [{'professor': r[0], 'curso': r[1]} for r in rows]
        return {'Aulas por professor': aulas}
    else:
        cursor.execute('select curso, prof from ensina order by curso')
        rows = cursor.fetchall()
        aulas = [{'curso': r[0], 'professor': r[1]} for r in rows]
        return {'Aulas por curso': aulas}



@router.post('/cadastrar_professor_em_materia')
def cadastrar_professor_em_materia(prof: Professor, curso: CursoResponse, conn: sqlite3.Connection = Depends(get_db)):
    cursor = conn.cursor()
    try:
        dados = (prof.nome, curso.titulo)
        cursor.execute('insert into ensina (prof, curso) values (?,?)', dados)
        conn.commit()
        return {f"{prof.nome} cadastrado": curso.titulo}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        cursor.close()

@router.delete('/excluir_relacao_professor_curso')
def excluir_relacao_aluno_curso(prof: Professor, curso: CursoResponse, conn:sqlite3.Connection= Depends(get_db)):
    cursor = conn.cursor()
    dados = (prof.nome, curso.titulo)
    cursor.execute('delete from ensina where prof = (?) and curso = (?)', dados)
    conn.commit()
    return {f'{prof.nome} desvinculado': curso.titulo}


