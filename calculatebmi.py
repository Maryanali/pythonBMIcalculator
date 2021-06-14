#!/usr/bin/env python3
#subscripting
print("Hello"[4])
#concatnation
print("Hello" + "world")
#calculation 
print(123 + 345)

#received an error when concatnating string with integer, type function will give the the type of data that you are using.

#type casting (conversion)
#1 exercise
num_char = len(input("What is your name? "))
new_num_char =str(num_char)
print("Your name has " + new_num_char + " characters.")


#2 exercise
#converting to int
two_digit_number = input("Type a two digit number ")

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

result = int(first_digit) + int(second_digit)
print(result)



#BMI calculator 
weight= input("Input your weight in kg: ")
height= input("Input your height please in m: ")
bmi= int(weight)/ float(height) ** 2
print(round(bmi, 2))