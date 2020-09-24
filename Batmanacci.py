from collections import defaultdict

fibo_num = defaultdict(lambda:-1)
fibo_num[1] = 1
fibo_num[2] = 1

def length(n):

    if n >100:
        return -1
    if n not in fibo_num:
        fibo_num[n] = length(n - 2) + length(n - 1)
    return fibo_num[n]

def letter_indicator(n,k):

    if n == 1:
        print('N')
        return 0
    if n == 2:
        print('A')
        return 0
    l = length(n - 2)
    while l == -1:
        n -= 1
        l = length(n-2)

    if k > l:
        k = k - l
        letter_indicator(n-1,k)

    else:
        letter_indicator(n-2,k)

N, K = tuple(map(int, input().split()))

letter_indicator(N,K)

#maximum recursion depth exceeded in comparison?????????