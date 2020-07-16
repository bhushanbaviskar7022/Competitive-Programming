#your task to complete a function count_heads() that takes two inputs N and R the function should return the probability 
#of getting exactly R head on N sucessive tosses of a fair coin A fair coin has equal probability of landing a head or a 
#tail 

#sample input
#1 1


#sample output
#0.500000


n , r = map(int , input().split())
if n == 1:
    print('%0.6f'%float(1-(r/2)))
else:
    print('%0.6'%float(1-(r/n)))
