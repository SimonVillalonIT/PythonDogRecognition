import DogDetector
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return "Hello World!"

@app.get('/')
def detect():
    return DogDetector.dog_detector("/home/simonvillalon/Descargas/1.jpg")
