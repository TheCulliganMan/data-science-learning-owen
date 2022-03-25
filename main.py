from fastapi import FastAPI

app = FastAPI()
COUNTER: int = 0


@app.get("/")
def hello_world():
    global COUNTER
    COUNTER += 1
    return {"message": f"Hello World! {COUNTER}"}


if __name__ == "__main__":
    print(hello_world())