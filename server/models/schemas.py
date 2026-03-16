from pydantic import BaseModel
from typing import Optional

class LeadTimes(BaseModel):
    supplier_to_factory: int = 7
    factory_to_dc: int = 5
    dc_to_retailer: int = 2

class Disruption(BaseModel):
    node: str        # this could be something like "supplier", "factory", "dc", "retailer", ideally these would be enforced by actual types however for now, i think using a str makes the most sense.
    start_day: int
    duration: int

class SimulationRequest(BaseModel):
    days: int = 365
    mean_demand: float = 100.0
    demand_std: float = 20.0
    lead_times: LeadTimes = LeadTimes()
    service_level_target: float = 0.95
    disruption: Optional[Disruption] = None
    mode: str = "rulebased" # soon to implement "aibased" which uses AI for simulation
    monte_carlo_runs: int = 1

class NodeRecommendation(BaseModel):
    safety_stock: float
    reorder_point: float
    order_quantity: float

class SimulationResponse(BaseModel):
    inventory_history: dict[str, list[float]]  # node → daily levels
    total_cost: float
    holding_cost: float
    ordering_cost: float
    stockout_cost: float
    service_level: float
    stockout_count: int
    recommendations: dict[str, NodeRecommendation]