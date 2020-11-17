from django.urls import path
from . import  views

urlpatterns = [path('',views.index , name='index'),  ## 이름 index인 함수 호출

               ]
# 127.0.0.1/polls/ 를 받고 mysite/urls에서 여기로 보내준다음  views로 이동시켜줌