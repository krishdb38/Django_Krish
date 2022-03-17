import imp
from django.shortcuts import render
from django.http import HttpResponse
from . models import Question
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import  Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse 


from django.views import generic

# Create your views here.

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {"latest_question_list" : latest_question_list }
#     return render(request, 'polls/index.html', context)


# def detail(request, question_id):
#     # Short cut for get objects fromque
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
#     response = "You are looking at the results of question%s"
#     return HttpResponse(response%question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choices_set.get(pk = request.GET.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question  voting Form.
        return render(request, 'polls/detail.html', {'question': question,
        "error_message" : "You didnot select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        " Return the last five published questions"
        return Question.objects.order_by('-pub_date')[:5]
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
