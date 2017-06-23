import numpy as np

def solution(array):
    if(type(array)==list):
        array.reverse()
        return array
    else:
        arr2 = array.tolist()
        arr2.reverse()
        return arr2



tp = solution(np.array([1,2,3,4,5,6]))
print tp
