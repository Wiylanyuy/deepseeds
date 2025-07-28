# # for loop
# # 1. starting point 
# 2. condition
# 3. increment or decrement 
names =['Will', 'Leo', 'Kate', 'kilian', 'gfhh bom', 'trg mbom', 'muhk mbom']
# print(names[0])
# print(names[1])
# print(names[2])
# # print(names[3])
# prefered solution 
# for name in names:
#     print(name)
#     if name.endswith('mbom'):
#         print(f'we dan catch you {name}')
#     else:
#         print(f'welcome to the party {name}')
# # print name with numbers ast the in the list
# count = 1
# for name in names:
#     print(f'{count}. {name}')
#     count +=1

# # basic for loop with range 
# for numbers in range (2, 10):
#     print(f'count {numbers}')

# # looping through a list
# fruits= ['banana', 'orange', 'apple', 'cherry']
# print("\n i have fruits in my basket") 
# for fruit in fruits:
#     print(f'I have a {fruit}')


# # looping through a string
# word= 'hellopython'




# RANGE FUNCTION (range(top) stars from zero)
# for i in range(10):
#     print(i)
# # range(start, stop)
# for i in range(5, 20):
#     print(i)

# #  count down 
# for i in range(10, 0, -1):
#     print(f'countdown: {i}')
#     print('Blast off!')

# # range(start, stop, step)
# for i in range(0, 20, 2):
#     print(i)

# # WHILE LOOP
# # simple while loop
# count =1
# while count<=5:
#     print(f'count: {count}')
#     count+=1

# # user input loop
# user_input= ""
# while user_input !="quit":
#     user_input= input("Enter 'quit' to exit:")
#     if user_input!='quit':
#         print(f'you entered: {user_input}')
# print('Goodbye')

# LOOP CONTROL STATEMENTS
# break- exit loop completely
# print('finding the first even number: ')
# for number in range(1, 10):
#     if number%2==0:
#         print(f'I have found an even number: {number}')
#         break
#     print(f'{number} is odd')

# # continue . skip to the next itteration 
# print('\n Print only odd numbers')
# for number in range (1, 10):
#     if number%2==0:
#         continue
#     print(f'odd number: {number}')

# NESTED LOOPS(loops inside a loop)
print('Multiplication Table')
for i in range(1, 21):
    for j in range(1, 20):
        result = i * j
        print(f'{i} * {j} = {result}')
    print() 
# pattern printing
print('Triangle patterns')
for row in range(1, 6):
    for star in range(row):
        print('*', end='')
    print()