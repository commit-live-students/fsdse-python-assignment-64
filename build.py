import numpy as np
#from random import randint

def solution(array):
    l = []
    if array == None:
        return None
    else:
        #print array
        for i in range(len(array)-1,-1,-1):
            l.append(array[i])
        #print l
        #print np.array(l)
        return np.array(l)

#num1 = randint(0, 10)
#num2 = randint(11, 20)
#num3 = randint(21, 30)
#num4 = randint(31, 40)

#array = [num1, num2, num3, num4]
#solution(array)
