from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def pong():
  return {"ping": "pong!"}

@app.get("/simulate")
def simulate():
  # TODO: Implementing a /simulate entry point for the sim engine to be ran
  return {"result": "this is a test"}



def main():
    print("Hello from server!")


if __name__ == "__main__":
    main()
