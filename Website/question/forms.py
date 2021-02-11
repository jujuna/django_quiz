from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Question,Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields="__all__"



class AnswerForm(forms.ModelForm):

   
    class Meta:
        model=Answer
        fields="__all__"

    

    


