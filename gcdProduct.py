import os
import sys
from math import floor, sqrt, log
MOD = 10**9+7


def sieve(N):
    # sieve 
    prime = [ True for i in range(N+1) ]
    prime[1] = False
    for i in range( 2, floor( sqrt(N) ) + 1):
        for j in range(i**2, N+1, i) :
            prime[j] = False
    return [ p for p in range(1,N+1) if prime[p] ]
 
def solve(n, m):
    primes = sieve (n)
    prod_n_m = 1
    if n>m : n,m = m,n
    for p in primes :
        e_p = 0
        pow_p = p
        while pow_p <= n :   
            e_p =  ( e_p + ( n//pow_p) * (m//pow_p) ) % ( MOD -1 ) 
            pow_p = p * pow_p
        prod_n_m = ( prod_n_m * pow(p, e_p, MOD) ) % MOD 
    return prod_n_m % MOD
