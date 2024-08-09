import numpy as np  
arr = [[2, 2, 2, 2, 2], 
	[15, 6, 27, 8, 2], 
	[23, 2, 54, 1, 2, ], 
	[11, 44, 34, 7, 2]]  
print("\nvar of arr, axis = None : ", np.var(arr)) 
print("\nvar of arr, axis = 0 : ", np.var(arr, axis = 0)) 
print("\nvar of arr, axis = 1 : ", np.var(arr, axis = 1)) 

