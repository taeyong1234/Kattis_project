import sys

N = int(input())
K = int(input())
members = {}

for i in range(N):
    members[str(i+1)] = set()

for i in range(K):
    inp = sys.stdin.readline().split()

    if '1' in inp[1:]:
        for mem in inp[1:]:
            members[mem].add(i)

    else:
        list_merged = set()
        for mem in inp[1:]:
            list_merged |= members[mem]
            # O(n)

        for mem in inp[1:]:
            members[mem] = list_merged.copy()


out = sorted(list(filter(lambda z: members[z] == members['1'], list(members))))

for i in out:
    print(int(i))

# 무슨차이지 ?
'''
n, d = int(input()), int(input())
songs = [set() for i in range(n + 1)]

for i in range(d):
    lis = list(map(int, input().split()))[1:]
    if 1 in lis:
        for j in lis:
            songs[j].add(i)
    else:
        new_set = set()
        for j in lis:
            new_set |= songs[j]
            # var |= value is short for var = var | value
        for j in lis:
            songs[j] = new_set.copy()

list(map(lambda y: print(y[0]), filter(lambda z: z[0] > 0 and len(z[1]) == len(songs[1]), enumerate(songs))))
'''
