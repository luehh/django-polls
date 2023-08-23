from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question 

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/detail.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,"polls/detail.html", {"question": question})

def results(request, question_id):
    response = f'Resultados da pergunta de número {question_id}'
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Você está votando em uma enquete %s." % question_id)

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class QuestionCreateView(CreateView):
    model = Question
    success_url = reverse_lazy('index')