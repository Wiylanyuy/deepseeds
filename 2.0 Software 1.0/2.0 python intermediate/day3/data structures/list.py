# # Creating lists - like filling up your shopping cart
# shopping_cart = ["apples", "bread", "milk", "eggs"]
# numbers = [1, 2, 3, 4, 5]
# mixed_items = ["Alice", 25, True, 3.14]  # Lists can hold different types
# empty_cart = []  # An empty list, ready to be filled

# print(f"Shopping cart: {shopping_cart}")
# print(f"Numbers: {numbers}")
# print(f"Mixed items: {mixed_items}")


fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Accessing items by index (position)
print(f"First fruit: {fruits[0]}")      # apple
print(f"Second fruit: {fruits[1]}")     # banana
print(f"Last fruit: {fruits[-1]}")      # elderberry (negative indexing)
print(f"Second to last: {fruits[-2]}")  # date

# Getting slices (portions) of the list
print(f"First three fruits: {fruits[0:3]}")    # ['apple', 'banana', 'cherry']
print(f"From second to end: {fruits[1:]}")     # ['banana', 'cherry', 'date', 'elderberry']
print(f"Every second fruit: {fruits[::2]}")    # ['apple', 'cherry', 'elderberry']


# Modifying Lists

# Starting with a basic grocery list
groceries = ["milk", "bread", "eggs"]
print(f"Original list: {groceries}")

# Adding single items (like adding items to your cart)
groceries.append("cheese")
print(f"After adding cheese: {groceries}")

# Adding multiple items at once
groceries.extend(["apples", "bananas"])
print(f"After adding fruits: {groceries}")

# Inserting an item at a specific position
groceries.insert(1, "yogurt")  # Insert at index 1
print(f"After inserting yogurt: {groceries}")

# Changing an existing item
groceries[0] = "almond milk"  # Change milk to almond milk
print(f"After changing milk: {groceries}")

# Removing items
groceries.remove("bread")  # Remove by value
print(f"After removing bread: {groceries}")

removed_item = groceries.pop()  # Remove and return last item
print(f"Removed item: {removed_item}")
print(f"After popping: {groceries}")

specific_item = groceries.pop(1)  # Remove and return item at index 1
print(f"Removed item at index 1: {specific_item}")
print(f"Final list: {groceries}")

# List Methods and Operations

# Sample list of test scores
test_scores = [85, 92, 78, 96, 88, 79, 94]

# Getting information about the list
print(f"Number of scores: {len(test_scores)}")
print(f"Highest score: {max(test_scores)}")
print(f"Lowest score: {min(test_scores)}")
print(f"Average score: {sum(test_scores) / len(test_scores):.1f}")

# Checking if items exist
print(f"Is 85 in the list? {85 in test_scores}")
print(f"Is 100 in the list? {100 in test_scores}")

# Counting occurrences
grades = ["A", "B", "A", "C", "B", "A", "D"]
print(f"Number of A's: {grades.count('A')}")

# Finding the position of an item
print(f"Position of first 'B': {grades.index('B')}")

# Sorting (this changes the original list)
test_scores.sort()
print(f"Sorted scores: {test_scores}")

# Sorting in descending order
test_scores.sort(reverse=True)
print(f"Scores (highest to lowest): {test_scores}")

# Reversing the list
test_scores.reverse()
print(f"Reversed list: {test_scores}")


#  Lists in Loops

# List of students
students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

# Simple iteration
print("Class roster:")
for student in students:
    print(f"- {student}")

# Iteration with index numbers
print("\nNumbered class roster:")
for i, student in enumerate(students):
    print(f"{i + 1}. {student}")

# Processing each item
prices = [19.99, 25.50, 12.75, 33.20, 8.99]
print("\nPrice list with tax:")
for price in prices:
    price_with_tax = price * 1.08
    print(f"${price:.2f} -> ${price_with_tax:.2f}")

# Creating new lists based on existing ones
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(f"Even numbers: {even_numbers}")

# List comprehension - a compact way to create lists
squares = [x**2 for x in range(1, 11)]
print(f"Squares: {squares}")

even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")


# List examples
# Todo list manager
todo_list = []

def add_task(task):
    """Add a task to the todo list."""
    todo_list.append(task)
    print(f"Added: '{task}'")

def complete_task(task):
    """Mark a task as completed by removing it."""
    if task in todo_list:
        todo_list.remove(task)
        print(f"Completed: '{task}'")
    else:
        print(f"Task '{task}' not found in the list")

def show_tasks():
    """Display all pending tasks."""
    if todo_list:
        print("Your tasks:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks pending. Great job!")

# Using the todo list
add_task("Buy groceries")
add_task("Write Python code")
add_task("Call mom")
show_tasks()

complete_task("Buy groceries")
show_tasks()

# Grade tracker
def calculate_class_statistics(grades):
    """Calculate statistics for a class."""
    if not grades:
        return "No grades to analyze"

    total = sum(grades)
    count = len(grades)
    average = total / count

    # Count letter grades
    letter_grades = []
    for grade in grades:
        if grade >= 90:
            letter_grades.append("A")
        elif grade >= 80:
            letter_grades.append("B")
        elif grade >= 70:
            letter_grades.append("C")
        elif grade >= 60:
            letter_grades.append("D")
        else:
            letter_grades.append("F")

    return {
        "average": average,
        "highest": max(grades),
        "lowest": min(grades),
        "total_students": count,
        "letter_grades": letter_grades
    }

# Example usage
class_grades = [85, 92, 78, 96, 88, 79, 94, 87, 91, 83]
stats = calculate_class_statistics(class_grades)
print(f"Class average: {stats['average']:.1f}")
print(f"Grade range: {stats['lowest']} - {stats['highest']}")
print(f"Letter grades: {stats['letter_grades']}")


# List Exercises

# Favorite Movies Manager
favorite_movies = []

def add_movie(movie):
    """Add a movie to the favorites list."""
    # Your code here
    pass

def remove_movie(movie):
    """Remove a movie from favorites."""
    # Your code here
    pass

def show_movies():
    """Display all favorite movies."""
    # Your code here
    pass

# Test your functions
add_movie("The Matrix")
add_movie("Inception")
add_movie("Pulp Fiction")
show_movies()
remove_movie("Inception")
show_movies()

# Number Analyzer
def analyze_numbers(numbers):
    """Analyze a list of numbers and return statistics."""
    # Your code here
    # Return a dictionary with: sum, average, min, max, even_count, odd_count
    pass

# Test your function
test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = analyze_numbers(test_numbers)
print(result)