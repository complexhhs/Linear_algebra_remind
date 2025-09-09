import numpy as np
from numpy.testing import assert_array_equal
def test_np_zeros(shape=(4,4)):
    my_array = np.zeros(shape)
    #assert my_array == np.zeros_like(my_array), "Numpy zero array shape test failed"
    assert_array_equal(my_array, np.zeros_like(my_array), "Numpy zero array shape test failed")

def test_np_ones(shape=(4,4)):
    my_array = np.ones(shape)
    #assert my_array == np.ones_like(my_array), "Numpy ones array shape test failed"
    assert_array_equal(my_array, np.ones_like(my_array), "Numpy ones array shape test failed")