from django import forms
import qa.models as models

class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)
    author = models.User.objects.get(pk=1) # Dummy
    def clean(self):
        pass
    def save(self):
        question = models.Question(**self.cleaned_data)
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField()
    def clean(self):
        if not models.Question.objects.get(pk=self.cleaned_data['question']):
            raise forms.ValidationError(u'Wrong wuestion ID', code='wrong_id')
    def save(self):
        answer = models.Answer(**self.cleaned_data)
        answer.save()
        return answer
