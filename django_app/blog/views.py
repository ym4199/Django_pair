from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
from blog.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'blog/question_list.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'blog/question_detail.html' ,{'question':question})

def results(request, question_id):
    response = "your looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)



