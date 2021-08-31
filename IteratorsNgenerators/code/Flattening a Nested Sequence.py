from typing import Iterable


def flatten(items):
    for x in items:
        if  isinstance(x,Iterable):
            yield from flatten(x)
        else:
            yield x

nested_list = [[1,2,3],4,5,6,[7,8,9]]

for i in flatten(nested_list):
    print(i,end=',') #1,2,3,4,5,6,7,8,9,