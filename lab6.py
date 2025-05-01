import numpy as np

def sutun_ceminden_B(A):
    B = np.sum(A, axis=0)
    return B

A = np.array([[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 9]])

B = sutun_ceminden_B(A)
print(B)
