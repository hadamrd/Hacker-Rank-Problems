from math import floor, ceil


def solve(n, k):

    q = (n-1)//k 

    r = (n-1) % k

    T = k*q*(q-1)/2 + q*(r+(k+1)//2) - (r+1)//k

    if r >= ceil((k-1)/2) :

        T += r-ceil((k-1)/2)+1
   
    return int(T)
