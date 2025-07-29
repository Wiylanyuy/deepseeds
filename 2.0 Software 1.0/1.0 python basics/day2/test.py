# swaaping variables
a=3
b=6
c=a
a=b
b=c
print(f"swaped numbers : {a} and {b}")


# number guessing game 
import random
number=15
count=0
guess=int(input("Enter a number beteen 1 and 30"))
if guess==number and count<3:
    print(f'{guess} is out of range, try again')
    count +=1
    print(count)
    guess=int(input("Enter a number beteen 1 and 30")) 
elif guess>15 and count<3:
    print(f"{guess} is biger than the number try again,")
    count +=1
    print(count)
    guess=int(input("Enter a number beteen 1 and 30"))
elif guess<15 and count<3:
    print(f"{guess} is smaller than the number, try gain ")
    count +=1
    guess=int(input("Enter a number beteen 1 and 30"))



