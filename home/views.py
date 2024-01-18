from datetime import datetime, timezone
from .models import *

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404


@login_required(login_url='login')
def home(request):
    words = Word.objects.filter(user_id=request.user).order_by('-id')

    context = {
        'words': words,
    }
    return render(request, 'home.html', context)


@login_required(login_url='login')
def add_word(request):
    if request.method == 'POST':
        word_text = request.POST['word']
        translate_text = request.POST['translate']
        current_date = datetime.now(timezone.utc)
        user = request.user
        getW = Word.objects.filter(user_id=request.user, translate=translate_text, word=word_text).count()
        if getW == 0:
            new_word = Word(user_id=user, word=word_text, translate=translate_text, create=current_date)
            new_word.save()

    words = Word.objects.filter(user_id=request.user).order_by('-id')

    context = {
        'words': words,
    }
    return render(request, 'addWord.html', context)

@login_required(login_url='login')
def delete_word(request, pk):
    word = get_object_or_404(Word, id=pk, user_id=request.user)
    word.delete()
    return redirect('add-word')
