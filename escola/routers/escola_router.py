# import sqlite3
#
# from fastapi import APIRouter, Depends, HTTPException
# from pydantic import BaseModel
#
# router = APIRouter(prefix='/escola')
#
#
# def get_db():
#     conn = sqlite3.connect("shared/escola.db")
#     try:
#         yield conn
#     finally:
#         conn.close()
#
#
# class CursoResponse(BaseModel):
#     id: int
#     titulo: str
#     valor: float
#     carga_horaria: int
#
#
# class CursoRequest(BaseModel):
#     titulo: str
#     valor: float
#     carga_horaria: int
#
#
# class AlunoResponse(BaseModel):
#     nome: str
#     cpf: str
#     email: str
#
#
# class Professor(BaseModel):
#     nome: str
#
#
# # @router.get('/listar_cursos')
# # def listar_cursos(conn: sqlite3.Connection = Depends(get_db)):
# #     cursor = conn.cursor()
# #     cursor.execute('SELECT * FROM cursos')
# #     rows = cursor.fetchall()
# #     cursos = [{"id": row[0], "titulo": row[1], "valor": row[2], 'carga_horaria': row[3]} for row in rows]
# #     return {"cursos": cursos}
#
#
# # @router.get('/listar_alunos')
# # def listar_alunos(conn: sqlite3.Connection = Depends(get_db)):
# #     cursor = conn.cursor()
# #     cursor.execute('select * from alunos')
# #     rows = cursor.fetchall()
# #     alunos = [{'id': row[0], 'nome': row[1], 'cpf': row[2], 'e_mail': row[3]} for row in rows]
# #     return {'alunos': alunos}
#
#
# # @router.get('/listar_professores')
# # def listar_professores(conn: sqlite3.Connection = Depends(get_db)):
# #     cursor = conn.cursor()
# #     cursor.execute('select * from professores')
# #     rows = cursor.fetchall()
# #     prof = [{'id': r[0], 'nome': r[1]} for r in rows]
# #     return {'professores': prof}
# #
#
# # @router.post('/listar_matriculas')
# # def listar_matriculas(aluno_ou_curso: str, conn: sqlite3.Connection = Depends(get_db)):
# #     cursor = conn.cursor()
# #     if aluno_ou_curso == 'aluno':
# #         cursor.execute('select aluno, curso from matricula order by aluno')
# #         rows = cursor.fetchall()
# #         mats = [{'aluno': r[0], 'curso': r[1]} for r in rows]
# #         return {'Matrículas por aluno': mats}
# #     else:
# #         cursor.execute('select curso, aluno from matricula order by curso')
# #         rows = cursor.fetchall()
# #         mats = [{'curso': r[0], 'aluno': r[1]} for r in rows]
# #         return {'Matrículas por curso': mats}
# #
#
# # @router.post('/listar_aulas')
# # def listar_aulas(professor_ou_curso: str, conn: sqlite3.Connection = Depends(get_db)):
# #     cursor = conn.cursor()
# #     if professor_ou_curso == 'professor':
# #         cursor.execute('select prof, curso from ensina order by prof')
# #         rows = cursor.fetchall()
# #         aulas = [{'professor': r[0], 'curso': r[1]} for r in rows]
# #         return {'Aulas por professor': aulas}
# #     else:
# #         cursor.execute('select curso, prof from ensina order by curso')
# #         rows = cursor.fetchall()
# #         aulas = [{'curso': r[0], 'professor': r[1]} for r in rows]
# #         return {'Aulas por curso': aulas}
# #
#
# # @router.post('/matriculas_por_aluno')
# # def matriculas_por_aluno(aluno: AlunoResponse, conn: sqlite3.Connection = Depends(get_db)):
# #     cursor = conn.cursor()
# #     dados = (aluno.nome,)
# #     cursor.execute('select * from matricula where aluno = (?)', dados)
# #     rows = cursor.fetchall()
# #     matriculas = [{'curso': r[1]} for r in rows]
# #     return {f'matriculas {aluno.nome}': matriculas}
# #
#
# # @router.post('/add_curso', response_model=CursoResponse)
# # def inserir_curso(curso: CursoRequest, conn: sqlite3.Connection = Depends(get_db)):
# #     cursor = conn.cursor()
# #     try:
# #         dados = (curso.titulo, curso.valor, curso.carga_horaria)
# #         cursor.execute('insert into cursos (titulo, valor, carga_horaria) values (?,?,?)', dados)
# #         curso_id = cursor.lastrowid
# #         conn.commit()
# #         return {'id': curso_id, **curso.dict()}
# #     except sqlite3.Error as e:
# #         raise HTTPException(status_code=500, detail=f"Database error: {e}")
# #     finally:
# #         cursor.close()
#
#
# # @router.post('/add_aluno')
# # def add_aluno(aluno: AlunoResponse, conn: sqlite3.Connection = Depends(get_db)):
# #     cursor = conn.cursor()
# #     try:
# #         dados = (aluno.nome, aluno.cpf, aluno.email)
# #         cursor.execute('insert into alunos (nome, cpf, email) values (?,?,?)', dados)
# #         aluno_id = cursor.lastrowid
# #         conn.commit()
# #         return {"id": aluno_id, **aluno.dict()}
# #     except sqlite3.Error as e:
# #         raise HTTPException(status_code=500, detail=f"Database error: {e}")
# #     finally:
# #         cursor.close()
#
#
# # @router.post('/add_professor', response_model=Professor)
# # def add_professor(prof: Professor, conn: sqlite3.Connection = Depends(get_db)):
# #     cursor = conn.cursor()
# #     try:
# #         dados = (prof.nome,)
# #         cursor.execute('insert into professores (nome) values (?)', dados)
# #         prof_id = cursor.lastrowid
# #         conn.commit()
# #         return {"id": prof_id, **prof.dict()}
# #     except sqlite3.Error as e:
# #         raise HTTPException(status_code=500, detail=f"Database error: {e}")
# #     finally:
# #         cursor.close()
# #
#
# # @router.delete('/excluir_aluno')
# # def excluir_aluno(nome, conn: sqlite3.Connection = Depends(get_db)):
# #     cursor = conn.cursor()
# #     try:
# #         dados = (nome,)
# #         cursor.execute('delete from alunos where nome = (?)', dados)
# #         conn.commit()
# #         return {"Aluno excluído": nome}
# #     except sqlite3.Error as e:
# #         raise HTTPException(status_code=500, detail=f"Database error: {e}")
# #     finally:
# #         cursor.close()
#
#
# # @router.delete('/excluir_professor')
# # def excluir_professor(prof: Professor, conn: sqlite3.Connection = Depends(get_db)):
# #     cursor = conn.cursor()
# #     try:
# #         dados = (prof.nome,)
# #         cursor.execute('delete from professores where nome = (?)', dados)
# #         conn.commit()
# #         return {"Professor excluído": prof.nome}
# #     except sqlite3.Error as e:
# #         raise HTTPException(status_code=500, detail=f"Database error: {e}")
# #     finally:
# #         cursor.close()
#
#
# # @router.delete('/excluir_curso')
# # def excluir_curso(curso: CursoResponse, conn: sqlite3.Connection = Depends(get_db)):
# #     cursor = conn.cursor()
# #     try:
# #         dados = (curso.titulo,)
# #         cursor.execute('delete from cursos where titulo = (?)', dados)
# #         conn.commit()
# #         return {"Curso excluído": curso.titulo}
# #     except sqlite3.Error as e:
# #         raise HTTPException(status_code=500, detail=f"Database error: {e}")
# #     finally:
# #         cursor.close()
# #
#
# # @router.delete('/excluir_relacao_aluno_curso')
# # def excluir_relacao_aluno_curso(aluno: AlunoResponse, curso: CursoResponse, conn:sqlite3.Connection= Depends(get_db)):
# #     cursor = conn.cursor()
# #     dados = (aluno.nome, curso.titulo)
# #     cursor.execute('delete from matricula where aluno = (?) and curso = (?)', dados)
# #     conn.commit()
# #     return {f'{aluno.nome} desmatriculado': curso.titulo}
# #
#
# # @router.delete('/excluir_relacao_professor_curso')
# # def excluir_relacao_aluno_curso(prof: Professor, curso: CursoResponse, conn:sqlite3.Connection= Depends(get_db)):
# #     cursor = conn.cursor()
# #     dados = (prof.nome, curso.titulo)
# #     cursor.execute('delete from ensina where prof = (?) and curso = (?)', dados)
# #     conn.commit()
# #     return {f'{prof.nome} desvinculado': curso.titulo}
# #
#
#
# # @router.post('/matricular_aluno')
# # def matricular_aluno(aluno: AlunoResponse, curso: CursoResponse, conn: sqlite3.Connection = Depends(get_db)):
# #     cursor = conn.cursor()
# #     try:
# #         dados = (aluno.nome, curso.titulo)
# #         cursor.execute('insert into matricula (aluno, curso) values (?,?)', dados)
# #         conn.commit()
# #         return {f"{aluno.nome} matriculado": curso.titulo}
# #     except sqlite3.Error as e:
# #         raise HTTPException(status_code=500, detail=f"Database error: {e}")
# #     finally:
# #         cursor.close()
# #
#
# # @router.post('/cadastrar_professor_em_materia')
# # def cadastrar_professor_em_materia(prof: Professor, curso: CursoResponse, conn: sqlite3.Connection = Depends(get_db)):
# #     cursor = conn.cursor()
# #     try:
# #         dados = (prof.nome, curso.titulo)
# #         cursor.execute('insert into ensina (prof, curso) values (?,?)', dados)
# #         conn.commit()
# #         return {f"{prof.nome} cadastrado": curso.titulo}
# #     except sqlite3.Error as e:
# #         raise HTTPException(status_code=500, detail=f"Database error: {e}")
# #     finally:
# #         cursor.close()
