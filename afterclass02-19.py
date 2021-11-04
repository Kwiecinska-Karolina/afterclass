a = int(input("Wprowadź długość pierwszego boku: "))
b = int(input("Wprowadź długość drugiego boku: "))
c = int(input("Wprowadź długość trzeciego boku: "))

p = ( a + b + c) / 2

area = ( p * ( p - a ) * ( p - b ) * ( p - c ) ) ** 1/2 
print(area)