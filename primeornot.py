n=int(input("Enter a number"))
flag=0
for i in range(2,n):
    if (n%i)==0:
        flag=1
        break
if n==1:
    print(" not palindrome")
elif flag==1:
    print("not prime")
else:
    print("prime")
