from itertools import chain


a = list(range(1,5))
b = list(range(5,11))

c = chain(a,b)

for i in c:
    print(i,end=',')#1,2,3,4,5,6,7,8,9,10,