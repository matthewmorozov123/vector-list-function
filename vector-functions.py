import numpy as np

Va = [2, 5, 7]
Vb = [5, 2.3, 9]
Ma = [[3, 2, 9.1],
      [7, 10, 14],
      [3, 0.5, 17.2]]
Mb = [[8, 17.3, 7.8],
      [2.9, 1, 1.4],
      [5, 0.5, 1.2]]
Mc = [[3, 2],
      [7, 10],
      [3, 0.5]]

def vecScale(A, a):
    return [a * x for x in A]

def vecAdd(A, B):
    return [x + y for x, y in zip(A, B)]

def vecSub(A, B):
    return [x - y for x, y in zip(A, B)]

def vecDot(A, B):
    return sum([x * y for x, y in zip(A, B)])

def vecLinOp1(A, B, a):
    return round(vecDot(A, B) * a, 1)

def vecLinOp2(A, B):
    temp = vecSub(B, A)
    return vecDot(temp, B)
    
