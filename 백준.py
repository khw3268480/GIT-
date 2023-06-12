import sys

n = int(input())
num_size = list(map(int, sys.stdin.readline().split()))
num_lst = list(sorted(set(num_size)))

dic = dict()
for i in range(len(num_lst)):
    dic[num_lst[i]] = i # <- 
for i in num_size:
    print(dic[i],end=" ")

# print(dic)