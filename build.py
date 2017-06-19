import numpy as np
def solution(array):
    return np.array(list(array)[len(array)::-1])
