from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question, Choice
from django.template import loader
from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse, Http404, HttpResponseRedirect


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,  # context를 통해 데이터를 전달
    }
    return HttpResponse(template.render(context, request))


# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)  v1

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")   ## 404 예외처리 기능 , raise 예외 발생시키기 (메시지) v2
#     return render(request,'polls/detail.html',{'question':question})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)   ##  try catch 문 생략 가능 get_object_or_404
    return render(request, 'polls/detail.html', {'question': question})  # v3
#get_object_or_404() 함수는 Django 모델을 첫번째 인자로 받고,
# 몇개의 키워드 인수를 모델 관리자의 get() 함수에 넘깁니다.
# 만약 객체가 존재하지 않을 경우, Http404 예외가 발생합니다.

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

## view에서는 request 라는 인자를 받고  HttpResponse 로 리턴함
## 클라이언트에서 request를 받으면 여러가지 정보가 들어있음