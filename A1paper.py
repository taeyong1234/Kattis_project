
# import math

# def possible(alist):

#     a = len(alist)
#     result = 0
#     i = 0
#     while(result < 1):
#         if i == len(alist):
#             return 0
#         result += alist[i]*1/pow(2,i+1)
#         i += 1

#     adjust = (result - 1)/(1/pow(2,i))
#     a = alist[i - 1] - adjust
#     alist[i-1] = a

#     return alist[:i]


# def result(apapers):

#     if possible(apapers) == 0:
#         print("impossible")

#     else:
#         new_apaper = possible(apapers)

#         total_peri = 0
#         widt = pow(2, -5 / 4)
#         leng = pow(2, -3 / 4)
#         for i in range(len(new_apaper)):

#             total_peri += 2*(leng + widt)*new_apaper[i]

#             new_len = widt
#             widt = leng/2
#             leng = new_len


#         peri_a1 = 2*(pow(2,-3/4) + pow(2,-1/4))

#         value = (total_peri - peri_a1)/2
#         print(value)





# if __name__ == "__main__":

#     n = int(input())

#     papers = list(map(int, input().split()))

#     result(papers)


