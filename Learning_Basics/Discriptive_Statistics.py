import numpy as np

# Mean represent the average( center point of a dataset ) of vectors Mean = (x1 + x2 + ... + xn) / n used in linear regression,k-means,normalization,loss function calculation
a=np.array([2,4,6,8,10])
print(np.mean(a))

# median represent the middle value when the dataset is sorted used for data preprocessing esspacilly for missing value implantaion
b=np.array([20,10,50,30,40])
print(np.median(b))

# mode represent most common value in a dataset
from scipy import stats
c=np.array([1,2,3,4,3,2,3,3,1])
mode_c=stats.mode(c,keepdims=True)
print(mode_c)

# variance means how far the value is spread out from mean Variance = sum((x - mean)²) / n used in detect the outliers

print(np.var(c))

# standard deviation means square root of variance Std Dev = √Variance used in detect the outliers

print(np.std(c))
