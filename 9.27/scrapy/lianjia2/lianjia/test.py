"""
:*args的使用方法
:*args 用来将参数打包成tuple给函数体调用
"""
class Person(object):
    def __init__(self,name='defaultname',age='defaultage'):
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        cls.bar = 'mary'
        return object.__new__(cls)

    def __str__(self):
        return 'name:'+self.name+'\n'+'age:'+self.age


person = Person()
print(Person)
print(person)
print(dir(person))
print(dir(Person))

dict1 = {
    '1':1,
    # '2':'2'
}
#list = [1,2,3,'4']
print(dict1['1'])
#print(list.get(1))

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print( d['Michael'])





