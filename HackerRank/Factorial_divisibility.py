# Given an n integer .
# Find if n! is divisible by 10 or not.
# Where n! represents factorial of .

# Input Format
# The first line contains integer  ; the number of test cases.
# Then  lines follow ; where each line consists of a single integer .

# Output Format
# For each test case, in a seperate line ; print :
# Divisible ; in case you find  divisible by 
# Not Divisible otherwise.

# Sample Input 0

# 2
# 1
# 10
# Sample Output 0

# Not Divisible
# Divisible


T = int(input())
for i in range(T):
  N = int(input())
  if N > 4:
    print("Divisible")
  else:
    print("Not Divisible")
