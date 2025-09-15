import json
from menu_item import MenuItem

class Restaurant:
    def __init__(self, data_file):
        self.data_file = data_file
        self.items = []
        self.load_data()
        
    def load_data(self):
        try:
            with open(self.data_file, 'r') as file:
                # Check if file is empty
                content = file.read().strip()
                if not content:
                    print("Data file is empty. Starting with fresh data.")
                    self.items = []
                    return
                    
                data = json.loads(content)
                self.items = [MenuItem(item["id"], item["name"], item["price"]) for item in data["items"]]
                
        except FileNotFoundError:
            print("Data file not found. Starting with fresh data.")
            self.items = []
        except json.JSONDecodeError as e:
            print(f"Error reading data file: {e}. Starting with fresh data.")
            self.items = []
        except KeyError as e:
            print(f"Invalid data format in file: {e}. Starting with fresh data.")
            self.items = []
        
    def save_data(self):
        data = {"items": [item.to_dict() for item in self.items]}
        with open(self.data_file, 'w') as file:
            json.dump(data, file, indent=2)
        
    def add_item(self, name, price):
        # Find the next available ID
        if self.items:
            new_id = max(item.id for item in self.items) + 1
        else:
            new_id = 1
        item = MenuItem(new_id, name, price)
        self.items.append(item)
        return item
        
    def find_item_by_id(self, item_id):
        for item in self.items:
            if item.id == item_id:
                return item
        return None
    
    def remove_item(self, item_id):
        item = self.find_item_by_id(item_id)
        if item:
            self.items.remove(item)
            return True
        return False
    
    def update_item(self, item_id, name, price):
        item = self.find_item_by_id(item_id)
        if item:
            item.name = name
            item.price = price
            return item
        return None
    
    def view_all_items(self):
        return self.items