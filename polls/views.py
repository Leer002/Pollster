from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View

from .models import Question, Choice

class PollsBaseView(View):
    model = Question

    def get_question(self, question_id):
        return get_object_or_404(self.model, pk=question_id) 

class IndexView(PollsBaseView):
    def get(self, request):
        latest_question_list = self.model.objects.order_by('-pub_date')[:5]
        context = {
            'latest_question_list': latest_question_list,
        }
        return render(request, 'polls/index.html', context)

class DetailView(PollsBaseView):
    def get(self, request, question_id):
        question = self.get_question(question_id)
        return render(request, 'polls/detail.html', context={'question': question})

class ResultsView(PollsBaseView):
    def get(self, request, question_id):
        question = self.get_question(question_id)
        return render(request, 'polls/result.html', {'question': question})

class VoteView(PollsBaseView):
    def post(self, request, question_id):
        question = self.get_question(question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
