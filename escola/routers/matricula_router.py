import sqlite3

from fastapi import APIRouter, Depends, HTTPException

from escola.routers.alunos_router import AlunoResponse
from escola.routers.cursos_router import CursoResponse
from shared.database import get_db

router = APIRouter(prefix='/matricula')




@router.post('/listar_matriculas')
def listar_matriculas(aluno_ou_curso: str, conn: sqlite3.Connection = Depends(get_db)):
    cursor = conn.cursor()
    if aluno_ou_curso == 'aluno':
        cursor.execute('select aluno, curso from matricula order by aluno')
        rows = cursor.fetchall()
        mats = [{'aluno': r[0], 'curso': r[1]} for r in rows]
        return {'Matrículas por aluno': mats}
    else:
        cursor.execute('select curso, aluno from matricula order by curso')
        rows = cursor.fetchall()
        mats = [{'curso': r[0], 'aluno': r[1]} for r in rows]
        return {'Matrículas por curso': mats}

@router.post('/matriculas_por_aluno')
def matriculas_por_aluno(aluno: AlunoResponse, conn: sqlite3.Connection = Depends(get_db)):
    cursor = conn.cursor()
    dados = (aluno.nome,)
    cursor.execute('select * from matricula where aluno = (?)', dados)
    rows = cursor.fetchall()
    matriculas = [{'curso': r[1]} for r in rows]
    return {f'matriculas {aluno.nome}': matriculas}


@router.post('/matricular_aluno')
def matricular_aluno(aluno: AlunoResponse, curso: CursoResponse, conn: sqlite3.Connection = Depends(get_db)):
    cursor = conn.cursor()
    try:
        dados = (aluno.nome, curso.titulo)
        cursor.execute('insert into matricula (aluno, curso) values (?,?)', dados)
        conn.commit()
        return {f"{aluno.nome} matriculado": curso.titulo}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    finally:
        cursor.close()



@router.delete('/excluir_relacao_aluno_curso')
def excluir_relacao_aluno_curso(aluno: AlunoResponse, curso: CursoResponse, conn:sqlite3.Connection= Depends(get_db)):
    cursor = conn.cursor()
    dados = (aluno.nome, curso.titulo)
    cursor.execute('delete from matricula where aluno = (?) and curso = (?)', dados)
    conn.commit()
    return {f'{aluno.nome} desmatriculado': curso.titulo}

