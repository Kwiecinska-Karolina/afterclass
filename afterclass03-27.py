""" A computer numeric keyboard has the arrangement of the keys as below.
The included program code displays the computer keyboard. 
Analyse the program in terms of the displayed results. 
Do you understand each program statement? 
Then make a change in your program code. 
Replace the ‘for’ with a ‘while’ statement.

7 8 9 
4 5 6 
1 2 3

for i in range(6,-1,-3): 
    for j in range(1,4):
        print(f' {i+j}',end='') 
    print()"""
i=7
j=4
x=1
while i<=9:
    print(i, end=" ")
    i = i + 1
print('\r')
while j<=6:
    print(j, end=" ")
    j = j + 1
print('\r')
while x<=3:
    print(x, end=" ")
    x = x + 1
