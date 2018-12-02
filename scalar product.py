# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt, pow

data = input()

C, M, n = list(map(int,data.split(' ')))

if n > 1 : 

    lambda_1 = (3-sqrt(5))/2

    lambda_2 = (3+sqrt(5))/2

    alpha = (C**2)*int(pow(lambda_1, 4)/(1+lambda_1) + pow(lambda_2, 4)/(1+lambda_2))

    S = [alpha %M]

    if n > 2 :
        
        alpha = (C**2)*int(pow(lambda_1, 5)/(1+lambda_1) + pow(lambda_2, 5)/(1+lambda_2))

        S.append(alpha %M)

        for k in range(6, 2*n+1):
            
            alpha = 3*S[-1] - S[-2]
            
            S.append(alpha %M)

    print(len(set(S)) %M)

else :
    
    print(0)

