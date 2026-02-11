import numpy as np 

hp_data = np.loadtxt("HP.csv")

print(hp_data)

# np.std = standard deviation - typically how much does a value from the average

s_deviation_of_hp = np.std(hp_data)
print("Standard deviation for the hp_data file")
print(s_deviation_of_hp)