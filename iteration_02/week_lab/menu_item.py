class MenuItem:

    def __init__(self,item_id,name,price):
        self.id = item_id
        self.name = name
        self.price = price

    def display_info(self):
        return f"{self.name}: $(self.price)"
    
    