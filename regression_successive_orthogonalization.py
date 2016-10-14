import numpy as np
#def regression_successive_orthogonalization(X, Y):

X = np.array(np.mat([[1, 2, 3, 4], [3, 4, 4, 5], [4, 5, 7, 6]]))
Y = np.array(np.mat([[30, 32, 23, 14], [53, 24, 34, 45], [34, 15, 37, 46]]))
X_T = X.transpose()
X_T = T.transpose()
shape = np.shape(X_T)
p = shape[0]
m = shape[1]

print('matrix X: ')
print(X)

# Initialize x_0 and z_0 with 0's elements which is the vector 1.
x_0 = np.ones((1, m), dtype=int)
z_0 = np.ones((1, m), dtype=int) #z_0 = np.array(np.full((1, shape[1]), 1, dtype=int))
X_T = np.insert(x_0, 1, X_T, 0)

Z = np.empty([p,m], dtype=int)
Z = np.insert(z_0, 1, Z, 0)
print('Z: ')
print(Z)

shape = np.shape(X_T)
p = shape[0]

print('matrix X_T: ')
print(X_T)
#print('shape: ', shape);
#print('dimension: ', p)
#print('num_elements: ',m)

Q = [[0 for i in range(p)] for j in range(p-1)]
print('Coefficient: ', Q)
for j in range(p):
    for l in range(p-1):
        print(j)
        print(X_T[j])
        Q[l][j] = np.inner(Z[l], X_T[j]) / np.inner(Z[l], Z[l])
        Z[j] = X_T[j] - Q[l][j]*Z[l].sum()
        print('Q: ', Q)
        print('Z: ', Z[j])

estimate_beta = list()
for i in range(p):
    estimate_beta[i] = np.inner(Z[i], Y_T[i]) / np.inner(Z[i], Z[i])

#print(estimate_beta)
