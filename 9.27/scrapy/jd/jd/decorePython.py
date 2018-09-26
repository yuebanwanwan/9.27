#装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，他的参数一般就是这个需要添加功能的函数对象。
# 装饰器的返回值也是一个函数对象,返回经过处理后的函数(添加了新的功能的函数)。用于有切面需求的场景,和java中Spring框架的AOP概念差不多.是一种代码重用的手段.
import logging
def foo():
    print('i am foo')

#添加新的需求(记录函数的执行日志)
def foo():
    print('i am foo')
    logging.info("foo is runing")

#当其他函数也有类似的需求时，会造成大量的雷同代码，为了减少重复代码或者说代码重用
#我们可以重新定义一个函数：专门处理日志，日志处理完成之后再执行业务代码.

def use_logging(func):
    logging.warn("%s is runing" % func.__name__)
    func()

def bar():
    print('i am bar')

print('-----1-----')
use_logging(bar)
#如果是像上面这样，每次都要将函数作为参数传递给use_logging()函数，会破坏原有的代码逻辑结构(
# 之前是直接运行，现在要改成use_logging(bar))
#那有没有更好的方式呢?

# 1 简单装饰器

def use_logging(func):

    def wrapper(*args,**kwargs):
        logging.warn("%s is runing" % func.__name__)
        return func(*args,**kwargs)
    return wrapper
def bar():
    print('i am bar')
print('-----2-----')
bar = use_logging(bar)
bar()
#函数use_logging就是装饰器，它把执行真正业务方法的func包裹在函数里面，
# 看起来像bar被use_logging装饰了。在这个例子中，函数进入和退出时 ，
# 被称为一个横切面(Aspect)，这种编程方式被称为面向切面的编程(Aspect-Oriented Programming)。

# @符号是装饰器的语法糖,在定义函数的时候使用,避免再一次赋值操作.

@use_logging
def foo2():
    print('i am foo2')

@use_logging
def bar2():
    print('i am bar2')

print('-----3-----')
foo2()
bar2()
#提高了程序的可重复利用性,增加了程序的可读性。
#这一切都要归功于在Python中一切都是对象，函数可以变量一样作为函数参数传递
# 、赋值给其他变量、可作为返回值、可以定义在另外一个函数内.


# 2 带参数的装饰器

# 在上面的装饰器调用中，比如@use_logging，该装饰器唯一的参数就是执行业务的函数。
# 装饰器的语法允许我们在调用时，提供其它参数，比如@decorator(a)。
# 这样，就为装饰器的编写和使用提供了更大的灵活性。


def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warn("%s is running1" % func.__name__)
            return func(*args)
        return wrapper

    return decorator

@use_logging(level="warn")
def foo(name='foo'):
    print("i am %s" % name)

print('-----4-----')
foo()



# 3 类装饰器
class Foo(object):
    def __init__(self,func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('class decorator runing')
        self.func()
        print('class decorator ending')

@Foo
def bar3():
    print('bar3')

print('-----5-----')
bar3()


# 4 functools.wraps
#使用装饰器极大地复用了代码，但是他有一个缺点就是原函数的元信息不见了，
# 比如函数的docstring、__name__、参数列表，先看例子：

def logged(func):
    def with_logging(*args,**kwargs):
        print('666:' + str(args[0]))
        print('777:' + str(args[1]))
        print(func.__name__ + ' was called')
        return func(*args,**kwargs)
    return with_logging

@logged
def f(x,y):
    return x + x*y

print('-----6-----')
# 观察该函数的执行结果，装饰器函数将传入的函数对象func封装在了wrapper函数里，并将参数一起传递.
# 然后在wrapper里先执行添加的功能  最后在执行func()函数(老功能)，
# 最后返回了这个添加了新功能的函数对象wrapper
print(f(8,9))
# 函数f被with_logging取代了,__name__属性也变成了with_logging的
print(f.__name__)
print(f.__doc__)

#这个问题就比较严重的，好在我们有functools.wraps，wraps本身也是一个装饰器，
# 它能把原函数的元信息拷贝到装饰器函数中，这使得装饰器函数也有和原函数一样的元信息了。
#例子如下所示
from functools import wraps

def logged2(func):
    #保留原函数的元信息
    @wraps(func)
    def with_logging(*args,**kwargs):
        print(func.__name__ + ' was called')
        return func(*args,**kwargs)
    return with_logging

@logged2
def f2(x):
    return x*x

print('-----7-----')

print(f2.__name__)
print(f2.__doc__)
print(f2(9))



# 5 内置装饰器
# a
@staticmethod
# b
@classmethod
# c
@property
def f3():
    pass
#等效于f3 = a(b(c(f3)))



