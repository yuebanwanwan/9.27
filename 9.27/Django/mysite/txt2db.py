import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")# project_name 项目名称
django.setup()

def main():
    from blog.models import Blog
    f = open('oldblog.txt')
    BlogList = []
    for line in f:
        title,content = line.split('****')
        blog = Blog(title=title,content=content)
        #Blog.objects.create(title=title,content=content)
        BlogList.append(blog)
    f.close()
    Blog.objects.bulk_create(BlogList)

if __name__ == '__main__':
    main()
    print('Done!')