import numpy as np
from numpy import *
n=int(input("Enter The number of rows: "))
g=np.zeros((n,n))

for i in range(n):
    for j in range(i+1):
        if i==j:
            g[i][j]=1
        if j==0:
            g[i][j]=1
        else:
            g[i][j]=g[i-1][j-1]+g[i-1][j]

for i in range(n):
        for j in range(i+1):
          print(g[i][j],'  ',end='')
        print()