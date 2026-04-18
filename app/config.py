import os
from dotenv import load_dotenv

load_dotenv()

MAPBOX_ACCESS_TOKEN = os.getenv("MAPBOX_ACCESS_TOKEN", "")
BASE_FARE = float(os.getenv("BASE_FARE", "1.50"))
COST_PER_KM = float(os.getenv("COST_PER_KM", "0.45"))
COST_PER_MIN = float(os.getenv("COST_PER_MIN", "0.10"))
CURRENCY = os.getenv("CURRENCY", "USD")