## Read input as specified in the question.
## Print output as specified in the question.
#Write your code here

n = int(input())
if(n>=3 and n<40):
    print("#"*n)
    for i in range(n-2):
        print("*"," "*(n-2),"*")
    print("#"*n)
