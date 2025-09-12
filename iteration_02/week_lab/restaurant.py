import json

data_path = "iteration_02/week_lab/restaurant_data.json"


class Restaurant:
    
    def add_menu_item():    
        with open(data_path,'r') as file:
            restaurant_data = json.load(file)

    while True:
        category = input("enter category (appetizer/entree/dessert):").lower().strip()
    if category in['appetizer,entree,dessert']:

      def __init__(self):
        self.items = []

    def add_item(self,item):
        self.items.append(item)
    def show_item(self):
        return self.items
    def delete_item(self,index):

        def list_items(self):
for item in self.items: