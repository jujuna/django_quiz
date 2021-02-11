from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from .forms import QuestionForm,AnswerForm
from .models import Question,Answer
import random
from django.forms import modelformset_factory, formset_factory



def home(request):
    form=QuestionForm
    if request.method=='POST':
        form=QuestionForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, "question/base.html", {"form":form})

def ans(request):
    questions=Question.objects.all()
    form=AnswerForm()
    if request.method=="POST":
        form=AnswerForm(request.POST)
        if form.is_valid():
            print(request.POST)
            ques=request.POST.getlist("question_id")
            ans=request.POST.getlist("answer")
            for i in range(len(ques)):
                form=Answer(questin=Question.objects.get(id=ques[i]), answer=ans[i])
                form.save()
                
    else:
        form=AnswerForm()
    return render(request, "question/ans.html", {"form":form, "questions":questions})
    


