# main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Hello World during the coronavirus pandemic}

# class HelloNameResponse(BaseModel):
#     message: str 

# @app.get('/hello/{name}', response_model=HelloNameResponse)
# def hello_name(name:str):
#     return HelloNameResponse(message=f"Hello {name}")
#     # return {"message": f"Hello {name}"}

#odpalenie appki:
#uvicorn app:app