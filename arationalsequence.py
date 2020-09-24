
n = int(input())

while(n):
    n -= 1
    inp = input().split()
    seq_ch = []
    rat = inp[1]

    for b, i in enumerate(rat):
        if i == '/':
            index_slash = b

    p = int(rat[:index_slash])
    q = int(rat[index_slash + 1:])

    while(p != 1 or q !=1):
        if p > q:
            seq_ch.insert(0,'right_child')
            p = p - q
        elif p < q:
            seq_ch.insert(0,'left_child')
            q = q - p

    index = 1
    while(len(seq_ch)):
        if seq_ch[0] == 'left_child':
            index = 2*index
            seq_ch.pop(0)
        elif seq_ch[0] =='right_child':
            index = 2*index + 1
            seq_ch.pop(0)
    print(inp[0],index)



