from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import math


app = FastAPI()

class SquareRootResponse(BaseModel):
    number: int
    square_root: float

def calculate_square_root(number: int) -> SquareRootResponse:
    if not 10 <= number <= 100:
        raise HTTPException(status_code=400, detail="The number must be between 10 and 100")
    square_root = math.sqrt(number)
    return SquareRootResponse(number=number, square_root=square_root)

@app.get("/square-root")
def get_square_root(number: int):
    return calculate_square_root(number)

