# # functions are the reusable code and more readability
# # there are mainly two types of functions: 1. Built in functions 2. User define functions

# def add(a,b):
#     #print(a+b) 
#     return a + b

# # function calling
# result = add(5, 6)
# print(result)

# # create user define function like subtract multiply add and divide

# def sub(a,b):
#     return a - b
# def div(a,b):
#     if b == 0:
#         return "cannont divide"
#     return a/b
# def mult(a,b):
#     return a * b

# result = sub(7, 3)
# result = div(6, 3)
# result = mult(7, 3)

# print(result)
    

# classwork
# def find_max(a,b,c):
#     if(a>b) and (a>c):
#         return a
#     elif(b>a) and (b>c):
#         return b
#     elif(c>a) and (c>a):
#         return c
    
# result = find_max(5,6,7)
# print(result)
    
# **kwargs -- arbitary argument

# class work using arbitary arguments
# check the existence  of particular key in a dictionary

# def check_key(key,**kwargs):
#     print(key)
#     chcek = kwargs.get(key)
#     if check:
#         return 'key exist'
#     elese:
#         return 'key doesnot exist'

# print(check_key('value',name="nepal",age=20))


#find the sum of all the values in a dictionary
# kwargs = {'a': 1, 'b': 2, 'c':3}

# def sum_number(**kwargs):
#     total = 0
    
#     for value in kwargs.values():
#         total += value

#     return total

# result = sum_number(a=15,b=25,c=90,d=30)
# print(result)
    
# nested function

# for i in range(5):      #range is stargted from 0
#     for j in range(5):
#         print(i+j)

#classwork nested for loop
#find the sum of all the value in nested for loop
# total = 0
# for i in range(5):
#     for j in range(5):
#         total += i+j
#         print(total)
#nested function to greet
# def greet(name):
#     def get_message():
#         print(f"Hello {name}")
#     return get_message()   # no argument

# result = greet('Nepal')
# print(result)

#state rentention counter example

# def parent_counter():
#     count = 0
#     def child_counter():

#         count += 1

#classwork for nested function
#find the max from a list of parent scope and pop the max value from the list until the list is empty


# def max_value():
#     nums = [1,2,3,4,5]
#     def remove_func():
#         nonlocal nums
#         m = max(nums)
#         nums.remove(m)
#         print(nums)
#         return m

#     return remove_func
# result = max_value()
# for i in range(5):
#     print(result())

# def max_value():
#     nums = [1,2,3,4,5]
#     def remove_func():
#         nonlocal nums
#         m = max(nums)
#         nums.remove(m)
#         # print(nums)
#         return m,nums

#     return remove_func
# result = max_value()
# val_max,array = result()
# print(val_max,array)

# while len(array) > 0:
#     val_max,array = result()
#     print(val_max,array)

#create discount_parent function with nested child function of apply_discount and set_discount and set_discount

# def discount_parent():
#     current_discount = 0.1

#     def apply_discount(price):
#         nonlocal current_discount
#         return price - (price * current_discount)       # return price * (1 - current_discount)

#     def set_discount(discount_rate):
#         nonlocal current_discount
#         current_discount = discount_rate

#     return apply_discount, set_discount
# apply_discount, set_discount = discount_parent()
# print(apply_discount(1000))
# set_discount(0.2)
# print(apply_discount(1000))

#recursive function
#sum of natural numbers using recursive function

# def natural_num(n):
#     if n == 1:
#         return 1
#     else:
#         return n + natural_num(n-1)
# num = int(input("Enter a natural number: "))
# print("Natural number = ", natural_num(num))

#factorial of a number using recursive function
# def fact(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * fact(n-1)
# num = int(input("Enter a number: "))
# print("Factorial of a given number is: ", fact(num))

#flatten the list using the recursive function
# example_list = [1,2,[3,4,[5,6],7],8,9,[10]]
# result_list = []

# def flatten_list(l):
#     for i in l:
#         if isinstance(i,list):
#             flatten_list(i)
#         else:
#             result_list.append(i)
#     return result_list
# print(flatten_list(example_list))
    

#flatten the list with maximum numnber no built in function using the recursive function
# example_list = [1,2,[3,4,[5,25],7],8,9,[10]]
# result_list = []

# def flatten_list(l):
#     for i in l:
#         if isinstance(i,list):
#             flatten_list(i)
#         else:
#             result_list.append(i)

#     return result_list
# flat_list = flatten_list(example_list)

# max_num = flat_list[0]

# for num in flat_list:
#     if num > max_num:
#         max_num = num
# print("Flatten Number: ", flat_list)
# print("Maximum number: ", max_num)

#Higher order function
#example
# def parent_function(func):
#     print(func)
#     def child_fumction():
#         print("My name is ")
#         func()
#         print("I am from Nepal ")
#     return child_fumction
# @parent_function                #Decorator 
# def name():
#     print("Ram")

# name()
# print(name())               #None

