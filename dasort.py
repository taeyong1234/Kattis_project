

from math import ceil

def dasort(arr):
    sorted_arr = sorted(arr)

    i = 0
    j = 0
    c = 0
    while (i != len(arr)):
        if arr[i] == sorted_arr[j]:
            i += 1
            j += 1
        else:
            i += 1

    while (j != len(arr)):
        x = arr.index(sorted_arr[j]
        arr = arr[:x] + arr[x + 1:] + [sorted_arr[j]]
        c += 1
        j += 1

    return c




if __name__ == '__main__':
    N = int(input())
    for i in range(N):
        arr = []
        inp = input().split()
        for j in range(ceil(int(inp[1])/10)):
            arr = arr + list(map(int,input().split()))
        print(inp[0],dasort(arr))