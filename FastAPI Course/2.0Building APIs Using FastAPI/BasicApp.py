from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def home():
    return {'message': "Welcome to the home page"}


@app.get('/cart')
def getcart():
    return{'message': 'Welcome to the cart PAGE'}

## Return a pydantic object rather than a dict 

class User(BaseModel):
    id: int
    name: str

@app.get('/user', response_model=User)
def getuser():
    return User(id=11907019,name="GT Nagaraj")
