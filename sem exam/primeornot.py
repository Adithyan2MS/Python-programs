n=13
i=2
prime=True
while i<=n//2:
    if n%i==0:
        prime=False
        break
    i=i+1
if prime==True:
    print("prime")
else:
    print("not prime")