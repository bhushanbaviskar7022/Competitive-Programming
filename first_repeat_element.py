# write a program to find first repetating element in the given array and return the first repetating element in the array having the smallest index
# Sample input
# 5
# 1 2 3 2 1 


# Sample Output
# 1



n = int(input())
lst = list(map(int, input().split()))
min = -1
myset = dict()
for i in range(n - 1, -1, -1):
    if lst[i] in myset.keys():
        min= i
    else:
        myset[lst[i]] = 1
if min != -1:
    print(lst[min])
