# contional statement
#  Basic if statement (if else pair)
# age= int(input("What is your age"))
# if age>18:
#     print('Yes you can vote')
# else:
#     print('Pleals wait for next elections')

# # take a persons age and check if they are more than 16, if yes they can play in a basketball team
# Player_age= int(input("What is your age"))
# if Player_age>16:
#     print('You are eligible to play in a basketball team ')
# else:
#     print('Wait untill you are more than 16')


# # IF-ELIF-ELSE CHAIN
# command= input("Enter 'exit' to end program or and 'continue' to keep going ")
# if command=='exit':
#     print('exit cmd')
# elif command=='continue':
#     print('continue enjoying')
# else:
#     print('wrong command')


# school grading system
# score= float(input('Enter your marks'))
# if score>=80:
#     grade='A'
# elif 70<=score<=79:
#     grade='B+'
# elif 60<=score<=69:
#     grade='B'
# elif 55<=score<=59:
#     grade='C+'
# elif 50<=score<=54:
#     grade='C'
# else:
#     grade='F'
#     print(f"Your grade is: {grade}")

# # # leap year calculate ( a year that is divisible by 4 and 400 and not divisible by 100,)
year= int(input("enter the year"))
if year%4==0 and year%400==0 and year%100 ==0:
    print(f'{year} is a leap year')
elif year%4==0 and year%400==0 and year%100!= 0:
    print(f'{year} is a leap year')
elif year%4==0 and year%400!=0 and year%100==0:
    print(f'{year} is not a leap year')
elif year%4!=0 and year%400==0 and year%100==0:
    print(f'{year} is not a leap year')
else:
    print(f'{year} is not a leap year')


# # simple calculator
# # taking input from user
# firt_number = float(input('Enter first number'))
# second_number = float(input('Enter second number'))
# operator = input('Enter operator')
# result=0
# if operator=='+':
#     result= firt_number + second_number
# elif operator=='-':
#     result= firt_number - second_number
# elif operator=='*':
#     result= firt_number * second_number
# elif operator=='/':
#     if second_number!=0:
#         result= firt_number /second_number
#     else:
#         print('division by zero is not alowed')
# else:
#     print('check your operator')
#     print(f'results= {firt_number} {operator} {second_number}')
