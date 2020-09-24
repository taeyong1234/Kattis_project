

n = int(input())
# number of test

while(n):
    n-=1
    test = list(map(int,input().split()))
    total_num = test[0]
    total = sum(test[1:])
    aver = total/total_num

    above_aver = list(filter(lambda z: z > aver, test[1:]))
    print("%.3f" %(len(above_aver)/total_num*100),end ='')
    print("%")