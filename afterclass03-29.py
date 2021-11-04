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
    
