import numpy as np

og_arr = np.array([12, 13, 14, 15, 16, 17, 18, 19])

def solution(array):
    """
    Enter your code here
    """
    rev_arr = np.flip(og_arr, axis=0)
    return rev_arr

print(solution(og_arr))
