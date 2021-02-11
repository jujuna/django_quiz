
from django.shortcuts import render

from .forms import QuestionForm, NewAnswerForm


def create_question(request):
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, "question/base.html", {"form": form})


def answer(request):
    form = NewAnswerForm(request.POST)

    if form.is_valid():
        form.save()

    return render(request, "quizz.html", {"form": NewAnswerForm(request.POST)})
