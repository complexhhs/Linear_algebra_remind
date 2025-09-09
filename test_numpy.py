import numpy as np
from numpy.testing import assert_array_equal
from utils import LU_decomposition, L_inverse

def test_np_zeros(shape=(4,4)):
    my_array = np.zeros(shape)
    #assert my_array == np.zeros_like(my_array), "Numpy zero array shape test failed"
    assert_array_equal(my_array, np.zeros_like(my_array), "Numpy zero array shape test failed")

def test_np_ones(shape=(4,4)):
    my_array = np.ones(shape)
    #assert my_array == np.ones_like(my_array), "Numpy ones array shape test failed"
    assert_array_equal(my_array, np.ones_like(my_array), "Numpy ones array shape test failed")

def test_LU_decomposition():
    A = np.array([
        [6, 18, 3],
        [2, 12, 1],
        [4, 15, 3]
    ])
    L, U = LU_decomposition(A)
    assert_array_equal(L@U, A, "LU decomposition is wrong!")

def test_L_inverse():
    A = np.array([
        [6, 18, 3],
        [2, 12, 1],
        [4, 15, 3]
    ])
    L, U = LU_decomposition(A)
    L_ = L_inverse(L) 
    assert_array_equal(L@L_, np.eye(len(L)), "L inverse is wrong!")

