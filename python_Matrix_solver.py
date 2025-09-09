# This example from https://math.gsu.edu/xye/course/na_handout/slides/mtx.pdf
from utils import *
import numpy as np
import time

def Conjugate_Gradient(A, B, max_norm_tol=1e-15, max_iteration=1000):
    '''
    Function for calculate Conjugate Gradient method for iterative matrix solver
        "Ax = B"
    Input arguments:
        A: Size MxN matrix
        B: Length "N" vector
        max_norm_tol: Iterative method error tolerance(max_norm)
        max_iteration: if iterative method failes, you have to stop unlimit loop
    Output:
        x: answer vector for linear system 
        idx: the number of iterations
    '''
    assert len(A.shape) == 2, "A is not a rank 2 tensor, Give me a matrix!"
    B = B.ravel()
    assert len(B.shape) == 1, "B is not a rank 1 tensor, Give me a vector!"
    M, N = A.shape
    K = len(B)
    assert N == K, f"Your Matrix and Vector are invalid for linear system. A({M}x{N}) vs B({K})"
    
    x = np.ones_like(B)
    res = B - A@x # Matrix multiplication method would be updated for faster method
    v = res
    for idx in range(max_iteration):
        if max_norm(res) <= max_norm_tol:
            break
        t = (res.T @ res) / (v.T @ ((A @ v)))
        x = x + t*v
        res_ = res - t* A@v
        s = (res_.T @ res_) / (res.T @ res)
        v = res_ + s * v
        res = res_
    return x, idx


def Preconditioned_Conjugate_Gradient(A, B, max_norm_tol=1e-15, max_iteration=1000):
    '''
    Function for calculate Conjugate Gradient method for iterative matrix solver
        "Ax = B"
    Input arguments:
        A: Size MxN matrix
        B: Length "N" vector
        max_norm_tol: Iterative method error tolerance(max_norm)
        max_iteration: if iterative method failes, you have to stop unlimit loop
    Output:
        x: answer vector for linear system 
        idx: the number of iterations
    '''
    assert len(A.shape) == 2, "A is not a rank 2 tensor, Give me a matrix!"
    B = B.ravel()
    assert len(B.shape) == 1, "B is not a rank 1 tensor, Give me a vector!"
    M, N = A.shape
    K = len(B)
    assert N == K, f"Your Matrix and Vector are invalid for linear system. A({M}x{N}) vs B({K})"
    
    # make preconditioner
    C = np.zeros_like(A)
    for i in range(min(M,N)):
        C[i][i] = np.sqrt(np.abs(A[i][i]))
    
    x = np.ones_like(B)
    res = B - A @ x
    C_ = diag_inverse(C)
    w = C_ @ res
    v = C_.T @ w
    for idx in range(max_iteration):
        if max_norm(res) <= max_norm_tol:
            break
        t = w.T @ w / (v @ (A @ v))
        x = x + t*v
        res = res - t * A @ v
        w_ = C_.T @ res
        s = (w_ @ w_) / (w @ w)
        v = C_.T @ w_ + s*v
        w = w_
    return x, idx

if __name__ == "__main__":
    A = np.array([
        [0.2, 0.1, 1, 1, 0],
        [0.1, 4, -1, 1, -1],
        [1, -1, 60, 0, -2],
        [1, 1, 0, 8, 4],
        [0, -1, -2, 4, 700],
    ])
    B = np.array([1,2,3,4,5])
    
    X_expected = np.array(
        [7.859713071,
         0.4229264082,
         -0.07359223906,
         -0.5406430164,
         0.01062616286
         ]
    )
    
    #X, iCG = Conjugate_Gradient(A, B, max_iteration=10)
    start_time = time.time()
    X, iCG = Conjugate_Gradient(A, B)
    end_time = time.time()
    CG_norm = max_norm(X-X_expected)
    print(f"CG's solution: {X}")
    print(f'Iteration for Conjugate Gradient method: {iCG}, max_norm: {CG_norm}, {end_time - start_time} second elapsed.')
    print('')
    
    start_time = time.time()
    X, iCG = Preconditioned_Conjugate_Gradient(A, B)
    end_time = time.time()
    CG_norm = max_norm(X-X_expected)
    print(f"Preconditioned CG's solution: {X}")
    print(f'Iteration for Preconditioned Conjugate Gradient method: {iCG}, max_norm: {CG_norm}, {end_time - start_time} second elapsed.')
    