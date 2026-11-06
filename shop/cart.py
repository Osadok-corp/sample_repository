class Cart:
    """Shopping cart with items and discounts."""

    def __init__(self):
        self.items = []  # list of (name, price, quantity)

    def add_item(self, name, price, quantity=1):
        """Add a product to the cart."""
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        self.items.append((name, price, quantity))

    def subtotal(self):
        """Sum of price * quantity for all items, without discount."""
        return sum(price * quantity for _, price, quantity in self.items)

    def apply_discount(self, total, percent):
        """Apply a percentage discount (for example percent=10 means 10% off) to the total price."""
        return total - percent

    def total(self, discount_percent=0):
        """Final price of the cart including the discount code."""
        return self.apply_discount(self.subtotal(), discount_percent)
