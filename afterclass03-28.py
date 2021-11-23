"""Write a program that displays the first fifty words of the Fibonacci sequence.
The sequence is defined as follows: 
the first term is equal to 0, the second is equal to 1, each subsequent term is the sum of the previous two.
Sample result below.

0 1 1 2 3 5 8 13 21 34 ... """
def fib (n):
    a=0
    b=1
    
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        
        for i in range(2, n):
            c= a + b
            a = b
            b = c
            print(c)
    
fib(12)
