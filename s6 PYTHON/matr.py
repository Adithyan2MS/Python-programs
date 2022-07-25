

# Program to add two matrices using nested loop
 
X = [[1,2,89],
    [76 ,9,6],
    [7 ,90,9]]
 
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]
 
 
result = [[0,0,0],
        [0,0,0],
        [0,0,0]]
 
# iterate through rows
for i in range(len(X)):  
# iterate through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
 
for r in result:
    print(r)

 
# This function stores
# transpose of A[][] in B[][]
 
def transpose(A,B):
 
 for i in range(3):
  for j in range(3):
   B[i][j] = result[j][i]

 
 
B = result[:][:] # To store result
 
transpose(result, B)
 
print("Result matrix is")
for k in B:
    print(k)