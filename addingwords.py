import sys

entry = {}
entry_rev = {}


def definition(vari, num):

    if vari in entry:
        del entry_rev[entry[vari]]
    entry[vari] = num
    entry_rev[num] = vari


def calc(alist):

    if len(list(filter(lambda z: z in entry.keys(), alist[1:][::2]))) != len(alist[1:][::2]):
        print(" ".join(alist[1:]) + ' unknown')

    else:
        sum = eval(
            " ".join(map(lambda z: entry[z] if z in entry.keys() else z, alist[1:-1])))

        if str(sum) in entry_rev:
            print(" ".join(alist[1:]) + " " + entry_rev[str(sum)])

        else:
            print(" ".join(alist[1:]) + ' unknown ')


for line in sys.stdin:
    func = line.split()[0]
    if func == 'def':
        definition(line.split()[1], line.split()[2])

    elif func == 'calc':
        calc(line.split())

    elif func == 'clear':
        entry.clear()
        entry_rev.clear()
    else:
        break

# # 변수 3개 이상은?
# # calc에 value만 넣어서 entry에서 확인

# #calculation function 알고리즈 어디가 틀린지 찾아야함

# #entry_rev를 만듬으로서 dictionary를 list로 접근하는 것에서 (O(n))
# #O(1)로 바꿈

# # for statement 보다 map(lambda), filter(lambda)가 더 빠르다.


def solution(p):
    next = True
    while(next):
        p += 1
        a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        first = p // 1000
        second = (p % 1000) // 100
        third = (p % 100) // 10
        fourth = p % 10
        count = 0
        number = [first, second, third, fourth]
        for i in number:
            if i in a:
                count += 1
                a.remove(i)
        if count == 4:
            next = False
            return p


print(solution(1987))
