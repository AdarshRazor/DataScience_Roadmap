'''
Operations
There are a number of basic operations that can be applied to modify matrices:

Addition
Scalar Multiplication
Transposition
Multiplication
'''

a = [[1,2,3],[4,5,6]]
b = [[7,8,9],[10,11,12]]

addition = [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a)) ]
print("Addition of the matrix:",addition)


multiplication = [[a[i][j] * b[i][j] for j in range(len(a[0]))] for i in range(len(a)) ]
print("\nMultiplication of the matrix:",multiplication)