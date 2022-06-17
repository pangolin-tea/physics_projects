import numpy as np

from sympy.sympy import *


# eigen_val used to determine eigenvalue of a matrix
def eigen_val(lis):
    dimension = len(lis[0])
    nabla = Symbol('l')
    for x in range(dimension):
        lis[x][x] = lis[x][x] - nabla


def determinate(lis):
    if len(lis) == 2:
        return lis[0][0]*lis[1][1] - lis[0][1]*lis[1][0]

