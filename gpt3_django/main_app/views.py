from django.shortcuts import render

# Create your views here.
from . import gpt3_models

# gpt3_models.gpt3_question_and_answer()

def index(request):
    context = {}
    return render(request, 'index.html', context)