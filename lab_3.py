import numpy as np
import timeit


def jordan_gauss(a, b):
    time = timeit.default_timer()
    a = np.array(a, float)
    b = np.array(b, float)
    n = len(b)

    for k in range(n):
        if np.fabs(a[k,k]) < 1.0e-12:
            for i in range(k+1, n):
                if np.fabs(a[i,k]) > np.fabs(a[k,k]):
                    for j in range (k,n):
                        a[k,j], a[i,j] = a[i,j], a[k,j]
                    b[k], b[i] = b[i], b[k]
                    break
        
        pv = a[k,k]
        for j in range(k,n):
            a[k,j] /= pv
        b[k] /= pv
        
        for i in range(n):
            if i == k or a[i,k] == 0:
                continue
            fc = a[i,k]
            for j in range(k,n):
                a[i,j] -= fc * a[k,j]
            b[i] -= fc * b[k]
    runtime = timeit.default_timer() - time
    return a,b, runtime


def gauss(A):
    time = timeit.default_timer()
    m = len(A)
    n = m + 1
    
    for k in range(m):
        pivots = [abs(A[i][k]) for i in range(k, m)]
        i_max = pivots.index(max(pivots)) + k
        
        A[k], A[i_max] = A[i_max], A[k]

        for i in range(k + 1, m):
            f = A[i][k] / A[k][k]
            for j in range(k + 1, n):
                A[i][j] -= A[k][j] * f

            A[i][k] = 0
            print(A)
    
    x = []
    for i in range(m - 1, -1, -1):
        x.insert(0, A[i][m] / A[i][i])
        for k in range(i - 1, -1, -1):
            A[k][m] -= A[k][i] * x[0]
    runtime = timeit.default_timer() - time
    return A,x, runtime

if __name__ == "__main__":
    myA = [
            [3,  0, -1],
            [2, -5,  1],
            [2, -2,  6] 
    ]

    myB = [
            -4,
             9,
             8
    ]
    myA_B_raw = [
              [ 3,  0, -1, -4],
              [ 2, -5,  1,  9],
              [-3, -2,  6,  8] 
    ]
    myA_B = [
              [ 3,  0, -1, -4],
              [ 2, -5,  1,  9],
              [-3, -2,  6,  8] 
    ]
    
    Tr_A_1, Res_X_1, runtime_1 = jordan_gauss(myA, myB)
    Tr_A_2, Res_X_2, runtime_2 = gauss(myA_B)
    print("\nМетод Жордана-Гаусса: \nПервичная матрица: ")
    for i in range(len(myA)):
        print(myA[i])
    print("\nПервичный вектор: \n[")
    for i in range(len(myB)):
        print('  ', myB[i], ',', sep='')
    print("    ]\n\nИтоговая матрица: ")
    for i in range(len(Tr_A_1)):
        print(Tr_A_1[i])
    print("\nИтоговый вектор: \n[")
    for i in range(len(Res_X_1)):
        print('  ', round(Res_X_1[i]), ',', sep='')
    print("       ]\nОтвет:")
    for i in range(len(Res_X_1)):
        print(f"x{i+1} = {round(Res_X_1[i])}")

    print("\nМетод Гаусса: \nПервичная матрица(A|B): ")
    for i in range(len(myA_B_raw)):
        print(myA_B_raw[i])
    print("\nИтоговая матрица(A|B):")
    for i in range(len(Tr_A_2)):
        print(Tr_A_2[i])
    print("\nОтсюда получаем: ")
    print(f"{Tr_A_2[0][0]}*x1 + {Tr_A_2[0][1]}*x2 + {Tr_A_2[0][2]}*x3 = {Tr_A_2[0][3]}")
    print(f"{Tr_A_2[1][0]}*x1 + {Tr_A_2[1][1]}*x2 + {Tr_A_2[1][2]}*x3 = {Tr_A_2[1][3]}")
    print(f"{Tr_A_2[2][0]}*x1 + {Tr_A_2[2][1]}*x2 + {Tr_A_2[2][2]}*x3 = {Tr_A_2[2][3]}")
    print(f"\nОтвет: \nx1 = {round(Res_X_2[0])}, \nx2 = {round(Res_X_2[1])}, \nx3 = {round(Res_X_2[2])}.")


    print(f"\n\nВремя работы: \nметод Жодана-Гаусса - {round(runtime_1, 7)} с., \nметод Гаусса - {round(runtime_2, 7)} с., \nВо сколько раз метод Жордана-Гаусса быстрее метода Гаусса - в {round(runtime_1 / runtime_2, 5)} раз.")
    