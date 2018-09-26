"""Django1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from learn import views as learn_views
from cacl import views as calc_views
from blog import views as blog_views
from django.conf.urls import url
from blog.views import MyView
from blog.views import HomePageView


#所有的url匹配都有一个起始url链接比如http://127.0.0.1:8000
#name属性为网址的别名
urlpatterns = [
    #该path匹配了所有的url
    #path('',learn_views.index),
    #path('add/', calc_views.add, name='add'),
    #Django支持优雅的url
    path('newadd/<int:a>/<int:b>/', calc_views.add2, name='add2'),

    path('admin/', admin.site.urls),
    #path('',calc_views.index,name='home'),
    path('',learn_views.home,name="home"),
    #匹配add/整数/整数 的url
    #path('add/<int:a>/<int:b>/',learn_views.add,name="learnadd"),

    path('logic/<int:var>/',learn_views.logic,name="logic"),

    path('login/<str:user>/',learn_views.login,name="login"),

    path('add/',blog_views.add,name="blogadd"),

    #path('',blog_views.index,name="blogindex"),

    path('blog/index2',blog_views.index2,name="blogindex2"),

    path('ajax_list/',blog_views.ajax_list,name="ajaxlist"),

    path('ajax_dict/',blog_views.ajax_dict,name="ajaxdict"),



    path('mine/',MyView.as_view(),name="my-view"),


    path('TemplateView/',HomePageView.as_view(),name="templateview"),

    path('blog_home/',blog_views.index3,name="bloghome"),

    path('blog_columns/',blog_views.columns,name="blogcolumns"),

]

