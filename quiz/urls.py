from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.start_quiz, name='start_quiz'),
    path('<int:session_id>/question/', views.get_question, name="get_question"),
    path('<int:session_id>/<int:question_id>/submit/', views.submit_answer, name='submit_answer'),
    
]