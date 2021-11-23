"""Write a program that displays two numbers entered from the keyboard in ascending order.

Enter first number: 27 Enter second number: 14 Numbers in ascending order: 14, 27"""
number_1 = input("Podaj pierwszą liczbę: ")
number_2 = input("Podaj drugą liczbę: ")

if number_1 <= number_2:
    print (number_1 + ", " + number_2)
elif number_1 >= number_2:
    print(number_2 + ", " + number_1)
