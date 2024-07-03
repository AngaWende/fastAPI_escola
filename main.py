from fastapi import FastAPI
import uvicorn
from escola.routers import alunos_router, cursos_router, professores_router, matricula_router, vincular_professor_router

app = FastAPI()


@app.get('/')
def boas_vindas() -> str:
    return 'Bem vindo'


app.include_router(alunos_router.router)
app.include_router(cursos_router.router)
app.include_router(professores_router.router)
app.include_router(matricula_router.router)
app.include_router(vincular_professor_router.router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
