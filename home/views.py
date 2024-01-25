from datetime import datetime, timezone
from .models import *

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404


@login_required(login_url='login')
def home(request):
    words = Word.objects.filter(user_id=request.user).order_by('-id')
    word = words.count()
    if word < 5:
        return redirect('game_word')
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


@login_required(login_url='login')
def add_text(request):
    if request.method == 'POST':
        word_text = request.POST['word']
        translate_text = request.POST['translate']
        current_date = datetime.now(timezone.utc)
        user = request.user
        getW = Text.objects.filter(user_id=request.user, translate=translate_text, word=word_text).count()
        if getW == 0:
            new_word = Text(user_id=user, word=word_text, translate=translate_text, create=current_date)
            new_word.save()

    words = Text.objects.filter(user_id=request.user).order_by('-id')

    context = {
        'words': words,
    }
    return render(request, 'addText.html', context)

@login_required(login_url='login')
def delete_text(request, pk):
    word = get_object_or_404(Text, id=pk, user_id=request.user)
    word.delete()
    return redirect('add-text')

@login_required(login_url='login')
def text(request):
    words = Text.objects.filter(user_id=request.user).order_by('-id')

    context = {
        'words': words,
    }
    return render(request, 'text.html', context)

@login_required(login_url='login')
def game_word(request):
    words = Word.objects.filter(user_id=request.user).order_by('-id')

    context = {
        'words': words,
    }
    return (render(request, 'gameWord.html', context))

@login_required(login_url='login')
def game_text(request):
    words = Text.objects.filter(user_id=request.user).order_by('-id')

    context = {
        'words': words,
    }
    return render(request, 'gameText.html', context)
@login_required(login_url='login')
def update_word(request, pk):
    word_instance = Word.objects.get(id=pk)  # Use get instead of filter to retrieve a single object

    if request.method == 'POST':
        word = request.POST.get('word', '').strip()  # Use get to get the value and strip to remove trailing spaces
        translate = request.POST.get('translate', '').strip()

        if word and translate:  # Check if both word and translate are not empty
            word_instance.word = word
            word_instance.translate = translate
            word_instance.save()

    return redirect('add-word')

@login_required(login_url='login')
def update_text(request, pk):
    word_instance = Text.objects.get(id=pk)  # Use get instead of filter to retrieve a single object

    if request.method == 'POST':
        word = request.POST.get('word', '').strip()  # Use get to get the value and strip to remove trailing spaces
        translate = request.POST.get('translate', '').strip()

        if word and translate:  # Check if both word and translate are not empty
            word_instance.word = word
            word_instance.translate = translate
            word_instance.save()

    return redirect('add-text')