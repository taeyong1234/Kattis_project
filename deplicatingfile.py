def hash_fun(s):
    hash_out = 0
    for c in s:
        hash_out ^= ord(c)
    return hash_out


while(True):
    n = int(input())
    if n == 0:
        break
    hash_ = {}
    for i in range(n):
        inp = input()

        file_hash = hash_fun(inp)

        if file_hash not in hash_:
            hash_[file_hash] = [0,{}]

        hash_[file_hash][0] += 1
        if inp not in hash_[file_hash][1]:
            hash_[file_hash][1][inp] = 0
        hash_[file_hash][1][inp] += 1

        coll = 0
        total_files = 0

        for _,alist in hash_.items():

            total_files += len(alist[1])
            if alist[0] > 1:
                for k,v in alist[1].items():
                    coll += (alist[0]-v)*v

    print("{:d} {:d}".format(total_files, coll//2))


