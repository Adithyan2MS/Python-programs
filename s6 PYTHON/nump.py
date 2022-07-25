from re import X
import numpy as np
from numpy import random
# a=np.array([1,2,3,4,5,6,7,9])
# print(a)
# a_slice=a[3:8]
# print(a_slice)
# a_slice[:]=64
# print(a)
# b=np.arange(50)
# print(b)
# b=np.eye(4,3,1,dtype=np.float32)
# print(b)


# x=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(x[1,2])
# print(x[:2,1:])
# print(x[2:,:])
# print(x[:,:2])
# print(x[1:2,:2])

x=np.array([[1,2,3,4],[5,6,7,8]])
print(x)
y=np.array([[1,2,3,4],[5,6,7,8]])
print(y)

print("///")
print(np.add(x,y))
print(np.subtract(x,y))
print(np.divide(x,y))
print(np.multiply(x,y))
print(np.sqrt(y))
print(np.sum(x,0))
print(np.sum(x,1))
print(x.T)
print(np.multiply(x.T,y.T))
i=random.randint(100,size=(6,5))
print(i)