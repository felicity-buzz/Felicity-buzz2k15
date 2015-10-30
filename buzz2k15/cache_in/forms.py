from django import forms

class AnswerForm(forms.Form):
	q_answer = forms.CharField(max_length = 100, label = 'answer')
