from django.urls import path
from . import  views

# 함수 기반  view
app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

] ## 이름 index인 함수 호출

# <int:question_id>/vote/ django의 url 패턴 예로 《/polls/34/》를 요청했다고 하면,
# Django는 mysite.urls 파이썬 모듈을 불러오게 됩니다. ROOT_URLCONF 설정에 의해
# 해당 모듈을 바라보도록 지정되어 있기 때문입니다. mysite.urls에서 urlpatterns라는
# 변수를 찾고, 순서대로 패턴을 따라갑니다. 'polls/'를 찾은 후엔, 일치하는 텍스트("polls/")를
# 버리고, 남은 텍스트인 "34/"를 〈polls.urls〉 URLconf로 전달하여 남은 처리를 진행합니다.
# 거기에 '<int:question_id>/'와 일치
# 127.0.0.1/polls/ 를 받고 mysite/urls에서 여기로 보내준다음  views로 이동시켜줌


# ## 클래스 기반 view
# app_name = 'polls'
# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
#     path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#     path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]