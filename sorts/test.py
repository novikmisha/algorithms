from merge import merge_sort
from merge_insert import merge_insert_sort
from insertion import insert_sort
from create_arrays import create_arrays

import time
import sys

import numpy as np

def test_range(start, end, step):
    insert_times = []
    i = 1
    for i in range(1, 100):
        for j in range(0, 10):
            A = np.loadtxt('merge/50000/{0}.txt'.format(j), dtype="int").tolist()

            start = time.time()
            merge_insert_sort(A)
            end = time.time()
            insert_times.append(end - start)
            ''' 
            start = time.time()
            merge_sort(A)
            end = time.time()
            merge_times.append(end - start)
            #A = np.loadtxt('merge/{0}/{1}.txt'.format(i, j), dtype="int").tolist()
            '''
        insert_time = (np.mean(insert_times))
        print("{0} - {1:f}".format(i, float(insert_time)))

if __name__ == "__main__":
    test_range(50000, 100000, 50000)

