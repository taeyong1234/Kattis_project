
import sys

for line in sys.stdin:
    n = int(line.split()[0])
    total_bit = 32
    register = {}

    if n == 0:
        break
    for i in range(total_bit):
        register[i] = '?'
    while(n):
        n -= 1
        instruction = sys.stdin.readline().split()

        if instruction[0] == 'CLEAR':
            register[total_bit - 1 - int(instruction[1])] = '0'
        elif instruction[0] == 'SET':
            register[total_bit - 1 - int(instruction[1])] = '1'
        elif instruction[0] == 'OR':
            i = total_bit - 1 - int(instruction[1])
            j = total_bit - 1 - int(instruction[2])
            if register[i] == '1' or register[j] == '1':
                register[i] = '1'
            elif register[i] == '?' or register[j] == '?':
                register[i] = '?'
            else:
                register[i] = '0'

        elif instruction[0] == 'AND':
            i = total_bit - 1 - int(instruction[1])
            j = total_bit - 1 - int(instruction[2])
            if register[i] == '0' or register[j] == '0':
                register[i] = '0'
            elif register[i] == '?' or register[j] == '?':
                register[i] = '?'
            else:
                register[i] = '1'

    reg_out = "".join(map(lambda z: register[z], list(register.keys())))
    print(reg_out)
