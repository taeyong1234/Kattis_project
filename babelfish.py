import sys
index = 0
limit = 100000
stop1 = True
entry = {}

while(stop1):

    entry.append(sys.stdin.readline())
    index += 1
    if entry[index-1] == '\n':
        stop1 = False

while(limit):
    limit -= 1
    words = sys.stdin.readline().split()[0]
    in_entry = 0

    for j in range(len(entry) - 1):

        if words == entry[j].split()[1]:
            print(entry[j].split()[0])
        else:
            in_entry += 1

    if in_entry == len(entry) - 1:
        print('eh')

'''
import sys

entry = {}
add = True

for line in sys.stdin:
    if add:
        if line == '\n':
            add = False
        else:
            entry[line.split()[1]] = line.split()[0]

    else:
        key = line.split()[0]
        if key not in entry:  # dict is assessible with 'key'
            print('eh')
        else:
            print(entry[key])




            # https://stackoverflow.com/questions/513882/python-list-vs-dict-for-look-up-table
# says that the complexity of dict is O(1) and that of a list is O(n)'''


