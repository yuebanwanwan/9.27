from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def add(request):
    #当a没有传递时默认为0
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))
def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
def index(request):
    #render是渲染模版
    #使用render的时候需要将此app加入到settings中的INSTALLED_APPS中
    #这样使用render的时候，Django会自动找到该app下的templates文件
    #小提示，DEBUG=True 的时候，Django 还可以自动找到 各 app 下 static 文件夹中的静态文件（js，css，图片等资源），方便开发


    #为了防止各个app下的静态文件冲突,推荐在每个app下的tmplates文件夹中单独建立一个与app同名的文件夹用来存储static文件
    return render(request, 'calc/home.html')