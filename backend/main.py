
from fastapi import FastAPI

app = FastAPI(
    title="AtmoGraph API",
    description="Supply Chain Ripple Effect Predictor",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to AtmoGraph",
        "status": "Running"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

@app.get("/api/graph")
def get_graph():
    return {
        "nodes": [
            {"id": "S1", "name": "Supplier A", "type": "Supplier"},
            {"id": "M1", "name": "Manufacturer A", "type": "Manufacturer"},
            {"id": "P1", "name": "Port A", "type": "Port"}
        ],
        "edges": [
            {"source": "S1", "target": "M1", "relationship": "SUPPLIES_TO"},
            {"source": "M1", "target": "P1", "relationship": "SHIPS_THROUGH"}
        ]
    }
