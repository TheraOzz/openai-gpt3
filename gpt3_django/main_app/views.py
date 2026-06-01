from django.contrib import messages
from django.shortcuts import render

from .forms import QuestionForm
from .openai_service import ask_openai

# gpt3_models.gpt3_question_and_answer()

def index(request):
    answer = None
    form = QuestionForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            prompt = form.cleaned_data['prompt']
            try:
                answer = ask_openai(prompt)
            except Exception as exc:
                messages.error(request, f'Could not reach OpenAI: {exc}')
        else:
            messages.error(request, 'Please enter a valid question.')

    return render(request, 'index.html', {'form': form, 'answer': answer})