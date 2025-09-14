import json

data_path = "iteration_02/week_lab/restaurant_data.json"


class Restaurant:

    
    
    def add_menu_item(self):    
    #add a new manu item to the specified category#
        with open(data_path,'r') as file:
            restaurant_data = json.load(file)

        category = input("enter category (appetizer/entree/dessert):").lower().strip()
        name = input("Enter item name: ").strip()
        price = float(input("Enter price:"))
        stock_status = input("Is this item in stock? (y/n):").strip().lower()
        stock_status == 'y'
        item_id = self.get_next_id(category)
        new_item = {
            "id":item_id,
            "name":name,
            "in stock": stock_status
        }


    def delete_menu_item(self):    
        #add a new manu item to the specified category#
        with open(data_path,'r') as file:
            restaurant_data = json.load(file)

        delItem = input("enter name of the item you want to delete").lower().strip()
        item_id = self.get_next_id(category)
        
        def __init__(self):
            self.items = []

        def add_item(self,item):
            self.items.append(item)
        def show_item(self):
            return self.items
        def delete_item(self,index):
            return None
        def list_items(self):
            for item in self.items:
                return None
            