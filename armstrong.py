num=int(input("Enter a three digit number:"))
sum=0
a=num
while num!=0:
    rem=num%10
    sum=sum+(rem*rem*rem)
    num//=10
if a==sum:
    print("Number is armstrong")
else:
    print("Not Armstrong")

