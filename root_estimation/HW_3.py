import mpmath.function_docs
import sympy

import math
import sympy as sp
from sympy.utilities.lambdify import lambdify


def Bisection_Method(polynomial, distance, epsilon=0.0001):
    """
    Finds the root of the Polynomial using the bisection method
    :param polynomial: The Polynomial EX: lambda x: (x*x) - 4
    :param distance: The distance to look in the solution for the Polynomial
    :param epsilon: The max distance to stop
    :return: The solution to the problem with epsilon as the max error
    """
    if polynomial(distance[0]) * polynomial(distance[1]) > 0:  # if there is no root between 2 points.
        return
    max_Loops = -math.log(epsilon / (distance[1] - distance[0]), math.e) / math.log(2, math.e)  # max loops
    loop_Counter = 0
    while loop_Counter <= max_Loops + 2 and abs(distance[0] - distance[1]) >= epsilon:
        # Run till the distance between the root is the lowest or passed max runs
        mid = (distance[1] + distance[0]) / 2
        if polynomial(distance[0]) * polynomial(distance[1]) == 0:
            if polynomial(distance[0]) == 0:
                return distance[0]
            else:
                return distance[1]
        if (polynomial(distance[0]) * polynomial(mid)) <= 0:
            distance[1] = mid
        else:
            distance[0] = mid
        loop_Counter += 1
    if loop_Counter == int(max_Loops + 2):
        print(f'The polynomial does not converge by bisection method. ran {loop_Counter} times ')
        return
    return mid, loop_Counter


def bisection_all_roots(polynomial, polynomial_tag, start_point, end_point, epsilon=0.0001):
    '''
    finds all roots between start_point and end_point using Bisection_Method on polynomial and polynomial_tag
    :param polynomial: polynomial given
    :param polynomial_tag: polynomial_tag
    :param start_point: starting range
    :param end_point: ending range
    :param epsilon: tolerance
    :return: None
    '''
    roots = []
    x1 = start_point + 0.1
    while x1 <= end_point:
        temp = Bisection_Method(polynomial, [start_point, x1], epsilon)  # Polynomial bisection
        temp2 = Bisection_Method(polynomial_tag, [start_point, x1], epsilon)  # Polynomial tag bisection
        if temp is not None:
            print(f'iterated for {temp[1]} times until it found the root {temp[0]}')
            roots.append(temp[0])

        if temp2 is not None and abs(polynomial(temp2[0])) <= epsilon:
            print(f'iterated for {temp2[1]} times until it found the root {temp2[0]}')
            roots.append(temp2[0])
        start_point, x1 = x1, x1 + 0.1
    [print(f'X{i}, {root}') for i, root in enumerate(roots)]


def Newton_Raphson(polynomial, distance, epsilon=0.0001):
    """
    The method solves the root of the Polynomial in the given range using the newton Raphson method
    :param polynomial: The Polynomial to solve
    :param distance: The range where to look (Array<float>[2])
    :param epsilon: The error range
    :return:
    """
    if polynomial(distance[0]) * polynomial(distance[1]) > 0:
        return

    if abs(polynomial_tag(distance[0])) < epsilon:  # Check if one of the sides is really close to the 0
        return distance[0], 0
    elif abs(polynomial_tag(distance[1])) < epsilon:
        return distance[1], 0

    x_r = distance[0]
    x_r1 = x_r - polynomial(x_r) / polynomial_tag(x_r)  # Newton raphson formula
    max_Loops = 50  # max loops
    loopCounter = 0
    while abs(x_r - x_r1) >= epsilon and loopCounter < max_Loops + 1 and polynomial(x_r1) != 0:
        x_r1 = x_r - polynomial(x_r) / polynomial_tag(x_r)
        x_r = x_r1
        loopCounter += 1
    if loopCounter >= int(max_Loops + 1):
        return
    return x_r1, loopCounter


