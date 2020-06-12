from time import time
import random as rd


SIZE = 150


def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time()
        return_value = func(*args, **kwargs)
        end = time()
        print(f'{func.__name__}: {end-start} секунд.')
        return return_value
    return wrapper


def num_gen():
    """function that generate randome list with float nums like [0.72612,0.21261,0.16525,....,0.71126]"""
    rnd_num = [rd.uniform(0, 1) for it in range(SIZE)]
    return rnd_num


def zero_gen():
    """function that generate empty list like [0,0,0,0....,0,0]"""
    zero_list = [0 for it in range(SIZE)]
    return zero_list


@benchmark
def mitrix_multiply():
    """main program that multiply 2 matrix size 1200x1200"""
    X = [num_gen() for it in range(SIZE)]
    Y = [num_gen() for it in range(SIZE)]
    result = [zero_gen() for it in range(SIZE)]

    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]

    gflops = (SIZE*SIZE*(2.0*SIZE-1.0)/1000**3)
    return result, gflops


if __name__ == "__main__":
    a, b = mitrix_multiply()
    print(b)
