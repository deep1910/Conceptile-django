from django.shortcuts import render, get_object_or_404,redirect
from django.http import JsonResponse
from .models import Question, QuizSession
import random


def start_quiz(request):
    if request.method == "POST":
        session = QuizSession.objects.create()
        return redirect('get_question', session_id=session.id)
    return render(request, 'quiz/start_quiz.html')
  

def get_question(request, session_id):
    session = get_object_or_404(QuizSession,id=session_id)
    question = random.choice(Question.objects.all())
    print(question.question_text)
    print(question.option_a)
    context = {
        "session_id": session_id,
        "question_id": question.id,
        "question_number": session.total_questions + 1,
        "question_text": question.question_text,
        "options": {
            "A": question.option_a,
            "B": question.option_b,
            "C": question.option_c,
            "D": question.option_d
        }
    }
    return render(request, 'quiz/question.html', context)
 

def submit_answer(request, session_id,question_id):
    session = get_object_or_404(QuizSession, id=session_id)
    question = get_object_or_404(Question, id=question_id)
    user_answer = request.GET.get("answer")

    if user_answer == question.correct_option:
        session.correct_answers += 1
    else:
        session.incorrect_answers += 1
    session.total_questions += 1
    session.save()
    print(session.total_questions)
    if session.total_questions >= 5: 
        return render(request, 'quiz/result.html', {
            "total_questions": session.total_questions,
            "correct_answers": session.correct_answers,
            "incorrect_answers": session.incorrect_answers
        })

    return redirect('get_question', session_id=session.id)