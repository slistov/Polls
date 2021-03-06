from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Poll, Question, Answer, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Poll.objects.order_by('-start_date')[:5]


class PollView(generic.DetailView):
    model = Poll
    template_name = 'polls/poll.html'


class QuestionView(generic.DetailView):
    model = Question
    template_name = 'polls/question.html'



class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def index(request):
    latest_poll_list = Poll.objects.order_by('-start_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_poll_list': latest_poll_list,
    }
    return HttpResponse(template.render(context, request))

def poll(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/poll.html', {'poll': poll})

def question(request, poll_id, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/question.html', {'question': question})

def results(request, poll_id, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, poll_id, question_id):
    SESSION = {
        'GUID': '1A1A',
        'user_id': 1
    }

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.answer_set.get(pk=request.POST['answer'])
    except (KeyError, Answer.DoesNotExist):
        # Снова показать форму голосования
        return render(request, 'polls/question.html', {
            'question': question,
            'error_message': "Вы не сделали выбор",
        })
    else:
        # selected_choice.votes += 1
        # selected_choice.save()
        choice = Choice(answer=selected_choice, user_id=SESSION['user_id'])
        choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.poll_id, question.id,)))