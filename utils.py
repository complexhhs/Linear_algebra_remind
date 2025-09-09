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