sum=0
print("enter the numbe of numbersN")
N=int(input())
print("enter the numbers:")
for i in range(N):
    num=int(input())
    if num%2==0:
        sum=sum+num
print(sum)