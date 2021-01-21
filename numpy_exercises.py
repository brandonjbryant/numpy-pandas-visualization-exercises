import numpy as np 
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

#1.How many negative numbers are there?()
len(a[a < 0])

#2.How many positive numbers are there?
len(a[a > 0])

#3.How many even positive numbers are there?
len(a[(a > 0) & (a % 2 == 0)])