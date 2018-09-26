from django.shortcuts import render
from django.http import HttpResponse
#引入自定义的表单类
from .forms import AddForm
import json
from django.http import JsonResponse
# Create your views here.


def index(request):
    if request.method == 'POST':

        form = AddForm(request.POST)

        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else:
        form = AddForm()
        return render(request,'index.html',{'form':form})

def index2(request):
    return render(request,'index2.html')


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))

def ajax_list(request):
    a = list(range(100))
    person_info_dict = [
        {"name": "xiaoming", "age": 20},
        {"name": "tuweizhong", "age": 24},
        {"name": "xiaoli", "age": 33},
    ]
    return JsonResponse(person_info_dict,safe=False)


def ajax_dict(request):
    name_dict = {'twz': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1536689510439&di=4cc8aab4713b08fc9245aa8b339aaf66&imgtype=0&src=http%3A%2F%2Fimage5.suning.cn%2Fuimg%2Fb2c%2Fnewcatentries%2F0070158597-000000000618561246_4_800x800.jpg', 'zqxt': 'I am teaching Django'}
    return JsonResponse(name_dict)


from django.http import HttpResponse
from django.views.generic import View


class MyView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')


from django.views.generic.base import TemplateView
from blog.models import Article

class HomePageView(TemplateView):
    #此处用得是learn app下的模版
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView,self).get_context_data(**kwargs)
        context['latest_articles'] = '你好！HomePageView！！！'
        return context


def index3(request):
    return render(request,'blog/index.html')

def columns(request):
    return render(request,'blog/columns.html')


