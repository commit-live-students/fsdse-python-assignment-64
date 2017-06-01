import numpy as np

def solution(array):
    """
    Enter your code here
    """
    if array is None:
        return None
    return np.flipud(array)
