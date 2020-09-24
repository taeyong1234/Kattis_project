'''
total_num_of branch = 2* (n-1)
stack
root or not
'''



def is_valid(n,branch):

    try:
        stack = [(next(branch),True)]
        c = 0
        total = 0
        while(c < n and stack):

            children,is_root = stack.pop()
            c += 1
            total += children

            if not is_root:
                children -= 1

            for i in range(children):
                stack.append((next(branch), False))

        return not bool(stack) and total == 2*(n-1)
    except StopIteration:
        return False

if __name__ == "__main__":

    print("YES" if is_valid(int(input()), map(int, input().split()))  else "NO")