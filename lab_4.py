import math
from numpy import arange

a = 0
b = math.pi/4
STEP = 0.01
FUNC = 'math.tan(x)'


def left_point_method(func:str, diapason:list):
    if not func and not diapason:
        raise Exception("no function or diapason")
    if len(diapason) > 2:
        raise Exception("diapason must consistrs of 2 int nums")

    summary =  0 
    for x in arange(diapason[0], diapason[1], STEP):
        summary += eval(f'math.tan({x})')
    
    return summary * STEP


def right_point_method(func:str, diapason:list):
    if not func and not diapason:
        raise Exception("no function or diapason")
    if len(diapason) > 2:
        raise Exception("diapason must consistrs of 2 int nums")

    summary = 0
    for x in arange(diapason[0]+STEP, diapason[1]+STEP, STEP):
        summary += eval(f'math.tan({x})')
    
    return summary * STEP


def middle_point_method(func:str, diapason:list):
    if not func and not diapason:
        raise Exception("no function or diapason")
    if len(diapason) > 2:
        raise Exception("diapason must consistrs of 2 int nums")

    summary = 0
    for x in arange(diapason[0]+STEP/2.0, diapason[1], STEP):
        summary += eval(f'math.tan({x})')
    
    return summary * STEP

# def trapezoid_point_method(func:str, diapason:list):
#     if not func and not diapason:
#         raise Exception("no function or diapason")
#     if len(diapason) > 2:
#         raise Exception("diapason must consistrs of 2 int nums")

#     summary = 0
#     for x in arange(diapason[0]+STEP/2.0, diapason[1], STEP):
        
#         summary += eval(f'math.tan({x})')
#     return summary * STEP

if __name__ == "__main__":
    res_1 = left_point_method(FUNC, [a,b])
    res_2 = right_point_method(FUNC, [a,b])
    res_3 = middle_point_method(FUNC, [a,b])
    print(res_1, res_2, res_3)