from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from django.shortcuts import render
import qa.models as models

def login(request, *args, **kwargs):
    return HttpResponse('login OK')

def signup(request, *args, **kwargs):
    return HttpResponse('signup OK')

def question(request, *args, **kwargs):
    idx = kwargs['idx']
    try:
        q = models.Question.objects.get(pk=idx)
        answers = models.Answer.objects.filter(question=idx)
    except:
        raise Http404
    return render(request, 'blog/question.html', {
        'question': q,
        'answers': answers,
    })

def ask(request, *args, **kwargs):
    return HttpResponse('ask OK')

def popular(request, *args, **kwargs):
    try:
        page = int(request.GET.get('page', 1))
        limit = 10
        posts = models.Question.objects.popular()
        paginator = Paginator(posts, limit)
        paginator.baseurl = '/popular/?page='
        page = paginator.page(page)
    except:
        raise Http404
    return render(request, 'blog/posts_popular.html', {
        'paginator': paginator,
        'page': page,
    })

def new(request, *args, **kwargs):
    return HttpResponse('new OK')

def add(request, *args, **kwargs):
    caption = request.GET.get('caption', None)
    category = models.TestCategory(caption=caption)
    category.save()
    return HttpResponse('add OK ' + caption)

def root(request, *args, **kwargs):
    try:
        page = int(request.GET.get('page', 1))
        limit = 10
        posts = models.Question.objects.new()
        paginator = Paginator(posts, limit)
        paginator.baseurl = '/?page='
        page = paginator.page(page)
    except:
        raise Http404
    return render(request, 'blog/posts_new.html', {
        'paginator': paginator,
        'page': page,
    })
