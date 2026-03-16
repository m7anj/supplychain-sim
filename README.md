# Supply Chain Digital Twin

This is a Supply Chain and Operations (SC&O) Simulator. It is essentially a replic of real supply chain operations in which users can run experiments on nodes in the chain, inject disruptions, and watch how stock levels, service quality, cost, and other metrics change due to this across every teir in simulated time.

## What It Does

- Simulates a full supply chain as discrete events running forward through time
- Runs thousands of scenarios using Monte Carlo simulation to produce probability-based insights
- Optimises safety stock and reorder points per node to minimise holding, ordering, and stockout costs
- Visualises the bullwhip effect — how small demand fluctuations amplify upstream
- Supports disruption injection (factory shutdowns, port closures) and shows downstream impact
- Offers two simulation modes: rule-based (pure logic) and AI-based (dynamic decision-making), with results compared side by side.

## Stack

- **Frontend:** Next.js, Tailwind CSS, Recharts
- **Backend:** FastAPI, SimPy, PuLP, NetworkX

## Running Locally

```bash
# Backend
cd server
uv run uvicorn main:app --reload

# Frontend
cd app
npm run dev
```
