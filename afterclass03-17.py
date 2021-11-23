"""Let x and y denote the coordinates of a point on the plane. 
Write a program that determines in which quadrant of the coordinate system the point P (x, y) 
is located or on which axis it is located, or that it is located in the position (0,0)
of the coordinate system. Sample result:

x = 5 y = 2 Point P(5,2) is in the first quadrant of the coordinate system"""
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
