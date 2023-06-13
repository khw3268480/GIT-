import sys

n = int(sys.stdin.readline())
lst1 = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
lst2 = list(map(int, sys.stdin.readline().split()))

for p in lst2:
    if p in lst1:
        print("1", end = " ")
    else:
        print("0", end = " ")