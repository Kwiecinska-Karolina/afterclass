ilość_n = int(input("Podaj liczbę liczb pierwszych: "))
n=2
while n <= ilość_n:
        
    if n % 2 == 0 and n!= 2:
        print(end='')
        
    elif n % 3 == 0 and n!= 3:
        print(end='')
    
    elif n % 5 == 0 and n!= 5:
        print(end='')
        
    elif n % 7 == 0 and n!= 7:
        print(end='')
        
    elif n % 9 == 0 and n!= 9:
        print(end='')
        
    elif n % n == 0 and n % 1 == 0:
        print(n)
    
     
    
    else:
        print(end='')
    n = n + 1