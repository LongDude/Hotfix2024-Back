from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()

@app.get("/calculate")
def calculate(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")

    sum_result = a + b
    difference_result = a - b
    product_result = a * b
    quotient_result = a / b if b != 0 else None

    return {
        "sum": sum_result,
        "difference": difference_result,
        "product": product_result,
        "quotient": quotient_result
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)