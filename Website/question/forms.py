from django import forms

from .models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = "__all__"


class NewAnswerForm(forms.Form):
    questions = Question.objects.all()  # @TODO: Quizz.questions

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for q in self.questions:
            self.fields[f'answer{q.pk}'] = forms.CharField(
                help_text=q.question,
                required=True,
                error_messages={'required': "შეავსეთ ველი", }
            )

    def clean(self):
        questions = []
        for q in self.questions:
            answer_field = f'answer{q.pk}'
            value = self.cleaned_data.get(answer_field)
            if value:
                questions.append(
                    AnswerForm({'question': q.pk, 'answer': value})
                )

        self.cleaned_data['questions'] = questions

    def save(self, ):
        for answer in self.cleaned_data['questions']:  # type: AnswerForm
            answer.save()
