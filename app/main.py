import uvicorn
from fastapi import FastAPI

from app.manager import Manager

app=FastAPI()

manager=Manager()

@app.get("/")
def display_data():
    try:
       return manager.run()
    except Exception as e:
       return {"dont success", "error", e}




if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

