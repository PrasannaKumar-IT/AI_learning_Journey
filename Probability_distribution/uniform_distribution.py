import numpy as np 
import matplotlib.pyplot as plt
data=np.random.uniform(low=0,high=10,size=1000)
data.sort()
plt.hist(data,bins=30,color="orange",edgecolor="black")
plt.title("Uniform Distribution")
plt.show()