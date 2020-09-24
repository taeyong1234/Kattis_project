
def sums(N):
    if N & (N-1) == 0:
        print('IMPOSSIBLE')

    else:
        if N % 2 == 1:
            print("{:d} = {:d} + {:d}".format(N,N//2,N//2+1))
        else:
            i = 3
            while(N - i):

                if i % 2 == 1:
                    if N % i == 0:
                        start = int(N/i-i//2)
                        print("{:d} = {:d}".format(N, start) + (" + {:d}" * (i - 1)).format(
                            *[start + j for j in range(1, i)]))
                        break
                elif i % 2 == 0:
                    if (N/i)-(N//i) == 0.5:
                        start = int(N//i+1-i//2)
                        print("{:d} = {:d}".format(N, start) + (" + {:d}" * (i - 1)).format(
                            *[start + j for j in range(1, i)]))
                        break
                i += 1

if __name__ == '__main__':
    T = int(input())
    while(T):
        T -= 1
        N = int(input())
        sums(N)









    # 어디에서 오류인지보고
    # 프린드문 공부하기  https://mingrammer.com/understanding-the-asterisk-of-python/

