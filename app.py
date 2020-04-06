from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Hello World during the coronavirus pandemic!"}

@app.route("/method", methods=["GET", "POST", "PUT", "DELETE"])
def get_method(req: Request):
    return {"method": req.method}


class HelloNameResponse(BaseModel):
    message: str 

@app.get('/hello/{name}', response_model=HelloNameResponse)
def hello_name(name:str):
    return HelloNameResponse(message=f"Hello {name}")
    # return {"message": f"Hello {name}"}

#odpalenie appki:
#uvicorn app:app