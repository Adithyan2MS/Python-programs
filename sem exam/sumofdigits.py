num=int(input("entr a number:"))
sum=0
while num!=0:
    t=num%10
    sum=sum+t
    num=num//10
print("sum ",sum)