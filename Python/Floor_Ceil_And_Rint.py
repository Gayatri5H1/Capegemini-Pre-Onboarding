import numpy as np 
a = np.array(input().split(), float)
np.set_printoptions(sign=' ')
print(np.floor(a))
print(np.ceil(a))
print(np.rint(a))
