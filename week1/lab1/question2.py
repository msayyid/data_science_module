import question1
import numpy as np 

print(question1.mpg_data)

# median is the middle number when the array is sorted, if even, average of the two number
print("here is the median of the content of the mpg:")
print(np.median(question1.mpg_data))