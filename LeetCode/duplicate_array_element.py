# Find All Duplicates in an Array Solution
#Input:
#[4,3,2,7,8,2,3,1]

#Output:
#[2,3]




lst = []
nums = [4,3,2,7,8,2,3,1]

for i in nums:
    temp = nums.count(i)

    if temp>= 2 and i not in lst:
        lst.append(i)
print(lst.sort())

#a = [1,2,3,2,1,5,6,5,5,5]
#import collections
#print([item for item, count in collections.Counter(a).items() if count > 1])

