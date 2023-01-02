# Check how much memory we have before creating a large matrix

import psutil
import numpy as np

memory = psutil.virtual_memory()
available_memory = memory.available
print(f'Available memory: {available_memory / (1024 ** 3)} GB')

# next we see how much memory will be required to create our N x N matrix using numpy

n = 5000
matrix = np.zeros((n, n))
size_in_bytes = matrix.nbytes
print(f'Size of matrix: {size_in_bytes / (1024 ** 2)} MB')

# now let's create the matrix

matrix = np.random.randint(1,4, size=(n, n))

print(matrix)

np.savetxt('matrix.csv', matrix, delimiter=',')
