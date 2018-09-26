# from django.core.mail import send_mail
# import os,django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django1.settings")# project_name 项目名称
# django.setup()
# print('I\'am messege')
# send_mail('你好66666！','I am the message.','943804417@qq.com',
#           ['943804417@qq.com'],fail_silently=False)

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# 3次就会回到整个项目的根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(BASE_DIR)