import sys


def tofe(alist):
    if alist[0] == 0:
        if sum(alist) == 0:
            return alist
        b = alist[0]
        alist[:len(alist) - 1] = alist[1:]
        alist[len(alist) - 1] = b

        return tofe(alist)
    if len(alist) == 1:
        return alist
    if alist[0] == sum(alist):
        return alist

    i = 1
    while (alist[i] == 0):
        i += 1
    if alist[0] == alist[i]:
        alist[0] *= 2
        alist[i] = 0
        alist[1:] = tofe(alist[1:])
    else:
        alist[1:] = tofe(alist[1:])
    return alist

def shift(tile):
    tile_90 = []
    for j in range(len(tile)):
        a = []
        for i in range(len(tile)):
            a.append(tile[i][j])
        tile_90.append(a)

    return tile_90

def reverse(tile):
    tile_180 = []
    for j in range(len(tile)):
        a = []
        for i in range(len(tile)-1,-1,-1):
            a.append(tile[j][i])
        tile_180.append(a)
    return tile_180



def left(tile):

    for i in range(len(tile)):
        print(" ".join(map(str, tofe(tile[i]))))

def up(tile):
    new_tile = []
    for i in range(len(tile)):
        new_tile.append(tofe(tile[i]))
    new_tile = shift(new_tile)
    for i in range(len(new_tile)):
        print(" ".join(map(str, new_tile[i])))

def right(tile):
    new_tile = []
    for i in range(len(tile)):
        new_tile.append(tofe(tile[i]))
    new_tile = reverse(new_tile)
    for i in range(len(new_tile)):
        print(" ".join(map(str,new_tile[i])))

def down(tile):
    new_tile = []
    for i in range(len(tile)):
        new_tile.append(tofe(tile[i]))
    new_tile = shift(reverse(new_tile))
    for i in range(len(new_tile)):
        print(" ".join(map(str, new_tile[i])))

if __name__ == "__main__":
    tile = []


    for i in range(4):
        inp = map(int,sys.stdin.readline().split())
        tile.append(list(inp))



    #direction = {0: 'left',1:'up',2:'right',3:'down'}

    ord = int(input())

    if ord == 0 or ord == 2:

        if ord == 0:
            left(tile)
        elif ord == 2:

            right(reverse(tile))

    elif ord == 1 or ord == 3:


        if ord == 1:
            up(shift(tile))

        elif ord == 3:
            down(reverse(shift(tile)))



