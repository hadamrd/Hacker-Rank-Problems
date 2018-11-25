#!/bin/python3

import math
import os
import random
import re
import sys


def ringIndices(p,m,n):
    for k in range(n-2*p  ) : yield (p, p+k)
    for k in range(m-2*p-1) : yield (p+k+1, n-p-1)
    for k in range(n-2*p-1) : yield (m-p-1, n-p-k-2)
    for k in range(m-2*p-2) : yield (m-p-k-2, p)

def matrixRotation(matrix, r):
    col = len(matrix[0])
    row = len(matrix)
    for  p in range(min(row,col)//2):
        ring_len = 2 * (m + n - 4 * p) - 4
        if r % ring_len == 0 :
            continue
        old_ring = [ matrix[i][j] for i,j in ringIndices(p, row, col) ]
        idx = r % ring_len
        for i,j in ringIndices(p, row, col) :
            matrix[i][j] = old_ring[idx]    
            idx = (idx + 1) % ring_len
            
    for l in matrix :
        print(*l)

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
