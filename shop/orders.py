import time


def create_order(user, cart):
    """Create an order from the user's cart and return it as a dict."""
    return {
        "user": user.email,
        "items": list(cart.items),
        "total": cart.total(),
        "status": "created",
        "created_at": time.time(),
    }


def cancel_order(order):
    """Cancel an order that has not been shipped yet."""
    if order["status"] == "shipped":
        raise ValueError("cannot cancel a shipped order")
    order["status"] = "cancelled"
    return order
