
def funct(n):

    answer = [1,3]
    
    current_three = 3
       
    while(len(answer) < n):
        b = answer[:-1]    
        for i in range(len(b)):
            bb = current_three + b[i]
            answer.append(bb)
            if len(answer) == n:
                break
        current_three *= 3
        if len(answer) == n:
            break
        answer.append(current_three)
        
    return answer
    



if __name__ == '__main__':
    n = int(input())
    print(funct(n))
