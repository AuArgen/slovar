from datetime import datetime, timezone
from .models import *
from django.http import JsonResponse
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


@login_required(login_url='login')
def learned_word(request, pk):
    word = get_object_or_404(Word, id=pk)
    get = LearnedWord.objects.filter(user_id=request.user, word=word).first()

    if not get:
        new_word = LearnedWord(user_id=request.user, word=word, active=True)
        new_word.save()
        return JsonResponse({'message': 'Ok'})
    else:
        get.active = True
        get.save()
        return JsonResponse({'message': 'Ok'})

    return JsonResponse({'message': 'No'})



@login_required(login_url='login')
def learned_text(request, pk):
    text = get_object_or_404(Text, id=pk)
    learned_text = LearnedText.objects.filter(user_id=request.user, word=text).first()
    if not learned_text:
        new_word = LearnedText(user_id=request.user, word=text, active=True)
        new_word.save()
        return JsonResponse({'message': 'Ok'})
    else:
        learned_text.active = True
        learned_text.save()
        return JsonResponse({'message': 'Ok'})
    return JsonResponse({'message': 'No'})


@login_required(login_url='login')
def learned_show_text(request):
    texts = Text.objects.filter(
        learnedtext__user_id=request.user,
        learnedtext__active=True
    ).order_by('-learnedtext__id').distinct()
    context = {
        'words': texts,
    }
    return (render(request, 'showLearnedText.html', context))


@login_required(login_url='login')
def learned_delete_text(request, pk):
    learned_text = get_object_or_404(LearnedText, user_id=request.user, word=pk)
    learned_text.active = False
    learned_text.save()
    return redirect('learned-show-text')


@login_required(login_url='login')
def learned_show_word(request):
    words = Word.objects.filter(
        learnedword__user_id=request.user,
        learnedword__active=True
    ).order_by('-learnedword__id').distinct()
    context = {
        'words': words,
    }
    return (render(request, 'showLearnedWord.html', context))


@login_required(login_url='login')
def learned_delete_word(request, pk):
    learned_word = get_object_or_404(LearnedWord, user_id=request.user, word=pk)
    learned_word.active = False
    learned_word.save()
    return redirect('learned-show-word')
