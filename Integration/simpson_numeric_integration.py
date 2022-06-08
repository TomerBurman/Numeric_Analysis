import math
def simpson_integration(function, start_point, end_point, n=0):
    '''
    simpson_integration - numeric method to calculate integration by using 2nd degree
    polynomials which we build from dividing our range by n(number of required divisions).

    :param function: function to integrate
    :param start_point: starting range
    :param end_point: end of range
    :param n: number of divisions.
    :return: numeric estimation of the integral
    '''
    if n <= 0:
        n = 100
    h = (end_point - start_point) / n
    i = (1 / 3) * h * (function(start_point) + function(end_point) + sum([multiply(i) * function(start_point + h * i) for i in range(1, n)]))
    return i



def multiply(index):
    '''
    multiplies by 2 if index is even else multiplies by 4.
    :param index:
    :return:
    '''
    if index % 2 == 0:
        return 2
    return 4


def find_required_precision(function_fourth_derivative, start_point, end_point, n):
    '''
    finds required precision
    :param function_fourth_derivative: fourth derivative of the function
    :param start_point: starting range
    :param end_point: end of range
    :param n: number of divisions
    :return: estimated error for this number of divisions.
    '''
    maximum_derivative = max(map(lambda x: function_fourth_derivative(x),
                                 [start_point + 0.1 * i for i in range(0, int((end_point - start_point) / 0.1))]))
    h = (end_point - start_point) / n
    error = (1 / 180) * (h ** 4) * (end_point - start_point) * function_fourth_derivative(maximum_derivative)
    return error


def find_required_partition(function_fourth_derivative, start_point, end_point, required_precision):
    '''
    finds required partition
    :param function_fourth_derivative: fourth derivative of the function
    :param start_point: starting range
    :param end_point: end of range
    :param required_precision: required precision to reach
    :return: estimated error for this number of divisions.
    :return: number of divisions we need to make in order to get this precision.
    '''
    maximum_derivative = max(map(lambda x: function_fourth_derivative(x),
                                 [start_point + 0.1 * i for i in range(0, int((end_point - start_point) / 0.1))]))
    h = math.sqrt(math.sqrt((180 * required_precision) / ((end_point - start_point) * maximum_derivative)))
    n = math.floor((end_point - start_point) / h)
    if n % 2 != 0:
        return n + 1
    return n

print(simpson_integration(math.sin,0,math.pi,4))
a = find_required_partition(math.sin, 0, math.pi, 0.00558)
print(a)
print(find_required_precision(math.sin, 0, math.pi, a))