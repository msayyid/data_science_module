import numpy as np 

mpg_data = np.loadtxt("MpG.csv")
print(mpg_data)

mpg_var = np.var(mpg_data)
print("MPG variance")
print(mpg_var)