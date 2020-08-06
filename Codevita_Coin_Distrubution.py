N = int(input())
f = int((N-4)/5)
if (N  - f *5)%2 == 0:
    o = 2
else:
    o =1
t = int((N - 5 * f - 1*o)/2)
print(f+o+t, f, t, o)
