""" Write a program that calculates the sum and arithmetic mean of numbers entered from the keyboard. 
Entering 0 ends entering numbers. 
Sample result:

Enter number: 15 
Enter number: 8 
Enter number: 10 
Enter number: 0 
RESULT: Quantity=3, Sum=33, Mean=11"""
i=0
sum=0
ilość=0
średnia=0
while i>=0:
    number = int(input("Podaj liczbę: "))
    sum = sum + number
    ilość=i
    
    if number == 0:
        średnia=sum/ilość
        print("Ilość: ",ilość,"Suma: ", sum,"Średnia: ", średnia)
    else:
        i= i+1
    
