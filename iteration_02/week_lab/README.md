PROGRAM DESCRIPTION
This program manages our restaurant "Oriental Flavors" 's menu. It allows user to to read the menu, add new dishes to the menu, delete dishes from the menu and also save their changes to the menu. Each dish has a unqiue ID, name and a price. Changes will be saved to a JSON file.

KEY FEATURES:
-View all Items
-Add new items by providing name and price
-Delete items
-save changes to a JSON file and exit
-retrive a specific menu item using the ID

SETUP AND RUN INSTRUCTIONS:
-clone the repository 
-run the program

EXAMPLE INPUT/OUTPUT INTERACTION:
1. view all items
2. add new item
3. find item by ID
4. update Item
5. delete Item
6. Save and Exit


Select Option (1-5): 1

Menu Items:
(displays menu items)

select option (1-5): 2
Enter Item Name : French Fries
Enter price: $3.50

Select option(1-5): 4
Enter the item ID: 2
Enter new name: Truffle Fries
Enter price: $5.99
updated item: True

Select option(1-5): 6
data saved. Exiting...


FOLDER STRUCTURE EXPLANATION

Main.py
-displays introduction
-handles user interaction(adding, deleting, and etc)through input of numbers
-imports Menu and Restaurant classes

restaurant.py
-load menu items from restaurant_data.json
-operates add_item, find_item_by_id and etc


menu_item.py
-defines what a menu item is.
-Shows the ID, name, price of a single menu item





