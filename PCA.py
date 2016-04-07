import numpy as np
import scipy


def Check_Variance(S):
    Snn = 0
    s = np.shape(S)
    x = int(s[0])
    
    for i in range(x):
        Snn += int(S[i])

    Sk = 0;
    print(Snn)

    for i in range(x):
        Sk += int(S[i])
        print(Sk)
        var =(Sk/Snn)
        if(var > 0.99 ):
            return i+1


def Feature_Normalize(X, m, n):
	st_d=X.std()
	mea_n=X.mean()
	for i in range(m):
		for j in range(n):
			X[i][j] = (X[i][j]-mea_n)/st_d
	return X


X = np.loadtxt('ex7.txt')
dim = np.shape(X)
m = dim[0]
n = dim[1]
print('The Dimensions of Image are %d * %d '% (m , n ))

#Normalizing the Features
X = Feature_Normalize(X, m, n)




X_trans = np.matrix.transpose(X)
sigma = np.dot(X_trans, X)
sigma = np.divide(sigma, m)
print('The Dimensions of sigma are '+ str(np.shape(sigma)))

#Now applying Singular Value Decomposition to find eigen vectors

U, S, V = np.linalg.svd(sigma)
#print(str(np.shape(U))+ ' '+ str(np.shape(S)) +' ' + str(np.shape(V)))

# Find K i.e the Number of principal components
K = Check_Variance(S)
print('The Number of Principal Components Along which data is Project %d' % K)

