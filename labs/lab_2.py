import numpy as np
import scipy as sc
import time

M = 1200

#My code on numpy:
start_1 = time.time()

a = np.random.random((M, M))
b = np.random.random((M, M))

c = np.dot(a,b)
end_1 = time.time()

tm_1 = (end_1-start_1) / 5.0
gflops_per_sec_1 = (M*M*(2.0*M-1.0)/1000**3)/tm_1
print('========================================================================')
print('результат умножения матриц: \n ', c, '\n\nЗа время: ', tm_1, '\nИ скоростью: ', gflops_per_sec_1, ' гигафлопс/с.\n========================================================================\n')

#Intel code on scipy:
start_2 = time.time()

a = np.array(np.random.random((M, M)), dtype=np.double, order='C', copy=False)  
b = np.array(np.random.random((M, M)), dtype=np.double, order='C', copy=False)  
A = np.matrix(a, dtype=np.double, copy=False)  
B = np.matrix(b, dtype=np.double, copy=False)  
C = A*B

end_2 = time.time()

tm_2 = (end_2-start_2) / 5.0  
gflops_per_sec_2 = (M*M*(2.0*M-1.0)/1000**3)/tm_2

print('========================================================================')
print('результат умножения матриц: \n ', C, '\n\nЗа время: ', tm_2, '\nИ скоростью: ', gflops_per_sec_2, ' гигафлопс/с.\n========================================================================\n')