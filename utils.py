import numpy as np

def max_norm(A):
    '''
    Useful function for Calculate Vector L_max_norm
    '''
    return np.max(np.abs(A))

def diag_inverse(A):
    '''
    Useful function for diag matrix inverse matrix
    '''
    M, N = A.shape
    for i in range(min(M,N)):
        A[i][i] = 1/A[i][i]
    return A

def LU_decomposition(A):
    '''
    Useful function for LU decomposition
    U matrix:
        u_{ij} = a_{ij} - sum_{k=1}^{j-1}l_{ik}u_{kj}
    L matrix:
        l_{ii} = 1, l_{ij} = (a_{ij} - sum_{k=1}^{i-1}l_{ik}u_{kj}) / u_{ii}
    '''
    M, N = A.shape
    L = np.zeros((M,M))
    U = np.zeros((M,N))
    # U matrix - step1 
    for i in range(M):
        
        # First, Upper triangular matrix
        #for j in range(i+1, N):
        for j in range(i, N): 
            sum_val = 0
            for k in range(j-1):
                sum_val += L[i][k]*U[k][j]
            U[i][j] = A[i][j] - sum_val
            
        # second, Lower traingular marix
        L[i][i] = 1
        for j in range(i, M):
            sum_val = 0
            for k in range(i):
                sum_val += L[j][k]*U[k][i]
            L[j][i] = (A[j][i] - sum_val) / U[i][i]   
       
    return L, U

def L_inverse(L):
    '''
    Useful function for L inverse matrix
    
    '''
    M = len(L)
    L_ = np.zeros_like(L)
    # Diagonal elements
    for i in range(M):
        L_[i][i] = 1 / L[i][i]
        
    # Off diagonal elements
    for i in range(1, M):
        for j in range(i):
            sum_val = 0
            for k in range(j,i):
                sum_val += L[i][k] * L_[k][j]
            L_[i][j] = - sum_val / L[i][i]
    return L_

def LU_gauss_seidel(A):
    '''
    Useful function for Gauss-Seidel LU decomposition
    
    '''
    M, N = A.shape
    L = np.zeros_like(A)
    U = np.zeros_like(A)
    for i in range(M):
        for j in range(N):
            if i >= j:
                L[i][j] = A[i][j]
            else:
                U[i][j] = A[i][j]
    return L, U

# To-do partiaal pivoting LU