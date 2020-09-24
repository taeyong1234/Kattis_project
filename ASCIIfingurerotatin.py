def control_last_space(list,n):
    ind = n-1
    while n >= 0 and list[ind] == ' ':
        ind -= 1
    print("".join(list[:ind+1]))


first = True
while(True):
    max = 0
    n = int(input()) # n: number of lines

    if n == 0:
        break
    elif first:
        first = False
    else:
        print()

    a = []
    for i in range(n):
        a.append(list(input()))
        if len(a[i]) > max:
            max = len(a[i])

    check = 0
    while (check == 0):
        check = n
        for j in range(n):
            if a[j][0] == ' ':
                check -= 1
        if check == 0:
            for j in range(n):
                del a[j][0]
            max -= 1
        else:
            break

    # making a copy list of a that has each elements with the length of max
    for i in range(n):
        if len(a[i]) < max:
            a[i] = a[i] + [' ']*(max - len(a[i]))

    copy_a = [[' ' for i in range(n)] for i in range(max)]

    for i in range(max):
        for j in range(n):

            c = a[j][i]
            if c == '-':
                copy_a[i][n-1-j] = '|'
            elif c == '|':
                copy_a[i][n-1-j] = '-'
            else:
                copy_a[i][n-1-j] = c

    for i in range(max):
        control_last_space(copy_a[i],n)





