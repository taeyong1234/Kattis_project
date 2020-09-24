

import sys

oper = {
    '+' : 1,
    '-': 1,
    '*':2,
    '/':2,
    '(':3,
    }
def inf_to_pof(line):

    line = line.strip().replace(' ','')
    stack = []
    output = []
    signorminus = 0
    for i in range(len(line)):

        if i == 0 and line[i] in oper:
            signorminus = 1
        elif line[i] in oper and line[i-1] in oper:
            signorminus = 1
        elif line[i] in oper :

            stack = [line[i]] + stack

        elif line[i] not in oper:
            if line[i] != ')':
                if signorminus == 1:
                    output.append(str(int(line[i])*(-1)))
                    signorminus = 0
                else:
                    output.append(line[i])

            elif line[i] == ')':

                while (stack[0] != '('):
                    output.append(stack.pop(0))
                stack.pop(0)

            if len(stack) >= 1:
                if oper[stack[0]] == 2:
                    while (len(stack) != 0 ):
                        if stack[0] == '(':
                            break
                        output.append(stack.pop(0))
    while(len(stack) != 0):
        output.append(stack.pop(0))
    return output


for line in sys.stdin:

    postfix = inf_to_pof(line)
    print(postfix)






    #print("%.2f" % val)
