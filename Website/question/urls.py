from django.urls import path
from django.conf.urls import url
from . import views

app_name='question'

urlpatterns = [
    path('', views.home, name="home"),
    path("a/",views.ans, name="ans")
    
    
]
