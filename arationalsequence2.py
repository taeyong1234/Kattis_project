

n = int(input())

while(n):
    n -= 1
    inp = input().split()
    index = int(inp[1])
    seq_child = []

    p = 1
    q = 1

    while(index != 1):
        if index % 2 == 1:
            seq_child.insert(0,'right_child')
            index = index // 2
        else:
            seq_child.insert(0,'left_child')
            index = index // 2

    while(len(seq_child)):
        if seq_child[0] == 'right_child':
            p = p + q
            seq_child.pop(0)
        elif seq_child[0] == 'left_child':
            q = p + q
            seq_child.pop(0)
    a = [str(p),'/',str(q)]
    print(inp[0],"".join(a))