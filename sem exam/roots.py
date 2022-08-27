import math
print("enter a b and c the coefficients line by line")
a=int(input())
b=int(input())
c=int(input())
if a==0:
        print("Not a quadratic eqtn..root is ", -c/b)
else:
    d=b*b-4*a*c
    
    if d==0:
        print("only one root",-b/(2*a))
    elif d>0:
        print("roots are real")
        print("root1",-b+math.sqrt(d)/(2*a))
        print("root2",-b-math.sqrt(d)/(2*a))
    else:
        print("roots are imaginary")