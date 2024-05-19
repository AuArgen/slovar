from datetime import datetime, timezone

from languages.models import Language
from lessons.models import Lesson, EventTest, Tests
from django.shortcuts import render, redirect, get_object_or_404

from teachers.models import Teacher, News


def index(request):
    languages = Language.objects.all()
    tests = EventTest.objects.all()
    teachers = Teacher.objects.all()
    news = News.objects.all()
    context = {'languages': languages, 'tests': tests, 'teachers': teachers, 'news': news}
    return render(request, 'home/index.html', context)


def lang_in(request, id):
    language = Language.objects.filter(pk=id)
    if language.exists():
        for lang in language:
            lessons = Lesson.objects.filter(language=lang)
            lang.lessons_total = len(lessons)
        language = language[0]
        context = {'language': language}
        return render(request, 'home/language_in.html', context)
    return redirect('index')


def lesson(request, id):
    lessons = Lesson.objects.filter(language=id)
    if lessons.exists():
        language = lessons[0].language
        for lesson in lessons:
            if EventTest.objects.filter(lesson=lesson).exists():
                lesson.is_test = True
            else:
                lesson.is_test = False
        context = {'lessons': lessons, 'language': language}
        return render(request, 'home/lesson.html', context)
    return redirect('index')


def lesson_in(request, id2):
    lesson = Lesson.objects.filter(id=id2)
    if lesson.exists():
        language = lesson[0].language
        for less in lesson:
            evetTests = EventTest.objects.filter(lesson=less)
            if evetTests.exists():
                less.is_test = True
                less.test = evetTests[0]
            else:
                less.is_test = False
        lesson = lesson[0]
        lesson.show += 1
        lesson.save()
        context = {'lesson': lesson, 'language': language}
        return render(request, 'home/lesson_in.html', context)
    return redirect('index')


def test_start(request, id):
    eventTest = EventTest.objects.filter(id=id)
    if eventTest.exists():
        language = eventTest[0].language
        test = eventTest[0]
        details = Tests.objects.filter(eventTest=test)
        context = {'test': test, 'details': details, 'language': language}
        return render(request, 'home/test.html', context)
    return redirect('index')


def teacher(request, id):
    teacher = Teacher.objects.filter(id=id)
    if teacher.exists():
        teacher = teacher[0]
        context = {'teacher': teacher}
        return render(request, 'home/teacher_in.html', context)
    return redirect('index')


def news(request, id):
    news = News.objects.filter(id=id)
    if news.exists():
        news = news[0]
        context = {'news': news}
        return render(request, 'home/news_in.html', context)
    return redirect('index')
