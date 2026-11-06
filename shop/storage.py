import json


def save_orders(orders, path):
    """Write the list of orders to a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(orders, f)


def load_orders(path):
    """Read the list of orders from a JSON file."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)
