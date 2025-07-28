import numpy as np 
import matplotlib.pyplot as plt
data=np.random.binomial(n=0,p=0.3,size=1000)
plt.hist(data,bins=30,color="orange",edgecolor="black")
plt.title("Binomial Distribution")
plt.show()