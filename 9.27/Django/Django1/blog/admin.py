from django.contrib import admin

from .models import MyArticle,Person
# Register your models here.
#此文件与后台相关

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','content','pub_date','update_time',)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

admin.site.register(MyArticle,ArticleAdmin)
admin.site.register(Person, PersonAdmin)

#定制加载的列表，根据不同的身份显示不同的列表
class MyModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(MyModelAdmin,self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(author = request.user)