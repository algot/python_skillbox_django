from datetime import datetime

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')


def contacts(request):
    return render(request, 'contacts.html')


def publish(request):
    if request.method == 'GET':
        return render(request, 'publish.html')
    else:
        secret = (request.POST['secret'])
        if secret != settings.SECRET_KEY:
            return render(request, 'publish.html', {
                'error': 'Incorrect secret key'
            })

        name = (request.POST['name'])
        if len(name) == 0:
            return render(request, 'publish.html', {
                'error': 'Empty name'
            })

        text = (request.POST['text'])
        if len(text) == 0:
            return render(request, 'publish.html', {
                'error': 'Empty text'
            })

        article_data.append({
            'id': len(article_data),
            'name': name,
            'date': datetime.now(),
            'text': text.replace('/n', '<br />')
        })
        return redirect('/articles')


article_data = [
    {
        'id': 0,
        'name': 'My first article',
        'date': datetime.now(),
        'text': '''Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.
                   <br>The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.'''
    },
    {
        'id': 1,
        'name': 'My second article',
        'date': datetime.now(),
        'text': '''Давно выяснено, что при оценке дизайна и композиции читаемый текст мешает сосредоточиться. Lorem Ipsum используют потому, что тот обеспечивает более или менее стандартное заполнение шаблона, а также реальное распределение букв и пробелов в абзацах, которое не получается при простой дубликации "Здесь ваш текст.. Здесь ваш текст.. Здесь ваш текст.." Многие программы электронной вёрстки и редакторы HTML используют Lorem Ipsum в качестве текста по умолчанию, так что поиск по ключевым словам "lorem ipsum" сразу показывает, как много веб-страниц всё ещё дожидаются своего настоящего рождения. За прошедшие годы текст Lorem Ipsum получил много версий. Некоторые версии появились по ошибке, некоторые - намеренно (например, юмористические варианты).'''
    },
    {
        'id': 2,
        'name': 'My third article',
        'date': datetime.now(),
        'text': '''Давно выяснено, что при оценке дизайна и композиции читаемый текст мешает сосредоточиться. Lorem Ipsum используют потому, что тот обеспечивает более или менее стандартное заполнение шаблона, а также реальное распределение букв и пробелов в абзацах, которое не получается при простой дубликации "Здесь ваш текст.. Здесь ваш текст.. Здесь ваш текст.." Многие программы электронной вёрстки и редакторы HTML используют Lorem Ipsum в качестве текста по умолчанию, так что поиск по ключевым словам "lorem ipsum" сразу показывает, как много веб-страниц всё ещё дожидаются своего настоящего рождения. За прошедшие годы текст Lorem Ipsum получил много версий. Некоторые версии появились по ошибке, некоторые - намеренно (например, юмористические варианты).'''
    },
]


def articles(request):
    return render(request, 'articles.html', {
        'articles': article_data
    })


def article(request, number):
    if number < len(article_data):
        return render(request, 'article.html', article_data[number])
    else:
        return redirect('/')


def status(request):
    return HttpResponse('<h2>OK<h2>')
