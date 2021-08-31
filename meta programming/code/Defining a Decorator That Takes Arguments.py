import logging
from functools import wraps

def logged(level, name = None, message = None):

    def decorator(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmessage = message if message else func.__name__


        @wraps(func)
        def wrapper(*args,**kwargs):
            log.log(level=level,msg=logmessage)
            return func(*args,*kwargs)
        return wrapper
    return decorator

@logged(level=logging.CRITICAL)
def foo():
    pass

if __name__ == '__main__':
   foo()