from datetime import datetime

from django.conf import settings
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, redirect

from web.models import Article


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

        Article(
            name=name,
            date=datetime.now(),
            text=text.replace('/n', '<br />')
        ).save()
        return redirect('/articles')


def articles(request):
    return render(request, 'articles.html', {
        'articles': Article.objects.all()
    })


def article(request, number):
    arts = Article.objects.filter(id=number)

    if len(arts) == 1:
        return render(request, 'article.html', model_to_dict(arts[0]))
    else:
        return redirect('/')


def status(request):
    return HttpResponse('<h2>OK<h2>')
