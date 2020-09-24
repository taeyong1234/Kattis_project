import sys
import math


def distance(a,b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)


def all(N):

    pos_all = []
    sum_x = 0
    sum_y = 0
    for i in range(N):
        inp = sys.stdin.readline().split()
        it = iter(inp)
        pos = []
        pos.append(float(next(it)))
        pos.append(float(next(it)))
        next(it)
        init_degree = float(next(it))

        for j in range(4, len(inp), 2):
            if inp[j] == 'walk':

                pos[0] += math.cos(math.radians(init_degree)) * float(inp[j + 1])
                pos[1] += math.sin(math.radians(init_degree)) * float(inp[j + 1])

            elif inp[j] == 'turn':
                init_degree += float(inp[j + 1])

        pos_all.append(tuple(pos[:2]))
        sum_x += pos[0]
        sum_y += pos[1]


    aver_x = sum_x / len(pos_all)
    aver_y = sum_y / len(pos_all)
    a = (aver_x, aver_y)
    # worst

    dis = [distance(a, pos_all[i]) for i in range(N)]

    print("{:.6f} {:.6f} {:.6f}".format(aver_x, aver_y, max(dis)))

if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        all(n)
# abs를 하니까 틀리지 ㅎㅎ