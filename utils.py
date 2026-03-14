import os
import json
import uuid
from datetime import datetime


def read_template(path: str) -> str:
    with open(path, "r") as f:
        return f.read()


def save_quote(quote: str) -> dict:
    os.makedirs("outputs", exist_ok=True)
    entry = {
        "id": str(uuid.uuid4()),
        "date": datetime.now().isoformat(),
        "quote": quote,
    }
    output_path = "outputs/quotes.json"
    if os.path.exists(output_path):
        with open(output_path, "r") as f:
            data = json.load(f)
    else:
        data = []
    data.append(entry)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    return entry
