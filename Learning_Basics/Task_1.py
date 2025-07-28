import numpy as np
Scalar=7
v=np.array([4,-1,2])
A=np.array([[1,2,3],[4,5,6]])

print("Scalar:", Scalar)
print("Vector:", v)
print("Matrix A:\n", A)

v_norm=np.linalg.norm(v)
print("Norm of vector:",v_norm)
u=np.array([1,0,-1])
vector_add=v+u
vector_prod=np.dot(v,u)
print("Addition:",vector_add)
print("Dot Product: ",vector_prod)

print("Transpose of A: ",A.T)
B=np.array([[7,8],[9,10],[11,12]])
matrix_mul=A@B
print("Multiplication of matrix:",matrix_mul)


X=np.array([[1,2],[3,4],[5,6]])
w=np.array([0.5,1.0])
y=np.dot(X,w)
print("y=",y)