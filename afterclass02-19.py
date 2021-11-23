""" The length of the sides of the triangle is a, b and c.
Write a program that calculates the area of the triangle using the Heron formula. 
Read the values of the sides of the triangle from the keyboard. 
Using the program, calculate the area of the triangle for the sides 3, 4 and 5.
"""
a = int(input("Wprowadź długość pierwszego boku: "))
b = int(input("Wprowadź długość drugiego boku: "))
c = int(input("Wprowadź długość trzeciego boku: "))

p = ( a + b + c) / 2

area = ( p * ( p - a ) * ( p - b ) * ( p - c ) ) ** 1/2 
print(area)
