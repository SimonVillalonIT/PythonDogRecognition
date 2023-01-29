from DogDetector import dog_detector 
from fastapi import FastAPI, File, UploadFile, Form
import os
import time

app = FastAPI()

@app.get('/')
def read_root():
    return "Hello World!"

@app.post('/detect')
async def post_detect(file: UploadFile = File(...)):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filename = f'{dir_path}/uploads/{time.time()}-{file.filename}'
    f = open(f'{filename}', 'wb')
    content = await file.read()
    f.write(content)
    result = {"Result": dog_detector(filename)}
    os.remove(filename)
    return result
