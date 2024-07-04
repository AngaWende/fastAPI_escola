import sqlite3
import os
from fastapi import FastAPI, Depends
import uvicorn
from escola.routers import alunos_router, cursos_router, professores_router, matricula_router, vincular_professor_router

app = FastAPI()


# def get_db():
#     db_path = os.path.join(os.path.dirname(__file__), 'shared', 'escola.db')
#     conn = sqlite3.connect(db_path)
#     try:
#         yield conn
#     finally:
#         conn.close()

@app.get('/')
def boas_vindas() -> str:
    return 'Bem vindo'

# @app.get('/LISTA_DE_ALUNOS')
# def lista_de_alunos(conn: sqlite3.Connection = Depends(get_db)):
#     cursor = conn.cursor()
#     cursor.execute('select * from alunos')
#     rows = cursor.fetchall()
#     alunos = [{'id': row[0], 'nome': row[1], 'cpf': row[2], 'e_mail': row[3]} for row in rows]
#     return {'alunos': alunos}


app.include_router(alunos_router.router)
app.include_router(cursos_router.router)
app.include_router(professores_router.router)
app.include_router(matricula_router.router)
app.include_router(vincular_professor_router.router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
