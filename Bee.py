
v = ['aa','ee','ii','oo','uu','yy']

while(True):

    n = int(input())

    if n == 0:
        break

    else:
        max_dv = -1
        storage = []
        for i in range(n):
            word = input()
            num_of_dv = sum([word.count(i) for i in v])
            if num_of_dv > max_dv:
                max_dv = num_of_dv
                storage.append(word)
        print(storage[len(storage)-1])

# 주석이 없어야 돌아가는듯
