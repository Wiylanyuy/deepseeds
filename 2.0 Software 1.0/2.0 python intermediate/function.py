# weight= float (input("enter your age"))
# height= float(input("enter your heigh"))
# bmi= weight/(height*height)
#  function to calculate bmi
# def bmi_calculator():
    # height= float(input("enter your heigh"))
    # weight= float (input("enter your age"))
    # bmi=weight/(height*height)
    # if bmi<18:
    #     print("under weight")
    # elif 18<bmi<25:
    #     print("normal weight")
    # elif 25<bmi<30:
    #     print("over weight")
    # elif bmi>30:
    #     print("You are in trouble")
    # return  bmi  
# def bmi_calculator(height, weight):
#     bmi=weight/(height*height)
#     print(bmi)
    

# height= float(input("enter your heigh"))
# weight= float (input("enter your weight"))
# print(bmi_calculator(height, weight) )

# withouth functions repetivive and error-prone 
# radius1 = 5
# area1 = 3.14159 * radius1 * radius1
# print(f"Area of circle 1: {area1}")

# radius2 = 10
# area2 = 3.14159 * radius2 * radius2
# print(f"Area of circle 2: {area2}")

# radius3 = 7
# area3 = 3.14159 * radius3 * radius3
# print(f"Area of circle 3: {area3}")

# With functions - clean, reusable, and maintainable
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

# Exercise 1: personal information
def create_profile(name, age, occupation, city):
    """Create a personal profile string."""
    # Your code here
    profile= f"My name is {name}, I am {age} years old. \nIam a/an {occupation} and live in {city}. "
    # Return a formatted string with all the information
    return profile 
    pass

# Test your function
profile = create_profile("Alice", 28, "Engineer", "San Francisco")
print(profile)

# excercise 2: grade calclator 

def calculate_grade(score):
    """Convert numerical score to letter grade."""
    # Your code here
    if score>90:
        grade= 'A'
        # print(f"Execelent, your grade is {grade}")
    elif 83<score<=89:
        grade='B+'
        # print(f'Very good, your grade is : {grade}')
    elif score>=60:
        grade='B-'
        # print(f'Very good, your grade is : {grade}')
    elif score>50:
        grade='C'
        # print(f"Average, your grade is : {grade}")
    elif score>35:
        grade='D'
        # print(f"Poor, your grade is : {grade}") 
    else:
        grade='F' 
    # Return appropriate letter grade (A, B, C, D, F)
    return grade
    # Include + and - modifiers for scores ending in 7-9 and 0-2
    pass

# Test your function
print(calculate_grade(95))  # Should return "A"
print(calculate_grade(87))  # Should return "B+"
print(calculate_grade(83))  # Should return "B-"
print(calculate_grade(5))  


# Exercise 3: Shopping Cart Total Function

def calculate_total(price, quantity, tax_rate=0.08):
    """Calculate total cost including tax."""
    # Your code here
    sub_total=price*quantity
    tax= sub_total*tax_rate
    final_total=sub_total + tax
    # Calculate subtotal, tax amount, and final total
    # Return the final total
    return final_total
    pass

# Test your function
total = calculate_total(29.99, 3)
print(f"Total cost: ${total:.2f}")