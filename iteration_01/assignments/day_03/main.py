
from shapes import Rectangle, Circle, Triangle
from utils import cm2_to_m2, m2_to_cm2, compare_areas

def show_welcome():
    print("=" * 40)
    print("      SHAPE TOOLKIT")
    print("=" * 40)
    print("Create shapes and calculate their areas.")

def make_rectangle():
    print("\nMaking a rectangle...")
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    return Rectangle(length, width)

def make_circle():
    print("\nMaking a circle...")
    radius = float(input("Enter the radius: "))
    return Circle(radius)

def make_triangle():
    print("\nMaking a triangle...")
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    return Triangle(base, height)

def main():
    show_welcome()
    shapes = []
    
    while True:
        print("\nOptions:")
        print("1. Make a new shape")
        print("2. See all shapes")
        print("3. Compare two shapes")
        print("4. Convert area units")
        print("5. Quit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            print("\nShape types:")
            print("1. Rectangle")
            print("2. Circle") 
            print("3. Triangle")
            
            shape_choice = input("Enter shape number (1-3): ")
            
            if shape_choice == "1":
                new_shape = make_rectangle()
                shapes.append(new_shape)
                print(f"Made: {new_shape.describe()}")
            elif shape_choice == "2":
                new_shape = make_circle()
                shapes.append(new_shape)
                print(f"Made: {new_shape.describe()}")
            elif shape_choice == "3":
                new_shape = make_triangle()
                shapes.append(new_shape)
                print(f"Made: {new_shape.describe()}")
            else:
                print("Invalid choice.")
        
        elif choice == "2":
            if not shapes:
                print("No shapes created yet.")
            else:
                print("\nYour shapes:")
                for i, shape in enumerate(shapes, 1):
                    print(f"{i}. {shape.describe()}")
        
        elif choice == "3":
            if len(shapes) < 2:
                print("Need at least 2 shapes to compare.")
            else:
                print("\nYour shapes:")
                for i, shape in enumerate(shapes, 1):
                    print(f"{i}. {shape.__class__.__name__}")
                
                try:
                    num1 = int(input("Enter first shape number: ")) - 1
                    num2 = int(input("Enter second shape number: ")) - 1
                    
                    if 0 <= num1 < len(shapes) and 0 <= num2 < len(shapes):
                        result = compare_areas(shapes[num1], shapes[num2])
                        print(f"Result: {result}")
                except:
                    print("Invalid input.")
        
        elif choice == "4":
            if shapes:
                print("\nYour shapes:")
                for i, shape in enumerate(shapes, 1):
                    print(f"{i}. {shape.__class__.__name__}")
                
                try:
                    num = int(input("Enter shape number: ")) - 1
                    if 0 <= num < len(shapes):
                        area = shapes[num].area()
                        print(f"Area: {area:.2f} m²")
                        print(f"Area: {m2_to_cm2(area):.2f} cm²")
                except:
                    print("Invalid input.")
            else:
                print("No shapes created yet.")
        
        elif choice == "5":
            print("Goodbye!")
            break
        
        else:
            print("Please enter 1-5.")

if __name__ == "__main__":
    main()
