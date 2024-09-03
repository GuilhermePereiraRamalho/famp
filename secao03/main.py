from fastapi import FastAPI, status, Path, Query, Header, Depends
from fastapi.exceptions import HTTPException
from fastapi.responses import Response
from models import Curso, cursos
from typing import List, Optional, Any, Dict
from time import sleep


def fake_db():
    try:
        print("Abrindo conexão com banco de dados...")
        sleep(1)
    finally:
        print("Fechando conexão com banco de dados...")
        sleep(1)

app = FastAPI(
    title="Api de Cursos da Geek University",
    version="0.0.1",
    description="Uma api para estudo do FastAPI",
    )


@app.get(
            "/cursos",
            response_model=List[Curso],
            description="Retorna todos os cursos ou uma lista vazia", 
            summary="Retorna todos os cursos", 
            tags=["Cursos"],
            response_description="Cursos encontrados com sucesso!"
        )
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos


@app.get(
            "/cursos/{curso_id}",
            response_model=Curso,
            tags=["Cursos"]
        )
async def get_curso(curso_id: int = Path(title="ID do Curso", description="Deve ser entre 1 e 2", gt=0, lt=3), db: Any = Depends(fake_db)):
    try:
        for curso in cursos:
            if curso.id == curso_id:
                return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado!")


@app.post("/cursos", status_code=status.HTTP_201_CREATED, tags=["Cursos"])
async def post_curso(curso: Curso):
    next_id: int = len(cursos) + 1
    curso.id = next_id
    cursos.append(curso)
    return curso


@app.put("/cursos/{curso_id}", tags=["Cursos"])
async def put_curso(curso_id: int, curso: Curso, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe um curso com o ID: {curso_id}")
    
@app.delete('/cursos/{curso_id}', tags=["Cursos"])
async def delete_curso(curso_id: int, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        del cursos[curso_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe um curso com o ID: {curso_id}")


@app.get("/calculadora", tags=["Calculadora"])
async def calcular(a: int = Query(gt=5), b: int = Query(gt=10), x_geek: str = Header(default=None), c: Optional[int] = None):
    soma: int = a + b
    if c:
        soma += c

    print(f"X-GEEK: {x_geek}")

    return {"resultado": soma}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)