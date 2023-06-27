from django.shortcuts import render
from django.http import HttpResponse


def detail(request, question_id):
    return HttpResponse(f"Essa é a pergunta número {question_id}.")

def results(request, question_id):
    return HttpResponse(f"Resultados da pergunta de número {question_id}.")

def vote(request, question_id):
    return HttpResponse(f"Você está votando na pergunta {question_id}.")

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)