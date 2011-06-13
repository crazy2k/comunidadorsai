from comunidadorsai import app

@app.route('/')
def hello():
    return "Halloa!"
