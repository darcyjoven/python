import numpy as np

m = int(input())
i = 0
o = []
while i <m:
    n = input().split()
    o.append(n)
    i+=1
c=[]
for a in o:
    for b in a:
        if b in c:
            pass
        else:
            c.append(b)

#d = np.unique(c)


print(c.__len__)


# 我的老家