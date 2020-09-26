from timeit import default_timer
import scipy.optimize


def penalty_method(interval):
    start = default_timer()

    primal_func = lambda x: 2*x[0]**2 + x[1]**2 - 4*x[0]
    first_D = lambda x: (x[0]**2 - 2*x[1])
    second_D = lambda x: (-2*x[0] + x[1])
      
    cons = ({'type': 'ineq', 'fun': first_D},
           {'type': 'ineq', 'fun': second_D})
    
    result = scipy.optimize.minimize(primal_func, interval, constraints=cons)

    return result.x, default_timer() - start

if __name__ == "__main__":
    x0 = [2.4, 8]
    res, time = penalty_method(x0)
    print(f'\nОтвет: [{res[0]}, {res[1]}]\n\nВремя работы: {time} с.')
