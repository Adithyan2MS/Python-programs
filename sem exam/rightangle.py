a=int(input("enter side a..:"))
b=int(input("enter side b..:"))
c=int(input("enter side c..:"))
if a+b>c and a+c>b and b+c>a:
    if a**2+b**2==c**2:
        print("Right angled triangle")
    else:
        print("Not a right angled triangle")
else:
    print("given sides does not form a triangle")