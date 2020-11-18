from django.contrib import admin
from .models import  Question, Choice
# Register your models here.

admin.site.register(Question)  #모델을 어드민 사이트에 등록
admin.site.register(Choice)
