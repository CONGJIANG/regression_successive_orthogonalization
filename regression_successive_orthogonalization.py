import numpy as np
#def regression_successive_orthogonalization(X):

X = np.array(np.mat([[1, 2, 3, 4], [3, 4, 4, 5], [4, 5, 7, 6]]))
X_T = X.transpose(); shape = np.shape(X_T); p = shape[0]; m = shape[1]

#print('shape: ', shape); print('vector_01: ', X[0,:])

print('matrix X: ')
print(X)

# Initialize x_0 and z_0 with 0's elements which is the vector 1.
x_0 = np.ones((1, m), dtype=int)
z_0 = np.ones((1, m), dtype=int) #z_0 = np.array(np.full((1, shape[1]), 1, dtype=int))


X_T = np.insert(x_0, 1, X_T, 0)

print('matrix X_T: ')
print(X_T)
print('dimension: ',p)
print('num_elements: ',m)

for x in X_T:
    print(x)


#for i in range(p):
#    if i == 0:
#        Z = np.array(np.full((1, shape[1]), 1, dtype=int))
        #Z = np.ones(i, shape[1])
        #x[i] = np.full((1, shape[1]), 1, dtype=int)
        #print(z[i])
        #print(x[i])
#        print('hello everyone.', Z)
    #else:
        #x[i] =


#    x[i] = X[i,:]
#    print(x[i])


#z_0 = np.array([p]) #x_0 = np.array([p]) #z_0.fill(1) #x_0.fill(1)

#for i in range(1, p+1):
    #np.inner(a, b)
#    print(i)
    #vector[i] = a[i, :]

#    return X
