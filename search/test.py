from merge import merge_sort
from binary import binary_search
from interpolation import interpolation_search

import time 

import numpy as np

if __name__ == "__main__":
    item = 3402

    for j in range(0, 50):

        A = np.loadtxt('/home/misha/python/sorts/merge/1000000/{0}.txt'.format(j), dtype="int").tolist()
        A.sort()

        inter_time = 0
        binary_time = 0

        for i in range(0, 10):
            binary_start = time.time()
            binary_index, binary_k = binary_search(A, item)
            binary_end = time.time()
            binary_time += (binary_end - binary_start) 

        for i in range(0, 10):
            inter_start = time.time()  
            inter_index, inter_k = interpolation_search(A, item)
            inter_end = time.time()
            inter_time += (inter_end - inter_start) 

        assert inter_index == binary_index

        print("{} | {} | {:f} | {} | {:f} | {} |".format(j, inter_k, float(inter_time), binary_k, float(binary_time), binary_index))
        print("------------------------")
