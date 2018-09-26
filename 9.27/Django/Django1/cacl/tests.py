from django.test import TestCase

# Create your tests here.
class T1(object):
    @staticmethod
    def add(x,y):
        return x**y
    @classmethod
    def look(cls):
        print(cls.add(2,4))
        print(cls().add(2,5))
        print(cls)
        print(id(cls))
        print(type(cls))
        print(cls.__dict__)

a = T1.add(2,3)
b = T1().add(2,3)
print(a)
print(b)
T1.look()