# def divider_function(func_add):
#     print(func_add)
#     def child_fumction(a, b):
#         if b == 0:
#             return "Cannont divide by zero"
#         return func_add(a, b)
#     return child_fumction

# @divider_function                #Decorator 
# def divide(a, b):
#     return a / b

# print(divide(10,5))
# print(divide(6,0))

#classwork for higher oreder function
#create a function that can validate the age of a person
#if the age is less than 18 return "You are not eligible for voting"
#if the age is greater than 18 return "You are eligible for voting"

# def age_validate(age_func):
#     print(age_func)
#     def child_fuc(age):
#         if age < 18:
#             return "You are not eligible for voting. "
#         else:
#             return age_func(age)
#     return child_fuc

# @age_validate                                       #Decorator
# def vot_age(age):
#     return "You are eligible for voting. "
# print(vot_age(40))

#create arithmetic operation function like add, sub, multiply and divide
#create a hihger function that takes two numbers and an operator and return the result

# def add_ope(a,b):
#     return a+b
# def sub_ope(a,b):
#     return a-b
# def mul_ope(a,b):
#     return a*b
# def div_ope(a,b):
#     return a/b

# def calc(a,b,operator_address):             #higher order function
#     return operator_address(a,b)            #function call

# print(calc(10,6,add_ope))
# print(calc(10,6,sub_ope))
# print(calc(10,6,mul_ope))
# print(calc(10,6,div_ope))

#create a user with username, password and role dict data type
#create a function to check if the user is admin or not

# def is_admin(func):
#     def child_function_admin(user):
#         if not user.get('role'):
#             return 'role must be provider'
#         if user.get('role') != 'admin':
#             return 'you are not authorized to access. '
#         return func(user)
#     return child_function_admin

# @is_admin
# def delete_database(user):
#     print(f'you are authorized {user.get('username')}. you can delete. ')
#     return 'database deleted. '

# user = {
#     'username' : 'admin',
#     'password' : 'password',
#     'role' : 'admin'
# }

# print(delete_database(user))

# user = {
#     'username' : 'Ram',
#     'password' : '123@ram',
#     'role' : 'admin'
# }
# def is_migratedata(func):
#     def child_function_admin(user):
#         data_list = [
#             {'username':'Ram','password':'123@ram','role':'admin'},
#             {'username':'Shyam','password':'12345@shyam','role':'BM'},
#             {'username':'Hari','password':'123@hari','role':'HR'},
#             {'username':'Sita','password':'123@Sita','role':'Staff'}
#         ]
#         for user_data in data_list:
#             if user.get('username') == user_data.get('username') and user.get('password') == user_data.get('password'):
#                 if user.get('role') == 'admin':
#                     return func(user) 
#                 else:
#                     return 'You are not authorized to migrate the data. '
#         return 'Invallid username and password. '
#     return child_function_admin

# @is_migratedata
# def migrate_database(user):
#     print(f"you are authorized {user.get('username')}. you can migrate. ")
#     return 'database migrated. '

# print(migrate_database(user))

                                #####closure decorator function #####

#lamda function
#syntax = lamda arguments: expression
#lambda can only use for one single line function

# result = lambda x,y: x+y
# print(type(result))
# print(result)
# print(result(10,20))

#find the square of a number using lambda function

# square = lambda x: x*x
# print(type(square))
# print("Square of a number= ", square(10))

# #find the cube of a number using lambda function

# cube = lambda x: x*x*x
# print(type(cube))
# print("Cube of a number = ", cube(10))

#find the sum of all the numbers in a list using lambda function

# list_data = [2,4,5,7,8]


#check if the number is even or odd

# even_odd = lambda x: 'even' if x%2 == 0 else 'odd'
# print(even_odd(10))

# #Greater number finding in two numbers

# greater_num = lambda a,b: a if a>b else b
# print(greater_num(10, 20))


#find the greatest number using 3 numbers
# greater_num = lambda a,b,c: a if (a > b and a > c)  else (b if (b > a and b > c) else c)
# greater_num = lambda a,b,c: a if (a > b) and (a > c)  else b if (b > a) and (b > c) else c

# print(greater_num(100, 20, 30))

#built in higher order function in python
#1. map function
#map function is used to apply a function to all the elements of an iterables
#syntax
#map(function,iterable)
#return type of map is map object
#we can convert it into list using list()

# listing = [1,2,3,4,5]
# map_object = map(lambda x: x*x*x, listing)
# print(map_object)
# result_list = list(map_object)
# print(result_list)

#map of all the string elements in list to their respective lenght

# listing_element = ['Ram','Shyam','Gopal','Sita']
# map_element = map(lambda x: len(x), listing_element)
# print(map_element)
# result = list(map_element)
# print(result)

#map function to convert the temperature in degree celsius to fahreinheit  --> (c = (celsius * 9/5) + 32)

# celsius = [34,67,89,50]
# map_ele = map(lambda c: ((c*9/5)+32), celsius)
# result = list(map_ele)
# print(result)

# filter function















