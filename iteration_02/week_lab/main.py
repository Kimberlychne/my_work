from menu_item import MenuItem
from restaurant import Restaurant

def get_valid_price():
    while True:
        price = float(input("Enter price: $"))
        if price > 0:
            return price
        else:
            print("Item price must be a postive number")

def get_non_empty_string(val):
    while True:
        input_value = input(val).strip()
        if input_value:
            return input_value
        else:
            print("Field can't be empty")

def display_menu():
    print("\n============= RESTAURANT MENU SYSTEM =============\n")
    print("1. View All Items")
    print("2. Add New Item")
    print("3. Find Item by ID")
    print("4. Update Item")
    print("5. Delete Item")
    print("6. Save and Exit")

def main():
    restaurant = Restaurant("restaurant_data.json")
    
    while True:
        display_menu()
        choice = input("Select option(1-6): ")
        
        if choice == "1":
            items = restaurant.view_all_items()
            if items:
                print("\nMenu Items:")
                for item in items:
                    print(f"{item}")
            else:
                print("No items in the menu")
                
        elif choice == "2":
            name = get_non_empty_string("Enter Item Name: ")
            price = get_valid_price()
            item = restaurant.add_item(name, price)
            print(f"Added Item: {item}")
            
        elif choice == "3":
            item_id = int(input("Enter the item ID: "))
            item = restaurant.find_item_by_id(item_id)
            if item:
                print(f"Found item: {item}")
            else:
                print("Item not found")
                
        elif choice == '4':
            item_id = int(input("Enter the item ID: "))
            item = restaurant.find_item_by_id(item_id)
            if item:
                name = get_non_empty_string("Enter new name: ")
                price = get_valid_price()
                item = restaurant.update_item(item_id, name, price)
                print(f"Updated item: {item}")
            else:
                print("Item not found")
                
        elif choice == "5":
            item_id = int(input("Enter the item ID: "))
            item = restaurant.find_item_by_id(item_id)
            if item:
                restaurant.remove_item(item_id)
                print(f"Deleted item: {item}")
            else:
                print("Item not found")
                
        elif choice == '6':
            restaurant.save_data()
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")
            

if __name__ == "__main__":
    main()
