from django.urls import path

from . import views

app_name = 'question'

urlpatterns = [
    path('create-question/', views.create_question, name="home"),
    path('quizz/', views.answer, name="quizz")

]
