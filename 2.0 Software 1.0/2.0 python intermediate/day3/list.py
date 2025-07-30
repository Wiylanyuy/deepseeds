# # creating a list 
# shopping_cart=['apple', 'bread', 'milk', 'egg']
# numbers=[1, 3, 4, 5, 6, 7]
# mixed_items= ['Alice', 3, 'apple', True, 3.6]
# empty_list=[]

# print(f"Shopping cart: {shopping_cart}")
# print(f"Numbers: {numbers}")
# print(f"Mixed items: {mixed_items}")

# # Acessing content of a list 
# fruit_list=['apple', 'banana', 'pineapple', 'cherry', 'date']
# print(fruit_list[2])  # prints what is at index 2
# print(fruit_list[0:3])  # print elements from index 0 to 2
# print(fruit_list[1:]) # all elements from index 2
# print(fruit_list[-1])  # the last element in the list


# # modifying list 
# # adding an item to the list
# fruit_list=['apple', 'banana', 'pineapple', 'cherry', 'date']
# fruit_list.append('Mango') # add mango at the end of the list 
# print(f'Current List: {fruit_list}')

# # add multiple items 
# fruit_list.extend(['cheese', 'butter', 'vanila']) 
# print(f'current list after adding: {fruit_list}')
# fruit_list.pop() # removes the last element and return the list 
# print(f'last list: {fruit_list}')

# fruit_list.insert(1, "choco")
# print(fruit_list)
# arr=[2, 5, 4, 6]
# target= input('Enter target')
def calc_average_list(array, target):
    sum_array=0
    lenght_array=0
    for element in array:
        sum_array = sum_array + element
        lenght_array= lenght_array+1
        average_array = sum_array/lenght_array
        print(sum_array)
        
    
    found = False
    for i in array:
        if i==target:
            found=True
            break
    if found==True:
         print("SEEN")
    else:
        print("unseen")
    return  average_array
arr=[2, 5, 4, 6]
target=4
results= calc_average_list(arr, target)



