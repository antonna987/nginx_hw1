from django.http import HttpResponse
import qa.models as models

def login(request, *args, **kwargs):
    return HttpResponse('login OK')

def signup(request, *args, **kwargs):
    return HttpResponse('signup OK')

def question(request, *args, **kwargs):
    return HttpResponse('question OK')

def ask(request, *args, **kwargs):
    return HttpResponse('ask OK')

def popular(request, *args, **kwargs):
    return HttpResponse('popular OK')

def new(request, *args, **kwargs):
    return HttpResponse('new OK')

def add(request, *args, **kwargs):
    caption = request.GET.get('caption', None)
    category = models.TestCategory(caption=caption)
    category.save()
    return HttpResponse('add OK ' + caption)

def root(request, *args, **kwargs):
    return HttpResponse('root OK')

