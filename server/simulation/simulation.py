from node import Node

def runSimulation(request: SimulationRequest) -> SimulationResponse:
  days = request.days
  mean_demand = request.mean_demand
  demand_std = request.demand_std
  lead_times = request.lead_times
  disruption = request.disruption

  # TODO: Create new nodes, and make them do the things they need to do
  