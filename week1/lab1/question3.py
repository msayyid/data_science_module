from scipy import stats
import numpy as np

ctype_data = np.loadtxt("CType.csv")
print(ctype_data)



mode_of_ctype = stats.mode(ctype_data)
print(mode_of_ctype)


print("--------------------------------------------")

hp_var = np.loadtxt("HP.csv")
print(hp_var)
variance_of_hp = np.var(hp_var)
# Variance = how spread out your data is around the mean
print("Variance of hp csv file")
print(variance_of_hp)
