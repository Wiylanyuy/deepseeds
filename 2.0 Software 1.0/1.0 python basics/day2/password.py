# password= input('\nEnter your password')
# lower_case=password.islower
# upper_case =password.isupper
# numeric=password.isdigit
# if lower_case and upper_case and numeric:
#     print('this is a strong password')
# else:
#     print('Please try agin')
l = False
u = False
d = False
password= input('Enter your password')
for letter in password:
    if letter.islower():
        l=True
    elif letter.isupper():
        u = True
    elif letter.isdigit():
        d= True
if l and u and d:
    print('Strong password')
else:
    print('Week password')        