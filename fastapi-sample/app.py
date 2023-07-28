from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route for the root endpoint
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Define a route for a custom endpoint
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}
