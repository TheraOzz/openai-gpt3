from django.shortcuts import render

# Create your views here.
from . import gpt3_models

# gpt3_models.gpt3_question_and_answer()

def base(request):
    context = {}
    return render(request, 'base.html', context)
