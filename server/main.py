from fastapi import FastAPI

app = FastAPI()

counter = 0


@app.get('/')
def main():
    global counter
    counter += 1
    return {"counter": counter}
