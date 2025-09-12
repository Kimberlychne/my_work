import menu_item
import restaurant
import json


#read a json file
data_path = "iteration_02/week_lab/restaurant_data.json"

with open(data_path,'r') as file:
    restaurant_data = json.load(file)

#write json file
item_data = {
    "id":5,
    "name":"New Item",
    "price":99.99
    }

for category in restaurant_data["menu"]:
    print(category["category"])
    for food in category["items"]:
        print(f"id: {food['id']} name: {food['name']} price:{food['price']}")


# with open(data_path, 'w') as file:
#     json.dump(data,file,indent=2)




# item = menu_item.MenuItem(1, "spring rolls",5.99)
# restaurant = restaurant.Restaurant()
# restaurant.add_item()
# print(restaurant.lsit_items())