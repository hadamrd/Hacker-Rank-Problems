import math
import os
import random
import re
import sys

N =  pow(10,9)+7
    
    
def update(bit, i, v):
    n = len(bit)
    while i < n :
        bit[i]+=v
        i+=i&(-i)

def getsum(bit, i):
    s=0
    while i>0 :
        s+=bit[i]
        i -= i&(-i)
    return s

def getnP(P,fixed):
    n = len(P)
    m = max(P)
    nI=[0]
    for i in range(2,n+1):
        nI.append(nI[-1] + fixed[i-2] ) 
    bit = [0 for i in range(m+1)]
    
    nP = [0 for i in range(n)]
    for i in range(n-1,0,-1):
        if P[i] > 0 :
            nP[i] = nI[P[i]-1] - getsum(bit, P[i]-1) 
            update(bit, P[i], 1)  
        else :
            nP[i] = -1
    
    return nP
    
def solve(P):
    n = len(P)
    fixed = n*[0]
    
    for v in P:
        if v > 0 :
            fixed[v-1] = 1
            
    idZ   = [i for i in range(n) if P[i]==0 ]
    idNZ  = [i for i in range(n) if P[i]>0 ]
    vP    = [i for i in range(1,n+1) if not fixed[i-1]]
    nz    = len(idZ)
    nV,nZ,f = [0],[0],[1]

    for i in range(1,n):
        f.append( f[-1]*i %N )
        nV.append(nV[-1]+(not fixed[i-1])) 
        nZ.append(nZ[-1]+(not P[i-1]))
    f.append( f[-1]*n %N)          
    
    nP = getnP(P,fixed)

    Tnz = sum( ( P[i] - 1 - nP[i] ) * f[n-i-1] for i in idNZ  ) 
    Tz  = sum( ( i - nZ[i] ) * f[n-i-1] for i in idZ )
    S  = f[nz] * ( Tnz - Tz + 1) %N

    if nz > 0 :
        svP = sum(j-1 for j in vP)
        snPV = [0]
        for i in range(1,n):
            snPV.append( snPV[-1] + nV[P[i-1]-1]*(P[i-1]>0) )
        Tnz = sum( nZ[i] * nV[P[i]-1] * f[n-i-1] for i in idNZ )
        Tz  = sum( ( svP + snPV[i] ) * f[n-i-1] for i in idZ )
        S += f[nz-1] * ( Tz - Tnz ) %N
        
    if nz > 1 :
        Tz = sum( nZ[i] * f[n-i-1] for i in idZ ) * sum( nV[l-1] for l in vP if l>1 )
        S -= f[nz-2] * Tz %N
        
    return S%N

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = solve(a)

    fptr.write(str(result) + '\n')

    fptr.close()
