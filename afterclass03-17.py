x = int(input("Podaj x: "))
y = int(input("Podaj y: "))

if x>0 and y>0:
    print("Punkt P(",x,",",y,") znajduje się w 1 ćwiartce")
elif x<0 and y>0:
    print("Punkt P(",x,",",y,") znajduje się w 2 ćwiartce")
elif x>0 and y<0:
    print("Punkt P(",x,",",y,") znajduje się w 4 ćwiartce")
elif x<0 and y<0:
    print("Punkt P(",x,",",y,") znajduje się w 3 ćwiartce")
elif x==0 and y<0:
    print("Punkt P(",x,",",y,") znajduje się na osi Y")
elif x==0 and y>0:
    print("Punkt P(",x,",",y,") znajduje się na osi Y")
elif x>0 and y==0:
    print("Punkt P(",x,",",y,") znajduje się na osi X")
elif x<0 and y==0:
    print("Punkt P(",x,",",y,") znajduje się na osi X")
else:
    print("Punkt P(",x,",",y,") znajduje się w pozycji (0,0) układu współrzędnych")