# Ask about this one
def Newton_Raphson_all_roots(polynomial, polynomial_tag, distance, epsilon=0.0001):
    '''
    finds all possible roots between given range.
    :param polynomial:
    :param polynomial_tag:
    :param distance:
    :param epsilon:
    :return: None
    '''
    roots = set()
    x0 = distance[0] + 0.1
    while x0 <= distance[1]:
        temp = Newton_Raphson(polynomial, [distance[0], x0], epsilon)
        temp2 = Newton_Raphson(polynomial_tag, [distance[0], x0], epsilon)
        distance[0], x0 = x0, x0 + 0.1
        if temp is not None:
            print(f'iterated for {temp[1]} times until it found the root {temp[0]}')
            roots.add(temp)
        if temp2 is not None and polynomial(temp2[0]) <= epsilon:
            print(f'iterated for {temp2[1]} times until it found the root {temp2[0]}')
            roots.add(temp2)
    if len(roots) > 0:
        [print(f'X{i}, {root[0]}') for i, root in enumerate(roots)]
    else:
        print("There are no roots in given range. ")


def secant_method(polynomial, epsilon=0.0001):
    '''
    iterative method to find roots between given ranges by initiality guessing range.
    building x2 = x1 - polynomial(x1) *
    where x_r2 is built by guessing initial ranges x_r0 and x_r1
    :param polynomial: polynom checked
    :param range: array of starting_point at index 0 and ending_point and index 1
    :param epsilon: error tolerance
    :return:
    '''
    while True:
        try:
            x0 = float(input("Please enter 1st initial guess"))
            x1 = float(input("Please enter 2nd initial guess"))
            if x0 > x1:
                raise ValueError
            break
        except ValueError:
            print("Invalid point. Please try again")
    loop_counter = 0
    max_Loops = 50  # max loops
    while abs(
            x1 - x0) > epsilon and loop_counter <= max_Loops:  # while absolute value of xk_1 - xk_0 bigger than epsilon or loop counter reached max
        x2 = x1 - (polynomial(x1) * (x1 - x0)) / (polynomial(x1) - polynomial(x0))  # x1 - a good estimation for f_tag.
        x0 = x1
        x1 = x2
    if loop_counter == max_Loops:
        return
    print(f'{x2} is a root for this equation')




# Main
if __name__ == "__main__":
    '''
    User interactive program that builds a polynomial depending on user input, and finds roots of
    given polynomial using 3 methods - Bisection method, Newton Raphson, Secant method
    '''
    n = 0
    temp = 0
    while n == 0 and temp == 0:
        try:
            n = int(input("Please enter polynomial degree: "))
        except ValueError:
            n = 0
            print("You must enter an integer")
    while True:
        try:
            temp = [float(input(f'Enter degree {i} coefficient: ')) for i in range(n, -1, -1)]
            break
        except ValueError:
            temp = 0
            print("You must enter numbers for coefficients")

    x = sp.symbols("x")
    polynomial = 0
    for coefficient in temp:
        polynomial += coefficient * ((x) ** n)
        n = n - 1
    print(polynomial)
    polynomial_tag = sp.diff(polynomial)
    polynomial = lambdify(x, polynomial)
    polynomial_tag = lambdify(x, polynomial_tag)
    while True:
        try:
            x = int(input(
                "Which method would you like to use to find roots ?\n1. Bisection Method \n2. Newton-Raphson Method\n3. Secant method\n"))
            break
        except ValueError:
            print("Invalid choice. Please try again. ")
    while True:
        if x == 3:
            secant_method(polynomial)
            break
        try:
            start_point = float(input("Choose starting point\n"))
            end_point = float(input("Choose ending point\n"))
            break
        except ValueError:
            print("invalid point. Please try again")

    if x == 1:
        bisection_all_roots(polynomial, polynomial_tag, start_point, end_point)
    if x == 2:
        Newton_Raphson_all_roots(polynomial, polynomial_tag, [start_point, end_point])
