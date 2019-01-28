from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import CreatePostModelForm
from .forms import CommentModelForm
from datetime import datetime
from django.shortcuts import redirect

# Create your views here.


def index(request):
	context = {}
	post = Post.objects.all()
	context['posts'] = post
	return render(request, 'index.html', context)

def details (request, post_id):
	context = {}
	context['posts'] = Post.objects.get(id=post_id)
	return render(request, 'details.html', context)

def update (request,post_id):
	post = Post.objects.get(id = post_id)
	context['form'] = PostModelForm(initial={'date_updated': datetime.now})

	if request.method == 'POST':
		form = PostModelForm(request.POST, instance=post)
		if form.is_Valid():
			form.save()
			return HttpResponse('Post updated')
		else:
			context['form'] = form
			render(request, 'update.html', context)
	else:
		context['form'] = QuestionModelForm(instance = post)
	return render(request, 'update.html', context)

def create(request):
	context = {}
	context['form'] = CreatePostModelForm(initial={'date_created': datetime.now})

	if request.method == "POST":
		form = CreatePostModelForm(request.POST)
		
		if form.is_valid():
			form.save()
			return redirect('/post/')
		else:
			context['form'] = form
			return render(request, 'create.html', context)
	else:
		return render(request, 'create.html', context)


def comment(request):
	context = {}
	context['form'] = CommentModelForm(initial={'date_created': datetime.now})

	if request.method == "POST":
		form = CommentnModelForm(request.POST)
		
		if form.is_valid():
			form.save()
			#form.pub_date = datetime.now()
			#form.save()
			return redirect('/post/')
		else:
			context['form'] = form
			return render(request, 'comment.html', context)
	else:
		return render(request, 'comment.html', context)

