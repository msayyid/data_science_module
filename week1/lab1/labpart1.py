import numpy as np 

HP_Var = np.loadtxt("HP.csv", dtype=int)
print(HP_Var)

# the mean is the average (sum of each element divided by the number of elements)
Mean_of_HP = np.mean(HP_Var)
print("this is the mean of hp file content")
print(Mean_of_HP)

hello = "hello world"
print(hello)