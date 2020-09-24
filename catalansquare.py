'''
n : 0 <= n <= 5000
상당히 큰수임
목표는 Sn
Cn, ....,C0의 값이 필요

홀수 짝수에 따라 값이 다름.
C0 = C1 = 1
Cn에 대한 점화식을 구할 수 있음


Sn은?
Sn = Cn+1
'''
from collections import defaultdict

C = defaultdict(lambda:-1)

C[0] = 1
n = int(input())
for i in range(n+1):
    C[i+1] = C[i]*(4*i+2)//(i+2)
print(C[i+1])








