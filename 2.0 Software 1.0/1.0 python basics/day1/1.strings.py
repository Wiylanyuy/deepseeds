# # conctenation and interpulation
# name = "Blaise"
# last_name = "Linyuy"
# full_nam = name + last_name
# # interpulation
# print(f"my full name is:{full_nam}")
# # multipliction
# laugh = 'Ha'*7
# print(laugh)
# message='Hello, Python'
# print(len(message))
# # message[2]
# # f string method (recommended - like fill in the blanks)
# name= 'Alice'
# age = 30
# score = 95.5
# print(f'Hello {name }! You are {age} years old.')
# print(f'Your score is {score:.1f}%')
# # method 2 format() method 
# print('Hello {}! You are {} years old.'.format(name, age))
# # method 3, % formating(older style)
# print('Hello %s! You are %d years old.'%(name, age))

# EXAMPLE 2
# email validator
# email = 'user@email.com'
# if '@' in email and '.' in email:
#     username= email.split('@')[0]
#     domain= email.split('@')[1]
#     print(f'username: {username}')
#     print(f'domain: {domain}')
# else:
#     print('Invalid email format')
# # text analyzer
# text = 'The quick brown fox jumps over the lazy dog'
# print(f'Text: {text}')
# print(f'Lenght: {len(text)} characters')
# print(f'Words: {len(text).split()} words')
# print(f'Uppercase: {text.upper()}')
# print(f'Title case: {text.title()}')
# print(f'Contains "fox": {"fox" in text}')
#  nam formating
full_name = "jOhN dOe"
# make John Doe
j=full_name[0].upper()
o=full_name[1].lower()
n=full_name[3].lower()
d=full_name[5].upper()
print()
full_name = "J" + full_name[:1]

# print first_name and last_name