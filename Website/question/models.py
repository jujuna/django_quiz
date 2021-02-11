from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100, default=None)
    quiz = models.ManyToManyField(to='Quiz', related_name='questions')

    def __str__(self):
        return self.question


class Quiz(models.Model):
    start_date = models.DateTimeField()
    duration = models.IntegerField()
    pass


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="questions", blank=True)
    answer = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.question)
