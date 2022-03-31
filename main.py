from fastapi import FastAPI
import redis

r = redis.Redis(
    host='redis',
    decode_responses=True,
)

app = FastAPI()


@app.get("/")
def hello_world():
    r.incr("counter")
    counter = r.get("counter")
    return {"message": f"Hello World! {counter}"}

@app.get("/owen")
def hello_owen():
    return {"message": f"Hello Owen!"}


if __name__ == "__main__":
    print(hello_world())