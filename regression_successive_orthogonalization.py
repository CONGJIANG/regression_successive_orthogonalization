import numpy as np
#def regression_successive_orthogonalization(X):
#a = np.matrix('1 2; 3 4')
X = np.array(np.mat([[1, 2, 3], [3, 4, 4], [4, 5, 7]]))
shape = np.shape(X)
p = shape[0]
#x = np.array(p+1)
#for i in range(1,p+1):
#    x[i] = X[i,:]
#    print(x[i])
print('shape: ', shape)
print('matrix: ', X)
print('vector_01: ', X[0,:])
print('dimension: ',p)

#z_0 = np.array([p])
#x_0 = np.array([p])
#z_0.fill(1)
#x_0.fill(1)
z_0 = np.full((1, p), 1, dtype=int)
x_0 = np.full((1, p), 1, dtype=int)
print('z_0: ', z_0)
print('x_0: ', x_0)
#vector = []
for i in range(1, p+1):
    #np.inner(a, b)
    print(i)
    #vector[i] = a[i, :]

#    return X
