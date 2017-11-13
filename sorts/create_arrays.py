import numpy as np
import os 

def create_dir(path):
    try:
        os.mkdir(path)
    except FileExistsError as e:
        pass


def create_arrays(amount, start, end, step):
    create_dir('merge')
    create_dir('insert')

    for i in range(start, end, step):
        create_dir('merge/{}'.format(i))
        create_dir('insert/{}'.format(i))

        for j in range(0, amount):
            np.savetxt('merge/{0}/{1}.txt'.format(i, j), np.random.randint(100000000, size = i).tolist(), fmt='%i')


if __name__ == "__main__":
    create_arrays(5, 1000000, 1000001, 50000)
