"""The variables a and b contain the dimensions of the sides of the rectangle.
Write a program that creates the following rectangle with dimensions a and b. 
Example result for a = 4 and b = 15:

***************
*             * 
*             * 
***************
"""
a = 4
b = 15
i = 0
j = 0
for i in range(0,a):
    for j in range(0,b):
        if i == 0 or j == 0 or i == a-1 or j == b-1:
            print("*", end='')
        else:
            print(" ", end='')
    print("\r")
 








           
