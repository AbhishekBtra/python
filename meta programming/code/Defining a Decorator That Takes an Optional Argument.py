import logging
from functools import wraps,partial

def logged(func=None,*,level = logging.DEBUG, name = None, message = None):
    if func is None:
        return partial(logged, level = level , name = name, message =message)

    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmessage = message if message else func.__name__

    @wraps(func)
    def wrapper(*args,**kwargs):
        log.log(level=level,msg=logmessage)
        return func(*args,*kwargs)
    return wrapper

@logged(level=logging.CRITICAL, name='testlog',message='sample')
def foo():
    pass

@logged
def bar():
    pass

if __name__ == '__main__':
  foo()
  bar()