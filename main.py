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


if __name__ == "__main__":
    print(hello_world())