import uvicorn
from fastapi import FastAPI

from app.manager import Manager
import logging
app=FastAPI()
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
manager=Manager()
manager.run()

@app.get("/")
def display_data():
    try:
       return manager.display()
    except Exception as e:
       return {"dont success", "error", e}





# if __name__=="__main__":
#     uvicorn.run(app)
