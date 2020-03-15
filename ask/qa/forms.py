import django.contrib.auth as auth
from django import forms
import qa.models as models
from django.contrib.auth.models import User

class LogInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        self.user = auth.authenticate(username=username, password=password)
        if not self.user:
            raise forms.ValidationError(u'Wrong username/password', code='wrong_credentials')
    class Meta:
        model = User
        fields = ('username', 'password')

class SignUpForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError(u'Already existed', code='wrong_username')
        return username
    def clean(self):
        pass
    def save(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        user = User.objects.create_user(
            username, email=email, password=password)
        user.save()
        return user
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)
    def clean(self):
        if not self._user.is_authenticated:
            raise forms.ValidationError(u'Please login', code='login_required')
    def save(self):
        self.cleaned_data['author'] = self._user
        question = models.Question(**self.cleaned_data)
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField()
    def clean(self):
        if not 'question' in self.cleaned_data or \
            not models.Question.objects.get(pk=self.cleaned_data['question']):
            raise forms.ValidationError(u'Wrong wuestion ID', code='wrong_id')
    def save(self):
        self.cleaned_data['question'] = \
            models.Question.objects.get(pk=self.cleaned_data['question'])
        answer = models.Answer(**self.cleaned_data)
        answer.save()
        return answer
