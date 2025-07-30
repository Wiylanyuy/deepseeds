
# # Unchangeable Data Containers(Tuples)

# # Creating tuples - like sealing important information
# point_coordinates = (10, 20)  # A point in 2D space
# rgb_color = (255, 128, 0)     # Orange color values
# student_record = ("Alice", 20, "Computer Science", 3.8)

# # Tuples can be created without parentheses too
# another_point = 5, 15
# single_item_tuple = (42,)  # Note the comma - this is important!

# print(f"Point coordinates: {point_coordinates}")
# print(f"RGB color: {rgb_color}")
# print(f"Student record: {student_record}")
# print(f"Single item tuple: {single_item_tuple}")


# # Accessing Tuple Elements

# # Working with a tuple representing a book record
# book_info = ("1984", "George Orwell", 1949, "Dystopian Fiction")

# # Accessing individual elements
# title = book_info[0]
# author = book_info[1]
# year = book_info[2]
# genre = book_info[3]

# print(f"Book: {title}")
# print(f"Author: {author}")
# print(f"Published: {year}")
# print(f"Genre: {genre}")

# # Tuple unpacking - a powerful feature
# title, author, year, genre = book_info
# print(f"Using unpacking - Book: {title} by {author} ({year})")

# # Partial unpacking with the rest operator
# first_name, last_name, *other_info = ("John", "Smith", 30, "Engineer", "New York")
# print(f"Name: {first_name} {last_name}")
# print(f"Other info: {other_info}")


# # Tuple Methods and Operations

# # Sample tuple with some repeated values
# grades = (85, 90, 78, 90, 92, 85, 88)

# # Getting information about the tuple
# print(f"Number of grades: {len(grades)}")
# print(f"Highest grade: {max(grades)}")
# print(f"Lowest grade: {min(grades)}")

# # Counting occurrences
# print(f"Number of 90s: {grades.count(90)}")
# print(f"Number of 85s: {grades.count(85)}")

# # Finding the position of an element
# print(f"First occurrence of 90: {grades.index(90)}")

# # Checking if an element exists
# print(f"Is 95 in grades? {95 in grades}")
# print(f"Is 85 in grades? {85 in grades}")

# # Slicing works with tuples too
# print(f"First three grades: {grades[:3]}")
# print(f"Last three grades: {grades[-3:]}")



# # Practical Tuple Examples
# # Representing geographic coordinates
# def get_distance_between_points(point1, point2):
#     """Calculate distance between two points using tuples."""
#     x1, y1 = point1
#     x2, y2 = point2

#     # Using the distance formula
#     distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#     return distance

# # Using coordinate tuples
# home = (0, 0)
# work = (3, 4)
# store = (1, 2)

# print(f"Distance from home to work: {get_distance_between_points(home, work):.2f}")
# print(f"Distance from home to store: {get_distance_between_points(home, store):.2f}")

# # Function that returns multiple values using tuples
# def analyze_text(text):
#     """Analyze text and return statistics as a tuple."""
#     words = text.split()
#     word_count = len(words)
#     char_count = len(text)
#     sentence_count = text.count('.') + text.count('!') + text.count('?')

#     return (word_count, char_count, sentence_count)

# # Using the function
# sample_text = "Python is amazing! It's powerful and easy to learn. Try it today!"
# word_count, char_count, sentence_count = analyze_text(sample_text)

# print(f"Text analysis:")
# print(f"Words: {word_count}")
# print(f"Characters: {char_count}")
# print(f"Sentences: {sentence_count}")

# # Database-like records using tuples
# employee_records = [
#     ("Alice", "Johnson", "Software Engineer", 75000),
#     ("Bob", "Smith", "Data Scientist", 80000),
#     ("Charlie", "Brown", "Product Manager", 85000)
# ]

# print("Employee Directory:")
# for first_name, last_name, position, salary in employee_records:
#     print(f"{first_name} {last_name} - {position} - ${salary:,}")
