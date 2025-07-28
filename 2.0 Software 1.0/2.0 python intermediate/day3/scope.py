# Scope determines where in your program a variable can be accessed. Think of it as the "living space" of your variables.

# Local Scope vs Global Scope


# # Global variable - lives in the "main house"
# house_name = "Python Manor"

# def cook_dinner():
#     # Local variable - lives only in this "kitchen"
#     recipe = "Spaghetti Carbonara"
#     cooking_time = 30

#     # This function can access both local and global variables
#     print(f"Cooking {recipe} in {house_name}")
#     print(f"Estimated cooking time: {cooking_time} minutes")

#     return recipe

# def set_table():
#     # Different local scope - this is like a "dining room"
#     plates = 4
#     utensils = "fork, knife, spoon"

#     # Can access global variable
#     print(f"Setting table for dinner at {house_name}")
#     print(f"Using {plates} plates with {utensils}")

#     # Cannot access recipe or cooking_time from cook_dinner function
#     # This would cause an error: print(recipe)

# # Using the functions
# dinner = cook_dinner()
# set_table()

# # Can access global variable
# print(f"Welcome to {house_name}!")

# # Cannot access local variables from outside their functions
# # This would cause an error: print(recipe)



# Modifying Global Variables

# Global counter
total_visitors = 0

def welcome_visitor(name):
    """Welcome a visitor and update the counter."""
    global total_visitors  # Ask permission to modify global variable
    total_visitors += 1
    print(f"Welcome, {name}! You are visitor #{total_visitors}")

def show_visitor_count():
    """Display current visitor count."""
    print(f"Total visitors today: {total_visitors}")

# Using the functions
welcome_visitor("Alice")
welcome_visitor("Bob")
welcome_visitor("Charlie")
show_visitor_count()
