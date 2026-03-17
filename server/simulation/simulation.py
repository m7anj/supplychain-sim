from node import Node

def runSimulation(request: SimulationRequest) -> SimulationResponse:
  days = request.days
  mean_demand = request.mean_demand
  demand_std = request.demand_std
  lead_times = request.lead_times
  disruption = request.disruption

  # TODO: Create new nodes, and make them do the things they need to do
  
  supplier = Node("supplier", inv=500, reorder_point=200, order_quantity=300, lead_time=0)
  factory  = Node("factory",  inv=400, reorder_point=150, order_quantity=250, lead_time=lead_times.supplier_to_factory)
  dc       = Node("dc",       inv=300, reorder_point=100, order_quantity=200, lead_time=lead_times.factory_to_dc)
  retailer = Node("retailer", inv=200, reorder_point=80,  order_quantity=150, lead_time=lead_times.dc_to_retailer)

  