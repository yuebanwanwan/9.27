# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse


#注意当项目中有中文时一定要先声明utf-8
def index(request):
    return HttpResponse(u"Hello Django!你好")

def home(request):
    string = "我在自强学堂学习Django，用它来建网站"
    #return render(request,'home.html',{'string':string})

    # TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    # return render(request, 'home.html', {'TutorialList': TutorialList})

    # info_dict = {'site': '自强学堂', 'content': '各种IT技术教程'}
    # return render(request, 'home.html', {'info_dict': info_dict})

    List = map(str, range(100))  # 一个长度为100的 List
    return render(request, 'home.html', {'List': List,'string':string})

def add(request, a, b):
    c = int(a) + int(b)
    #return HttpResponse(str(c))
    #通过dict向模版html传递参数
    return render(request,'home.html',{'a':a,'b':b})

def logic(request,var):
    return render(request,'home.html',{'var':var})

def login(request,user):
    return render(request,'home.html',{'user':user})