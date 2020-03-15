from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^question/(?P<idx>\d+)/$', views.question, name='question'),
    url(r'^ask/$', views.ask, name='ask'),
    url(r'^popular/$', views.popular, name='popular'),
    url(r'^new/', views.new, name='new'),
    url(r'^add/$', views.add, name='add'),
    url(r'^$', views.root, name='root'),
]
