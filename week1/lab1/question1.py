import numpy as np 

mpg_data = np.loadtxt("MpG.csv", dtype=float)
print(mpg_data)

print("So this is the mean value of MPG content\nMean Value is the average\n")
print(np.mean(mpg_data))