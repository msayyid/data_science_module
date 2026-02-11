from scipy import stats
import labpart1

# Scipy = Scientific python library

# mode = the element that appears the most
Mode_of_HP = stats.mode(labpart1.HP_Var)
print(Mode_of_HP)

print(labpart1.hello)