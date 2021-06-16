from fastapi import FastAPI 
from pydantic import BaseModel

from pyteeth import Teeth

class Image(BaseModel):
    url: str


app = FastAPI()





@app.post("/")
def root(image:Image):
    print(image.url)

    teeth = Teeth(image.url)
    
    #return image
    return {"message": teeth.coords}