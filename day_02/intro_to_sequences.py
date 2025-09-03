"""
Lesson: Lists and Dictionaries in Python
----------------------------------------
This file is intentionally incomplete.
Your job is to experiment, fill in blanks, and notice how lists and dictionaries store and organize data.
"""

# --- Section 1: Making a List ---

# Lists keep items in order.
# Example: foods = ["pizza", "sushi", "ice cream"]

# TODO: Create a list of 5 of your favorite foods.

foods = ["pizza", "sushi", "ice cream", "tacos", "pasta"]

# Access items by index (first = 0):
print(foods)
print(f"The first food is {foods[0]}")
print(f"The last food is {foods[-1]}")

# Bug Exploration:
# Try printing foods[100] below.
# Q: What error do you get, and what does it mean?

print(foods[100])

# --- Section 2: Changing a List ---

# Lists can grow and shrink using built-in methods.

# TODO: Add a new food to the end of your list with .append()
foods.append("ramen")

# TODO: Insert a food at the beginning with .insert()
foods.insert("burger")

# TODO: Remove one food from the list with .remove()
foods.remove("sushi")

# TODO: How many foods are in the list? Use len()
foods.len("6")

# Bug Exploration:
# Try removing something that isn’t in the list:
# foods.remove("chocolate")
# Q: What happens? Why?
foods.remove("chocolate")

# --- Section 3: Loops with Lists ---

# TODO: Write a for loop that prints each food in your list one by one.


# Bug Exploration:
# Change your loop to go past the length of the list:
for i in range(______):
    print(f"Index {i} → {foods[i]}")
# Q: Why does this cause an error?


# --- Section 4: Dictionaries (Key–Value Pairs) ---

# Dictionaries let us label data with keys.
# Example: 
me = {
    "name": "Kevin",
    "age": 30,
    "student": False
    }

# TODO: Make a dictionary with at least 3 pieces of information about yourself.
me = {
    "name": "kimberly",
    "age": 18,
    "student": True
    "favourite_color": "blue"
    }

# Access values using keys by using the .get() method rather than indexing
# print(f"My name is {me['name']}")
# print(f"My age is {me['age']}")
# print(f"My favorite color is {me['favorite_color']}")
print(f"my name is{me.get['name']}")
print(f"my age is{me.get['age']}")
print(f"my favourite color is{me.get['age']}")
# Bug Exploration:
# Try printing a key that doesn’t exist.
# print(me["hometown"])
# Q: What kind of error is this? How could you check if a key exists before using it? Why is the .get() method useful here?


# --- Section 5: Changing a Dictionary ---

# TODO: Add a new key-value pair.
me["hobby"] = "drawing"

# TODO: Change the value of an existing key.
me["age"] = "19"

# TODO: Remove one key-value pair.
me.pop("student")

# Bug Exploration:
# Try removing a key that doesn’t exist:
# me.pop("grade")
# Q: What happens? Is this similar to removing from a list?
me.pop("baddie")

# --- Section 6: Loops with Dictionaries ---

# TODO: Write a loop that prints both the keys and values in your dictionary using .items()
print(f{key}: {value})

# Bug Exploration:
# What happens if you loop over just the dictionary without calling .items()?
# for key in me:
#     print(key)
print(key)
# Q: Why does it only print the keys? How can you change your for loop to print key and value pairs?


# --- Section 7: Mixing Lists and Dictionaries ---

# TODO: Create a list of dictionaries. 
# Example: a list of 3 friends, where each friend has a name and favorite food.
friends = [
    {"name": "mia", "favorite_food": "sushi"}
    {"name": "bob", "favorite_food": "bread"}
    {"name": "boobooop", "favorite_food": "pancakes"}
]

# TODO: Print the favorite food of the second friend.
print(freinds[1][favorite_food])

# TODO: Loop through and print "<name> likes <food>" for each friend.
print(f"{friend['name']} likes {friend['favorite_food']}")

# Bug Exploration:
# What happens if you try to access friend["hobby"] when "hobby" doesn’t exist in the dictionary?
# Q: How might you prevent this kind of error in real programs?


# --- Section 8: Reflection ---
# Answer in comments:
# 1. How is a list different from a dictionary?
# 2. When would you want to use a dictionary instead of a list?
# 3. Can you think of a real-world situation where combining lists and dictionaries would be useful?
# 4. What types of mistakes gave you the most errors today?
# 5. How might noticing errors actually help you learn?