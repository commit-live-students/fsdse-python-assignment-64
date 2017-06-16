import numpy as np

def solution(array):
    print "Original array:"
    print array
    new_reverse_array = np.flipud(array)
    print "Reverse array:"
    print new_reverse_array
    return new_reverse_array
