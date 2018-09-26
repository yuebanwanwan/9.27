from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    #相当于java中的toStrong()方法
    def __str__(self):
        return self.name

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    #添加外键
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    #建立表之间的多对多关系
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline












# 新建一个对象的方法有以下几种：
#
# Person.objects.create(name=name,age=age)
#
# p = Person(name="WZ", age=23)
#
# p.save()
#
# p = Person(name="TWZ")
#
# p.age = 23
#
# p.save()
#
# Person.objects.get_or_create(name="WZT", age=23)
#
# 这种方法是防止重复很好的方法，但是速度要相对慢些，返回一个元组，第一个为Person对象，
# 第二个为True或False, 新建时返回的是True, 已经存在时返回False.

# 获取对象有以下方法：
#
# Person.objects.all()
#
# Person.objects.all()[:10] 切片操作，获取10个人，不支持负索引，切片可以节约内存
#
# Person.objects.get(name=name)
#
#
#
# get是用来获取一个对象的，如果需要获取满足条件的一些人，就要用到filter
#
# Person.objects.filter(name="abc")  # 等于Person.objects.filter(name__exact="abc") 名称严格等于 "abc" 的人
#
# Person.objects.filter(name__iexact="abc")  # 名称为 abc 但是不区分大小写，可以找到 ABC, Abc, aBC，这些都符合条件
#
#
#
# Person.objects.filter(name__contains="abc")  # 名称中包含 "abc"的人
#
# Person.objects.filter(name__icontains="abc")  #名称中包含 "abc"，且abc不区分大小写
#
#
#
# Person.objects.filter(name__regex="^abc")  # 正则表达式查询
#
# Person.objects.filter(name__iregex="^abc")  # 正则表达式不区分大小写
#
#
#
# filter是找出满足条件的，当然也有排除符合某条件的
#
# Person.objects.exclude(name__contains="WZ")  # 排除包含 WZ 的Person对象
#
# Person.objects.filter(name__contains="abc").exclude(age=23)  # 找出名称含有abc, 但是排除年龄是23岁的

