import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")# project_name 项目名称
django.setup()

from blog.models import Blog,Article

blog = Blog()
blog.title = '标题1'
blog.content = 'content1'
blog.save()

article = Article()
article.title = 'article-title-1'
article.content = 'article-content-1'
article.save()
#blog.save(using='db1')