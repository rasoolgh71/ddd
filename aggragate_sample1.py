class OrderItem:
    def __init__(self, product_id, quantity, price):
        self.product_id = product_id
        self.quantity = quantity
        self.price = price

    def calculate_total(self):
        return self.quantity * self.price


class Order:
    def __init__(self, order_id, customer_id):
        self.order_id = order_id
        self.customer_id = customer_id
        self.items = []  # List of OrderItem objects

    def add_item(self, product_id, quantity, price):
        item = OrderItem(product_id, quantity, price)
        self.items.append(item)

    def calculate_total(self):
        total = sum(item.calculate_total() for item in self.items)
        return total