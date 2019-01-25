import numpy as np

x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
v = np.array([1,0,1])
vv = np.tile(v, (4,1))

print(vv)

y = x + vv
print(y)
