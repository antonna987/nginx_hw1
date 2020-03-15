import django.contrib.auth as auth
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
import qa.models as models
import qa.forms as forms

def login(request, *args, **kwargs):
    if request.method == 'POST':
        form = forms.LogInForm(request.POST)
        if form.is_valid():
            auth.login(request, form.user)
            return HttpResponseRedirect('/')
    else:
        form = forms.LogInForm()
    return render(request, 'blog/login.html', {
        'form': form
    })

def signup(request, *args, **kwargs):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = forms.SignUpForm()
    return render(request, 'blog/signup.html', {
        'form': form
    })

def question(request, *args, **kwargs):
    idx = int(kwargs['idx'])

    try:
        q = models.Question.objects.get(pk=idx)
        answers = models.Answer.objects.filter(question=idx)
    except:
        raise Http404

    if request.method == 'POST':
        form = forms.AnswerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(q.get_absolute_url())
    else:
        form = forms.AnswerForm(initial={'question': idx})

    return render(request, 'blog/question.html', {
        'question': q,
        'answers': answers,
        'form': form,
    })

def ask(request, *args, **kwargs):
    if request.method == 'POST':
        form = forms.AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect(question.get_absolute_url())
    else:
        form = forms.AskForm()
    return render(request, 'blog/post_add.html', {
        'form': form
    })

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
