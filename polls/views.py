from django.shortcuts import get_objecst_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import Question

# Create your views here.
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = { 'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)
	#-second output option-
	#template = loader.get_template('polls/index.html')
	#return HttpResponse(template.render(context, request))
	#-first output option-
	#output = ', '.join([q.question_text for q in latest_question_list])
	#return HttpResponse(output)

def detail(request, question_id):
	#404 error shortcut
	question = get_objecst_or_404(Question, pk=question_id)
	return render(request, 'polls/details.html', {'question': question})
	#-without the 404 import, this is what you do
	#try:
	#	question = Question.objects.get(pk=question_id)
	#except Question.DoesNotExist:
	#	raise Http404("Question does not exist")
	#return render(request, 'polls/details.html', {'question': question})
	#response = "you're looking at the results of the question %s."
	#return HttpResponse(response % question_id)

def results(request, question_id):
	response = "you're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)
