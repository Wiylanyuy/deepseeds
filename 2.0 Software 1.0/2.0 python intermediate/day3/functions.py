# # withouth functions repitivive and error-prone 
# radius1 = 5
# area1 = 3.14159 * radius1 * radius1
# print(f"Area of circle 1: {area1}")

# radius2 = 10
# area2 = 3.14159 * radius2 * radius2
# print(f"Area of circle 2: {area2}")

# radius3 = 7
# area3 = 3.14159 * radius3 * radius3
# print(f"Area of circle 3: {area3}")

# # With functions - clean, reusable, and maintainable
# def calculate_circle_area(radius):
#     """Calculate the area of a circle given its radius."""
#     pi = 3.14159
#     area = pi * radius * radius
#     return area

# # Now we can use our function multiple times
# area1 = calculate_circle_area(5)
# area2 = calculate_circle_area(10)
# area3 = calculate_circle_area(7)

# print(f"Area of circle 1: {area1}")
# print(f"Area of circle 2: {area2}")
# print(f"Area of circle 3: {area3}")


# function to greet someone by name
# def greet_person(name):
#     """This function greets a person by name."""
#     message = f"Hello, {name}! Welcome to Python programming!"
#     return message

# # Using the function
# greeting = greet_person("Alice")
# print(greeting)



# FUNCTIONS WITH MUTIPLE PARAMETERS
# def calculate_rectangle_area(length, width):
#     """Calculate the area of a rectangle."""
#     area = length * width
#     return area

# def introduce_person(first_name, last_name, age, city):
#     """Create a personal introduction."""
#     introduction = f"Hi, I'm {first_name} {last_name}. I'm {age} years old and I live in {city}."
#     return introduction

# # Using functions with multiple parameters
# rect_area = calculate_rectangle_area(10, 5)
# intro = introduce_person("John", "Doe", 30, "New York")

# print(f"Rectangle area: {rect_area}")
# print(intro)



# Functions with Default Parameters
# def greet_with_title(name, title="Friend"):
#     """Greet someone with an optional title."""
#     return f"Hello, {title} {name}!"

# # Using the function with and without the optional parameter
# print(greet_with_title("Alice"))                # Uses default title
# print(greet_with_title("Bob", "Dr."))          # Uses custom title
# print(greet_with_title("Charlie", "Professor")) # Uses custom title



# Functions That Don't Return Values

# def print_separator():
#     """Print a decorative separator line."""
#     print("=" * 50)

# def countdown(start_number):
#     """Count down from a given number."""
#     for i in range(start_number, 0, -1):
#         print(f"Countdown: {i}")
#     print("Blast off! 🚀")

# # Using functions that don't return values
# print_separator()
# print("Welcome to the Launch Sequence")
# print_separator()
# countdown(5)

# Function Examples and Practice

# Temperature converter function
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Password strength checker
def check_password_strength(password):
    """Check if a password meets basic security requirements."""
    # Initialize strength indicators
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    # Check each character in the password
#     for char in password:
#         if char.isupper():
#             has_upper = True
#         elif char.islower():
#             has_lower = True
#         elif char.isdigit():
#             has_digit = True
#         elif char in "!@#$%^&*()":
#             has_special = True

#     # Determine strength level
#     if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
#         return "Strong"
#     elif len(password) >= 6 and has_upper and has_lower and has_digit:
#         return "Medium"
#     else:
#         return "Weak"

# # Simple calculator functions
# def add(a, b):
#     """Add two numbers."""
#     return a + b

# def subtract(a, b):
#     """Subtract second number from first."""
#     return a - b

# def multiply(a, b):
#     """Multiply two numbers."""
#     return a * b

# def divide(a, b):
#     """Divide first number by second."""
#     if b != 0:
#         return a / b
#     else:
#         return "Error: Cannot divide by zero!"

# # Using our functions
# print(f"25°C = {celsius_to_fahrenheit(25)}°F")
# print(f"77°F = {fahrenheit_to_celsius(77):.1f}°C")

# password_strength = check_password_strength("MyPassword123!")
# print(f"Password strength: {password_strength}")

# print(f"5 + 3 = {add(5, 3)}")
# print(f"10 / 2 = {divide(10, 2)}")
# print(f"10 / 0 = {divide(10, 0)}")




# Function Exercises
# Exercise 1: Personal Information Function

def create_profile(name, age, occupation, city):
    """Create a personal profile string."""
    # Your code here
    # Return a formatted string with all the information
    pass

# Test your function
profile = create_profile("Alice", 28, "Engineer", "San Francisco")
print(profile)
# Exercise 2: Grade Calculator Function

def calculate_grade(score):
    """Convert numerical score to letter grade."""
    # Your code here
    # Return appropriate letter grade (A, B, C, D, F)
    # Include + and - modifiers for scores ending in 7-9 and 0-2
    pass

# Test your function
print(calculate_grade(95))  # Should return "A"
print(calculate_grade(87))  # Should return "B+"
print(calculate_grade(83))  # Should return "B-"


# Exercise 3: Shopping Cart Total Function

def calculate_total(price, quantity, tax_rate=0.08):
    """Calculate total cost including tax."""
    # Your code here
    # Calculate subtotal, tax amount, and final total
    # Return the final total
    pass

# Test your function
total = calculate_total(29.99, 3)
print(f"Total cost: ${total:.2f}")


