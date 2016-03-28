from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator

# Create your views here.
def test(request, *args, **kwargs):
	return HttpResponse('OK')

def main(request):
	questions = Question.objects.order_by('-id')
	page_num = request.GET.get('page', 1)
	limit = 10
	paginator = Paginator(questions, limit)
	paginator.baseurl = '/?page='
	page = paginator.page(page_num)
	return render(request, 'templates/main.html', {
		'questions':	page.object_list,
		'paginator':	paginator,
	})
	
def popular(request):
	questions = Question.objects.order_by('-rating')
	page_num = request.GET.get('page', 1)
	limit = 10
	paginator = Paginator(questions, limit)
	paginator.baseurl = '/popular/?page='
	page = paginator.page(page_num)
	return render(request, 'templates/main.html', {
		'questions':	page.object_list,
		'paginator':	paginator,
	})

def question(request, id):
	question = get_object_or_404(Question, slug=id)
	try:
		answers = Answers.objects.get(question=question.id)
	except answers.DoesNotExist:
		answers = None
	return render(request, 'templates/question.html', {
		'question':		question,
		'answers':		answers,
	})