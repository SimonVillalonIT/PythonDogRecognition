from DogDetector import dog_detector 
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://0.0.0.0:3000",
]



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def read_root():
    return "Hello World!"

@app.get('/detect')
def get_detect():
    return {"isadog": dog_detector("/home/simonvillalon/Downloads/1.jpg")}
