import time as tm
import random as rd

SIZE = 150

#function that generate randome list with float nums like [0.72612,0.21261,0.16525,....,0.71126]
def num_gen():
    rnd_num = [rd.uniform(0, 1) for it in range(SIZE)]
    return rnd_num

#function that generate empty list like [0,0,0,0....,0,0]
def zero_gen():
    zero_list = [0 for it in range(SIZE)]
    return zero_list

#main program that multiply 2 matrix size 1200x1200
start = tm.time()
X = [num_gen() for it in range(SIZE)]
Y = [num_gen() for it in range(SIZE)]
result = [zero_gen() for it in range(SIZE)]

for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]

end = tm.time()
time = (end - start)/ 1.0
gflops_per_sec = (SIZE*SIZE*(2.0*SIZE-1.0)/1000**3)/time

print('\ncode runned successfully.')
print('code runtime is ', time, 'seconds')
print('code speed is ', gflops_per_sec, 'gigaflops per second\n')