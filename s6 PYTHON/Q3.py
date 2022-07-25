x=int(input())
y=int(input())
print("(",x,",",y,")",end="")
if x<0 and y<0 :
    print(" belongs to 3rd Quadrant.")
elif x>0 and y>0 :
    print(" belongs to 1st Quadrant.")
elif x<0 and y>0 :
    print(" belongs to 2nd Quadrant.")
elif x > 0 and y < 0:
    print("lies in the Fourth quadrant")
elif x == 0 and y == 0:
    print("lies at the origin")
elif y == 0 and x != 0:
    print("on x-axis")
elif x == 0 and y != 0:
    print(" at y-axis")