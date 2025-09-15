class MenuItem:

    def __init__(self, item_id, name, price):
        self.id = item_id  # Changed from 'item_id' to 'id'
        self.name = name
        self.price = price

    def to_dict(self):
        return {"id": self.id, "name": self.name, "price": self.price}
    
    def __str__(self):
        return f"{self.id}: {self.name} - ${self.price:.2f}"

