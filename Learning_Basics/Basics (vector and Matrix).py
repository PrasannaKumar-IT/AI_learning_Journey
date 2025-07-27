# Scalar defines a single number
n=5
print(type(n))

# vector defines the single set of values like list ( 1D Array ) used to represent image pixels and key values

import numpy as np
a=np.array([1,2,3,4])
print(type(a))
b=np.array([5,6,7,8])
print(a+b) # matrix addition
print(np.dot(a,b)) # Dot product

# matrix defines the 2 dimension values 
c=np.array([[1,2],[4,5]])
d=np.array([[8,7],[5,4]])
print(c)
print(c.T) # matrix Transpose used to represent datasets 
print(np.dot(c,d)) # matrix multiplication

# norms means magnitude of the vector ‖v‖ = √(x₁² + x₂² + ... + xₙ²)

print(np.linalg.norm(a)) # magnitude of the variable 'a'

# unit vector means divide each element by its norm (magnitude)

unit_a=a/np.linalg.norm(a) 
print(unit_a) # unit vector of the variable 'a'

# Distance between vectors : Euclidean Distance( Straight line between two points ) which is basically used in KNN,clustering Algorithms
a=np.array([1,2])
b=np.array([3,4])
distance=np.linalg.norm(a-b)
print(distance) # Euclidean Distance between point 'a' and 'b'


# Identity  Matrix
I=np.identity(2)
print(I)

# Inverse Matrix 
a=np.array([[1,2],[3,4]])
a_inverse=np.linalg.inv(a)
print(a_inverse)