from fastapi import FastAPI
from app.models import EstimateRequest, EstimateResponse
from app.services import get_route_from_mapbox, calculate_fare

app = FastAPI(
    title="Ride Fare API",
    description="API de estimación de viajes tipo Uber usando FastAPI y Mapbox Directions API",
    version="1.0.0"
)

history = []


@app.get("/")
def root():
    return {
        "message": "Bienvenido a Ride Fare API",
        "endpoints": [
            "GET /",
            "GET /health",
            "POST /estimate",
            "GET /history"
        ]
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/estimate", response_model=EstimateResponse)
def estimate_trip(request: EstimateRequest):
    origin = request.origin.model_dump()
    destination = request.destination.model_dump()

    profile = "driving"
    distance_km, duration_min = get_route_from_mapbox(origin, destination, profile)
    fare = calculate_fare(distance_km, duration_min, request.vehicle_type)

    result = {
        "origin": origin,
        "destination": destination,
        "profile": f"mapbox/{profile}",
        "distance_km": distance_km,
        "duration_min": duration_min,
        "vehicle_type": request.vehicle_type,
        "fare": fare
    }

    history.append(result)
    return result


@app.get("/history")
def get_history():
    return {
        "total": len(history),
        "data": history
    }