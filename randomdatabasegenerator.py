import json
import random
from datetime import datetime, timedelta

names = [
    "John Smith", "Emily Johnson", "Michael Brown", "Sarah Davis", "David Wilson",
    "Olivia Martinez", "James Anderson", "Sophia Thomas", "Daniel Taylor", "Isabella Moore"
]

cities = [
    "Atlanta, GA", "Charlotte, NC", "Dallas, TX", "Austin, TX", "Chicago, IL",
    "Detroit, MI", "Miami, FL", "Orlando, FL", "Denver, CO", "Seattle, WA",
    "Phoenix, AZ", "Las Vegas, NV", "New York, NY", "Boston, MA"
]

statuses = ["In Transit", "Delivered", "Out for Delivery", "Delayed"]

package_types = ["Standard", "Fragile", "Perishable", "Oversized", "Electronics"]

delay_reasons = [
    "Severe weather conditions",
    "Mechanical issue with vehicle",
    "High shipment volume",
    "Traffic delays",
    "Customs processing delay"
]

def random_date(start_days_ago=3):
    return datetime.now() - timedelta(days=random.randint(0, start_days_ago),
                                      hours=random.randint(0, 23))

def generate_history(origin, destination, ship_date, status, delayed):
    history = []

    current_time = ship_date
    history.append({
        "location": origin,
        "timestamp": current_time.isoformat(),
        "status": "Shipment picked up"
    })

    steps = random.randint(2, 4)
    for _ in range(steps):
        current_time += timedelta(hours=random.randint(6, 18))
        history.append({
            "location": random.choice(cities),
            "timestamp": current_time.isoformat(),
            "status": "In Transit"
        })

    if delayed:
        current_time += timedelta(hours=12)
        history.append({
            "location": random.choice(cities),
            "timestamp": current_time.isoformat(),
            "status": "Delayed"
        })

    if status == "Out for Delivery":
        current_time += timedelta(hours=6)
        history.append({
            "location": destination,
            "timestamp": current_time.isoformat(),
            "status": "Out for Delivery"
        })

    if status == "Delivered":
        current_time += timedelta(hours=6)
        history.append({
            "location": destination,
            "timestamp": current_time.isoformat(),
            "status": "Delivered"
        })

    return history, current_time

data = []

for i in range(1, 121):
    status = random.choice(statuses)
    delayed = True if status == "Delayed" else False

    origin = random.choice(cities)
    destination = random.choice(cities)

    ship_date = random_date()
    history, last_update = generate_history(origin, destination, ship_date, status, delayed)

    estimated_delivery = (datetime.now() + timedelta(days=random.randint(1, 3))).date().isoformat()

    shipment = {
        "tracking_number": f"TRK{100000 + i}",
        "customer_name": random.choice(names),
        "origin": origin,
        "destination": destination,
        "status": status,
        "current_location": history[-1]["location"],
        "ship_date": ship_date.isoformat(),
        "last_updated": last_update.isoformat(),
        "estimated_delivery": estimated_delivery,
        "delay": delayed,
        "delay_reason": random.choice(delay_reasons) if delayed else None,
        "package_details": {
            "type": random.choice(package_types),
            "weight_lbs": round(random.uniform(1, 50), 2),
            "priority": random.choice(["Standard", "Express", "Overnight"])
        },
        "history": history
    }

    data.append(shipment)

with open("shipments.json", "w") as f:
    json.dump(data, f, indent=2)

print("Generated shipments.json with 120 realistic entries.")