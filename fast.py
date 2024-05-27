from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def chap():
    return("Hello World")
