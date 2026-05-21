import math
import random as rnd
import csv
# age = 19
# height = 175.63473847
# is_student = True
# name = "Tanmay Kangule"

# print(f"I am {name}, {age} Y/O, {height: .2f}cm tall and it is {is_student} that I am a student!!")

#-------------------------------------------------------------------------------
# a = 10
# b = 3.0
# c = "7"
# d = True

# res1 = a + b
# print(res1)

# res2 = a + int(c)
# print(res2)

# print(b > a)

# res3 = str(d) + " is " + str(type(d))
# print(res3)

#-------------------------------------------------------------------------------

#Prac 1
# scores = [23, 44, 50, 19, 36] #List
# coordinates = (124.5, 192.5) #Tuples
# unique_ids = {1, 2, 5, 4, 5} #Set

# #Dict
# student = { 
#     "name": "Tanmay",
#     "age": 19,
#     "grade": "A",
#     "isPassed": True
# }

# scores.append(49)
# print(scores)

# print(set(unique_ids))

# name = student["name"]
# is_passed = student["isPassed"]
# print(f'Name {name} and it is {is_passed} that he has passed the exam')

#Prac 2
# data = [10, 25, 10, 33, 25, 8]

# # (i)
# convert_data_into_set = set(data)
# count = len(convert_data_into_set)
# print(count)

# # (ii)
# convert_data_into_list = list(data)
# convert_data_into_list.sort(reverse=True)
# print(convert_data_into_list)

# #(iii)
# convert_data_into_dict = dict(enumerate(data))
# print(convert_data_into_dict)

#-------------------------------------------------------------------------------

# arr = [10, 20, 30, 40, 50, 60, 70]
# text = "MachineLearning"

# #(i)
# for i in range(0, 3):
#     print(arr[i])

# # (ii)
# for i in range(4, 7):
#     print(arr[i])

# # (iii)
# for i in range(2, 6):
#     print(arr[i])

# # (iv)
# print(text[::2])

# # (v)
# print(text[::-1])

#-------------------------------------------------------------------------------

# (i) For
# for i in range(2, 21, 2):
#     print(i)

# (ii) While
# nums = 20
# while nums >= 20:
#     print(nums[2, 20, 2])

#-------------------------------------------------------------------------------

# score = int(input('Score '))
# if score >= 90:
#     print("Excellent")
# elif 80 <= score <= 89:
#     print("Very Good")
# elif 70 <= score <= 79:
#     print("Good")
# elif 60 <= score <= 69:
#     print("Pass")
# else: 
#     print("Fail") 
 

# a = 10
# b = 12
# c = 15
# max = a

# if(b > a):
#     max = b
# if(c > max):
#     max = c
# print(max)

#-------------------------------------------------------------------------------
# weight = float(input("Weight (kg): "))
# height = float(input("Height (m): "))

# def calculate_bmi(weight, height):
#     bmi = weight / (height ** 2)

#     if bmi < 18.5:
#         print(f"Your BMI is {bmi:.2f} and you are Underweight")
#     elif bmi < 25:
#         print(f"Your BMI is {bmi:.2f} and you are Normal")
#     elif bmi < 30:
#         print(f"Your BMI is {bmi:.2f} and you are Overweight")
#     else:
#         print(f"Your BMI is {bmi:.2f} and you are Obese")

# calculate_bmi(weight, height)

#-------------------------------------------------------------------------------

# root = math.sqrt(25)
# print(root)

# x = 5
# cube = 5 ** 3
# print(cube)

# pi = 3.14159265358979323846264338327950288419716939937
# print(f"{pi:.5f}")

# array = ["red", "blue", "green", "yellow"]

# random_number = rnd.randint(1, 100)
# print(random_number)

# random_float_number = rnd.uniform(0.0, 0.9)
# print(f"{random_float_number:.3f}")

# random_picker = rnd.choice(array)
# print(random_picker)

#-------------------------------------------------------------------------------
