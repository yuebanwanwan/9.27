


def logged(func):
    def with_logging(*args,**kwargs):
        print('666:' + str(args[0]))
        print('777:' + str(args[1]))
        print(func.__name__ + ' was called')
        return func(*args,**kwargs)
    return with_logging

@logged
def f(x,y):
    return x*y

print(f(7,8))