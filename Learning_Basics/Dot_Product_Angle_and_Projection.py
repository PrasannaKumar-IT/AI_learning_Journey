import numpy as np

# Cosine of Angle Between Vectors

a=np.array([1,2,3])
b=np.array([4,5,6])
dot=np.dot(a,b)
print("Dot Product: ",dot)

norm_a=np.linalg.norm(a)
norm_b=np.linalg.norm(b)
cos_theta=dot/(norm_a*norm_b)
angle=np.arccos(cos_theta)
degree=np.degrees(angle)
print(f"Angle: {angle}\nDegree: {degree}")

# Projection of Vector a onto Vector b

# 1.Scalar Projection
scalar_projection=np.dot(a,b)/norm_b
print("Scalar Projection: ",scalar_projection)

# 2.Vector Projection 
vector_projection=(np.dot(a,b)/np.dot(b,b))*b
print("Vector Projection: ",vector_projection)