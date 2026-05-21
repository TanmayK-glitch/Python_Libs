# hello = "Hello World"
# world = "Tim"
# hello = world
# number = 23

# print(hello, world, number)

# ----------------------------------------------------------------

# <<Input>>
# Input always takes the input in String -> use int() to conver it into INT, Float, Etc....
# name = input('Name: ')
# age = input('Age: ')
# print('Hello', name, 'you are', age, 'years old!!')

# ----------------------------------------------------------------

# <<Arithematic Ops>>
# x = 5
# y = 5.5
# result = int(x ** y)
# print(result)

# number1 = input('Number1: ')
# number2 = input('Number2: ')
# result = int(number1) + int(number2)
# print(result)

# ----------------------------------------------------------------

# <<String Methods>>
# Methods 1.upper/lower 2.strip 3.replace("this", "with that") 4.split 5.join 6.startswith/endswith 7. find/in 8. len
# name = 'Tanmay Kangule'
# newName = name.split()
# print(newName)

# ----------------------------------------------------------------

# <<Chained Conditions>>
# 1. and - both conditions must be true (if not then the result will be false)
age = 20
age > 18 and age < 60

#2. or - atleast one condition is true 
age = 16
age < 18 or age > 20

#3. not - reverse the result
# isLoggedIn = False
# isLoggedIn = not isLoggedIn
# print(isLoggedIn)

# username = "Tanmay"
# password = "tanmay@123"
# isBlocked = False
# if(username == "Tanmay" and password == "tanmay@123") and not isBlocked:
#     print('Access Granted!!')
# else:
#     print('Access Denied!!')

# ----------------------------------------------------------------

#If / Elif / Else
# x = input('Name: ')
# if x == "Tanmay":
#     print('You are Cracked Coder!')
# elif x == 'Tim':
#     print('You are wannabe Cracked!')
# else:
#     print('You are Noob in Coding')

# ----------------------------------------------------------------

#<<List / Tuples>>
#List - can store all the types of vars (order does not matter)
# x = ['Hello', 4, True]
# y = 'Hi'
# length = (len(x), len(y))
# print(length)

# Tuple - Similar to Lists (but tuples are mutable) and they use "()" brackets not
# "[]", Also you cannot use any properties on tuples like append or extend etc..
# x = (1, 2, 3, 4, 5)
# result = x[2]
# print(result)

# ----------------------------------------------------------------

#<<For Loop>>
# for i in range(10, -1, -1): #(Start Stop Step)
#     print(i)
x = [1, 2, 3, 4, 5, 6]
# for i in range(len(x)):
#     print(x[i])

# If you want to also print Index with the List use "eumerate"
# for i, element in enumerate(x):
#     print(i, element)

# ----------------------------------------------------------------

# <<Dictionaries>>
person = {
    "name": "Tanmay",
    "age": 20,
    "isCracked": True
}

# access = person["age "]
print(person.values()) #To get values form Dicts <--------

# ----------------------------------------------------------------

# <<Comprehensions>> 
x = [x + 10 for x in range(5)]
print(x)