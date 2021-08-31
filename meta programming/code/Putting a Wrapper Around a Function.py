import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        strttime = time.time()
        result = func(*args,**kwargs)
        endtime = time.time()
        print('Processing Time = ',endtime-strttime)
        return result
    return wrapper

@timeit
def countdown(n):
    while n >0:
        n-=1

if __name__ == '__main__':
    countdown(10000000) #Processing Time =  0.7943499088287354