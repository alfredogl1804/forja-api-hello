from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def root():
    return {'servicio': 'El Monstruo Hello', 'estado': 'vivo'}
