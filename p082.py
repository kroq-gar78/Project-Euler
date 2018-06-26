#!/usr/bin/env python2

import numpy as np

if __name__ == "__main__":
    test_array = np.array([[131, 673, 234, 103, 18], [201, 96, 342, 965, 150], [630, 803, 746, 422, 111], [537, 699, 497, 121, 956], [805, 732, 524, 37, 331]])
    array = test_array[:]
    array = np.genfromtxt('p082_matrix.txt', delimiter=',')
    res = array.copy()
    maxidx = array.shape[0]
    for i in xrange(1,array.shape[0]):
        res[:,i] = res[:,i-1] + array[:,i]
        for _ in xrange(array.shape[0]):
            for j in xrange(array.shape[0]):
                vals =[res[j-1,i] if j>0 else np.inf,
                                                        res[j,i-1],
                                                        res[j+1,i] if j<maxidx-1 else np.inf]
                res[j,i] = min(res[j,i], array[j,i] + min(vals))
    print(min(res[:,-1]))

