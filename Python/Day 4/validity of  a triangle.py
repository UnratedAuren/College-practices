a = int( input("Enter side1 ="))
b = int( input("Enter side2 ="))
c = int( input("Enter side3 ="))

if a+b>c and a+c>b and b+c>a:
    print("It's a triangle.")
else:
    print("Not a triangle.")