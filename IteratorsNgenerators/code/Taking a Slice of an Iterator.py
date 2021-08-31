from itertools import islice


def count(n):
    while True:
        yield n
        n+=1

if  __name__ == '__main__':
    c = count(0)
    #print(c[10:20]) # TypeError: 'generator' object is not subscriptable
    for i in (islice(c,10,20)):
        print(i,end=',')