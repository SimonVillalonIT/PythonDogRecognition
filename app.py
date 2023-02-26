from DogDetector import dog_detector 
from fastapi import FastAPI, File, UploadFile, Form
import os
import time
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

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

@app.post('/detect')
async def post_detect(image: UploadFile = File(...)):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filename = f'{dir_path}/uploads/{time.time()}-{image.filename}'
    f = open(f'{filename}', 'wb')
    content = await image.read()
    f.write(content)
    result = {"Result": dog_detector(filename)}
    os.remove(filename)
    return result
