from django.urls import path
from . import views

#URMConfig
urlpatterns = [
    path('hello/', views.say_hello)
]