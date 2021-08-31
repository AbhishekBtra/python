def  sample_async(func,*args,callback):
    result =  func(*args)
    callback(result)

def add(a,b):
    return a+b

def print_result(result):
    print('Got : ',result)

#sample_async(add,2,3,callback=print_result) # Got: 5

# What if you want the callback to interact with other variables or parts of the environment.

#We can use below approach with clousre

def  make_handler():
    seq = 0
    def  handler(result):
        nonlocal seq
        seq+=1
        print('[{}]Got : {}'.format(seq,result))
    return handler

handler = make_handler()
sample_async(add,2,3,callback=handler) #[1]Got : 5
sample_async(add,'two',' three',callback=handler) #[2]Got : two three