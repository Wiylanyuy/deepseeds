def style():
    print("_"*50)

def number_error():
    
    try:
        style()
        user_input= int(input("Enter your phone number"))
        print(f"user input is: {user_input}")
    except ValueError:
        print("Please enter a phone number")    
# number_error()

def division_error():
    """ZERO DIVISION ERROR"""
    try:
        style()
        first_number= int(input("Enter first number"))
        second_number= int(input("Enter first number"))
        division=first_number/second_number
        print(f"{first_number}/{second_number} = {division}")
        return division
    except ZeroDivisionError:
        print("Undefine: division by zeror is not surported")
# division_error()

def dictionary_error(data):
    try:
        coln= data["Color"]
        print(f"My Color is: {coln}")
    except KeyError:
    
        print("Key not found")
    
    
data={"name": "Faith", "age": 20, "Favourit_meal": "gari"}
dictionary_error(data)
