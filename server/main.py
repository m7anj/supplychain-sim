from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def pong():
  return {"ping": "pong!"}

@app.post("/simulate")
def simulate(request: SimulationRequest):
  result = runSimulation(SimulationRequest).dumps()
  return result



def main():
    print("Hello from server!")


if __name__ == "__main__":
    main()
