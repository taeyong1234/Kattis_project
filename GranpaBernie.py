


n = int(input())

info = {}

for i in range(n):
    country,year = input().split()
    if country not in info:
        info[country] = []
    info[country].append(int(year))

queries = int(input())
query = set()

for i in range(queries):
    count, kth = input().split()

    if count not in query:
        info[count].sort()
        query.add(count)

    print(info[count][int(kth)-1])