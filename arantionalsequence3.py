from math import ceil
n = int(input())

while(n):

    n -= 1

    inp = input().split()
    rat_seq = []
    data_num = int(inp[0])
    rat = inp[1]

    tt = True
    while(tt):
        tt = False
        for b,i in enumerate(rat):
            if i == '/':
                slash_index = b
        p = int(rat[:slash_index])
        q = int(rat[slash_index+1:])
        if p == 1 and q == 1:
            a = [str(p), '/', str(q+p)]
            print(data_num, "".join(a))
            break
        if p == 1 and q != 1:
            q = q - 1
            p = p + q
            a = [str(p), '/', str(q)]
            print(data_num, "".join(a))
            break
        elif p != 1 and q == 1:
            q = p + 1
            p = 1
            a = [str(p), '/', str(q)]
            print(data_num, "".join(a))
            break

        if p < q:
            q = q - 1
            p = p + q
            a = [str(p), '/', str(q)]
            print(data_num, "".join(a))
            break

        else:
            x = ceil((p-q)/q)
            p = p - q*x
        # x = number of rightchild
        q = q - p
        p = p + q
        q = x*p + q

        a = [str(p),'/',str(q)]
        print(data_num, "".join(a))