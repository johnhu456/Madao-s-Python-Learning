from django.shortcuts import render,get_object_or_404
import json
from django.http import Http404
from django.utils import timezone
from django.http import HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
from .models import Question, Choice,QuestionEncoder
from django.views import generic
from django.core.urlresolvers import reverse

# class IndexView(generic.ListView):
# 	template_name = 'polls/index.html'
# 	# context_object_name = 'latest_question_list'
# 	# def get_queryset(self):
# 	# 	return Question.objects.filter(
# 	# 		pub_date__lte=timezone.now()
# 	# 	).order_by('-pub_date')[:5]
# 	question = Question.objects.get(pk=1)


class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'
	def get_queryset(self):
		return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

def index(request):
	latest_question_list = Question.objects.all()
	return HttpResponse(json.dumps(latest_question_list,cls=QuestionEncoder), content_type='application/json')

# def detail(request,question_id):
# 	# try:
# 	# 	question = Question.objects.get(pk = question_id)
# 	# except Question.DoesNotExist:
# 	# 	raise Http404("Question dose not exist")
# 	question = get_object_or_404(Question,pk = question_id)
# 	return render(request, 'polls/detail.html',{'question':question})
#
# def results(request,question_id):
# 	question = get_object_or_404(Question, pk = question_id)
# 	return render(request, 'polls/results.html', {'question' : question})



def vote(request,question_id):
	p = get_object_or_404(Question , pk = question_id)
	try:
		selected_choice = p.choice_set.get(pk = request.POST['choice'])
	except (KeyError,Choice.DoesNotExist):
		return render(request, 'polls/detail.html',{
			'question' : p,
			'error_message' : "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
		return HttpResponse(json.dumps(Student("hahaha"),cls=StudentEncoder), content_type='application/json')