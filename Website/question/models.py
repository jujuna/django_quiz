from django.db import models
from django.core.exceptions import ValidationError

class Question(models.Model):
    question=models.CharField(max_length=100)
    answer_question=models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.question

    
class Answer(models.Model):
    questin=models.ForeignKey(Question, on_delete=models.CASCADE, related_name="questions", blank=True)
    answer=models.CharField(max_length=100, null=True)

    
    def __str__(self):
        return str(self.questin)