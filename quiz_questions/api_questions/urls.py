from django.urls import path

from api_questions.views import questions

urlpatterns = [
    path('questions', questions, name='questions'),
]
